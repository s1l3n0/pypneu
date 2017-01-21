#!/usr/bin/python
# or:
# !C:\Python27\python.exe

# By Giovanni Sileno

import logging
from collections import deque
import copy

logging.basicConfig(filename='pypneu.log', filemode='w', level=logging.INFO)


class Node:
    # Fields:
    # inputs
    # outputs
    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.nid = None ## assigned when attached to a net

    def __str__(self):
        return self.nid

class ArcType:
    NORMAL = 1
    INHIBITOR = 2
    RESET = 3


class Arc:
    # Fields:
    # source
    # target
    # arc type
    # weight
    def __init__(self, source, target, type=ArcType.NORMAL, weight=1):
        self.source = source
        self.target = target
        self.type = type
        self.weight = weight
        source.outputs.append(self)
        target.inputs.append(self)


class Place(Node):
    # Fields:
    # name
    # marking
    def __init__(self, name=None, marking=0):
        Node.__init__(self)
        self.name = name
        self.marking = marking

    def flush(self):
        logging.info("Flushing " + self.name)
        self.marking = 0


class Transition(Node):
    # Fields:
    # name
    def __init__(self, name = None):
        Node.__init__(self)
        self.name = name

    def is_enabled(self):
        logging.info("checking transition " + self.name + " if enabled.")

        if len(self.inputs) == 0:
            logging.info("no inputs: disabled.")
            return False

        for input in self.inputs:
            if input.type == ArcType.NORMAL:
                if input.source.marking < input.weight:
                    logging.info("not sufficient tokens in place " + input.source.name + ": disabled.")
                    return False
            elif input.type == ArcType.INHIBITOR:
                if input.source.marking >= input.weight:
                    logging.info("threshold number of tokens reached in place " + input.source.name + ": inhibited.")
                    return False
        return True

    def consume_input_tokens(self):
        for input in self.inputs:
            if input.type == ArcType.NORMAL:
                logging.info("consuming " + str(input.weight) + " tokens in place " + input.source.name)
                input.source.marking -= input.weight
            else:
                raise ValueError("Unexpected type of input arc")

    def produce_output_tokens(self):
        for output in self.outputs:
            if output.type == ArcType.NORMAL:
                logging.info("producing " + str(output.weight) + " tokens in place " + output.target.name)
                for i in range (0, output.weight):
                    output.target.marking += 1
            elif output.type == ArcType.RESET:
                logging.info("resetting place " + output.target.name)
                output.target.flush()
            else:
                raise ValueError("Unexpected type of input arc")

    def fireable_events(self):
        if self.is_enabled():
            return [Group([self])]


class PetriNetStructure:
    # Fields:
    # places
    # transitions
    # arcs

    def __build_dict(self, nodes):
        dict = {}
        for node in nodes:
            nid = node.name
            if dict.has_key(nid):
                i = 1
                while dict.has_key(nid):
                    i += 1
                    nid = node.name + "_" + str(i)
            dict[nid] = node
            node.nid = nid
        return dict

    def __init__(self, places, transitions, arcs):
        self.places = places
        self.transitions = transitions
        self.arcs = arcs
        self.id2place = self.__build_dict(places)
        self.id2transition = self.__build_dict(transitions)

    def marking_to_string(self):
        output = ""
        for place in self.places:
            output = output + place.nid + ": " + str(place.marking) + ", "
        return output[:-2]


class PetriNetExecution(PetriNetStructure):

    def __init__(self, places, transitions, arcs):
        PetriNetStructure.__init__(self, places, transitions, arcs)

    def run_simulation(self, iterations):
        n = 0
        for i in range(iterations):
            print self.marking_to_string()
            logging.info("attempting to run step " + str(i))
            if not self.run_execution_step():
                break
            else:
                n = n + 1
                logging.info("step " + str(i) + " completed")

        print str(n) + " steps completed."

    def run_execution_step(self):
        firedTransitionEvents = self.brute_force_execution()
        return len(firedTransitionEvents) > 0

    def brute_force_execution(self):
        firedTransition = None

        for t in self.transitions:
            if t.is_enabled():
                firedTransition = t
                ## to have a rotation, I simply implement a FIFO mechanism
                self.transitions.remove(firedTransition)
                self.transitions.append(firedTransition)
                break

        if firedTransition is not None:
            return self.fire(Group([firedTransition]))
        else:
            return []

    def fire(self, fired_transitions_group):
        events = []
        for fired_transition in fired_transitions_group.set:
            print fired_transition.name + " fires"
            fired_transition.consume_input_tokens()
            events.append(fired_transition.produce_output_tokens())
        return events


