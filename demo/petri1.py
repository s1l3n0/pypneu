#!/usr/bin/python
# or:  
# !C:\Python27\python.exe

# By David Tanzer, Copyright 2012, GNU Public License 
# Contributors: David Tweed, Ken Webb

import string
from random import random, randrange

# Species are represented just by their names, no class is needed

class Transition:
    # Fields used in this class: 
    #
    # transitionName
    # inputMap: speciesName -> inputCount
    # outputMap: speciesName -> outputCount 

    def __init__(this, transitionName):
        this.transitionName = transitionName
        this.inputMap = {}
        this.outputMap = {}

    def IsEnabled(this, labelling):
        for inputSpecies in this.inputMap.keys():
            if labelling[inputSpecies] < this.inputMap[inputSpecies]:
                return False  # not enough tokens
        return True  # good to go

    def Fire(this, labelling):
        print this.transitionName

        for inputName in this.inputMap.keys():
            labelling[inputName] = labelling[inputName] - this.inputMap[inputName]
        for outputName in this.outputMap.keys():
            labelling[outputName] = labelling[outputName] + this.outputMap[outputName]


class PetriNetBase:
    # Fields:
    # speciesNames
    # Transition list
    # labelling: speciesName -> token count 

    # constructor
    def __init__(this, speciesNames, transitionSpecs):
        this.speciesNames = speciesNames
        this.transitions = this.BuildTransitions(transitionSpecs)

    def BuildTransitions(this, transitionSpecs):

        transitions = []

        for (transitionName, inputSpecs, outputSpecs) in transitionSpecs:
            transition = Transition(transitionName)

            for degreeSpec in inputSpecs:
                this.SetDegree(transition.inputMap, degreeSpec)

            for degreeSpec in outputSpecs:
                this.SetDegree(transition.outputMap, degreeSpec)

            transitions.append(transition)

        return transitions

    def SetDegree(this, dictionary, degreeSpec):
        speciesName = degreeSpec[0]

        if len(degreeSpec) == 2:
            degree = degreeSpec[1]
        else:
            degree = 1

        dictionary[speciesName] = degree

    def PrintHeader(this):
        print string.join(this.speciesNames, ", ") + ", Transition"

    def PrintLabelling(this):
        for speciesName in this.speciesNames:
            print str(this.labelling[speciesName]) + ",",

    def SelectRandom(this, list):
        return list[randrange(len(list))]


class PetriNet(PetriNetBase):
    def RunSimulation(this, iterations, initialLabelling):

        this.PrintHeader()  # prints e.g. "H, O, H2O"

        this.labelling = initialLabelling

        this.PrintLabelling()  # prints e.g. "3, 5, 2"

        for i in range(iterations):
            if this.IsHalted():
                print "halted"
                return
            else:
                this.FireOneRule()
                this.PrintLabelling()

        print "iterations completed"

    def EnabledTransitions(this):
        return filter(
            lambda transition: transition.is_enabled(this.labelling),
            this.transitions)

    def IsHalted(this):
        return len(this.EnabledTransitions()) == 0

    def FireOneRule(this):
        this.SelectRandom(this.EnabledTransitions()).fire(this.labelling)


# now build a Petri net for two opposite transitions:
# combine: formation of water molecule
# split: dissociation of water molecule 

# combine: 2H + 1O -> 1H2O
combineSpec = ("combine", [["H", 2], ["O", 1]], [["H2O", 1]])

# split: 1H2O -> 2H + 1O 
splitSpec = ("split", [["H2O"]], [["H", 2], ["O", 1]])

petriNet = PetriNet(
    ["H", "O", "H2O"],  # species
    [combineSpec, splitSpec]  # transitions
)

initialLabelling = {"H": 5, "O": 3, "H2O": 4}

steps = 20
petriNet.RunSimulation(steps, initialLabelling)