class PetriNetAnalysis(PetriNetExecution):

    def __init__(self, places, transitions, arcs):
        PetriNetExecution.__init__(self, places, transitions, arcs)
        self.path_base = deque()
        self.state_base = deque()
        self.current_path = None
        self.current_state = None

    def status(self):
        # print "Summary: " + self.pathBase.toLog()
        print "######################## "
        if self.path_base is not None:
            print "paths: "
            for path in self.path_base:
                print str(path)
        if self.state_base is not None:
            print "states: "
            for state in self.state_base:
                print str(state)
        print "######################## "

    def run_analysis(self, iterations):
        n = 0
        for i in range(iterations):
            self.status()
            logging.info("attempting to run analysis step " + str(i))
            if not self.run_analysis_step():
                break
            else:
                n = n + 1
                logging.info("step " + str(i) + " completed")

        print str(n) + " steps completed."
        self.status()

    # save the current marking, if it was not already saved before
    def save_state(self):
        marking = {}
        for place in self.places:
            marking[place.nid] = place.marking
        for state in self.state_base:
            if state.marking == marking:
                return state

        new_state = State(marking=marking)

        fireable_groups = []
        if new_state.events_to_state is None:
            for transition in self.transitions:
                fireable_groups_per_transition = transition.fireable_events()
                if fireable_groups_per_transition is not None:
                    for group in fireable_groups_per_transition:
                        if group not in fireable_groups:
                            fireable_groups.append(group)
            new_state.events_to_state = {}

            for group in fireable_groups:
                new_state.events_to_state[group] = None

        self.state_base.append(new_state)

        return new_state

    # save the current state as consequent of a given firing
    def save_consequent(self, antecedent = None, fired_events = ()):
        state = self.save_state()
        self.current_path.steps.append(state)
        if len(fired_events) > 0:
            if fired_events in antecedent.events_to_state:
                antecedent.events_to_state[fired_events] = state
                self.current_path.events_per_step.append(fired_events)
            else:
                raise ValueError("I expected to have these events already saved in the antecedent.")
        return state

    def load_state(self, state):
        marking = state.marking
        for place in self.places:
            place.marking = marking[place.nid]

    def run_analysis_step(self):
        # create a new execution path if it does not exist
        if self.current_path is None: self.current_path = Path()

        # create a first state if it does not exist
        if self.current_state is None: self.current_state = self.save_consequent()

        next_events = None

        # the execution is complete if in the execution path we find the same state before the last one
        # if it is not complete, check for new events to fire
        if not (self.current_path.steps.index(self.current_state) + 1 < len(self.current_path.steps)):
            next_events = self.current_state.find_next_events()

        # if it is complete, backtrack to uncovered events [depth-first search]
        if next_events is None:
            print "Backtracking!!!"

            # record this completed path
            self.path_base.append(self.current_path)

            # start a new one cloning the previous one
            new_path = copy.copy(self.current_path)

            # go backwards until you don't find some next event
            for i in range(len(self.current_path.steps) - 1, 1, -1):
                step = self.current_path.steps[i]
                new_path.steps.pop()
                new_path.events_per_step.pop()

                next_events = step.find_next_events()

                if next_events is not None:
                    self.current_state = step
                    self.current_path = new_path
                    self.load_state(step)
                    break

        if next_events is None:
            return False
        else:
            self.fire(next_events)
            self.current_state = self.save_consequent(self.current_state, next_events)
            return True


class Path:

    def __init__(self):
        self.steps = []
        self.events_per_step = []

    def __str__(self):
        output = ""
        for i in range(0, len(self.steps)):
            output += "(" + str(self.steps[i]) + ")"
            if i < len(self.steps) - 1:
                output += " -- " + str(self.events_per_step[i]) + " -- "
        return output


class Group:

    def __init__(self, set=()):
        self.set = set

    def __len__(self):
        return len(self.set)

    def __hash__(self):
        key = ""
        for elem in sorted(self.set):
            key += str(elem)
        return hash(key)

    def __str__(self):
        output = ""
        for elem in self.set:
            output += str(elem) + ", "
        return output[:-2]

    def add(self, elem):
        if elem not in self.set:
            self.set.append(elem)



class State:

    def __init__(self, marking=None):
        self.marking = marking
        self.events_to_state = None

    def __str__(self):
        output = ""
        for nid in self.marking:
            output = output + nid + ": " + str(self.marking[nid]) + ", "
        return output[:-2]

    def find_next_events(self):
        print "["
        for group in self.events_to_state:
            print str(group) + ": " + str(self.events_to_state[group])
        print "]"

        next_events = None
        for key in self.events_to_state:
            if self.events_to_state[key] is None:
                next_events = key
                break
        return next_events


# really simple Petri net
# two places, a transition

# p1 = Place("p1", 3)
# p2 = Place("p2", 0)
# t1 = Transition("t1")
# a1 = Arc(p1, t1, ArcType.NORMAL, 1)
# a2 = Arc(t1, p2, ArcType.NORMAL, 1)
# net = PetriNet([p1, p2], [t1], [a1, a2])
# net.RunSimulation(5)

# simple Petri net with fork
# one place, two transition

p1 = Place("p1", 3)
t1 = Transition("t1")
t2 = Transition("t2")
a1 = Arc(p1, t1)
a2 = Arc(p1, t2)
net = PetriNetAnalysis([p1], [t1, t2], [a1, a2])

# net.run_simulation(5)

net.run_analysis(5)

