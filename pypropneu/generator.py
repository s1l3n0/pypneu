from pypropneu import Place, Transition, Arc, PetriNetExecution, Binding, BindingOperator, PetriNetAnalysis
from pyecpropneu import PetriNetEventCalculus

def buildSerial(p1, p2):
    t1 = Transition()
    a1 = Arc(p1, t1)
    a2 = Arc(t1, p2)
    return (t1, (a1, a2))

def buildFork(p1, t1, t2):
    a1 = Arc(p1, t1)
    a2 = Arc(p1, t2)
    return (a1, a2)

def buildJoin(t1, t2, p1):
    p1 = Place()
    t1 = Transition()
    t2 = Transition()
    a1 = Arc(t1, p1)
    a2 = Arc(t2, p1)
    return (a1, a2)

def buildBinding(n1, n2, n3, operator):
    b1 = Binding(operator)
    a1 = Arc(n1, b1)
    a2 = Arc(n2, b1)
    a3 = Arc(b1, n3)
    return ((a1, a2, a3), (b1))

def buildAndBinding(n1, n2, n3):
    return buildBinding(n1, n2, n3, BindingOperator.AND)

def buildOrBinding(n1, n2, n3):
    return buildBinding(n1, n2, n3, BindingOperator.OR)

def buildImpliesBinding(n1, n2, n3):
    return buildBinding(n1, n2, n3, BindingOperator.IMPLIES)

def buildEquivalenceBinding(n1, n2, n3):
    return buildBinding(n1, n2, n3, BindingOperator.EQUIV)

def buildSerialPetriNet(n=1):
    places = []
    transitions = []
    arcs = []

    p1 = Place(marking=True)
    places.append(p1)
    for i in range(1, n+1):
        p2 = Place()
        places.append(p2)
        (t1, (a1, a2)) = buildSerial(p1, p2)
        transitions.append(t1)
        arcs.extend([a1, a2])
        p1 = p2

    return places, transitions, arcs

def buildForkPetriNet(n=1, p1=None):
    places = []
    transitions = []
    arcs = []

    if p1 is None:
        p1 = Place(marking=True)

    places.append(p1)
    t1 = Transition()
    t2 = Transition()
    transitions.extend([t1, t2])
    (a1, a2) = buildFork(p1, t1, t2)

    p2 = Place()
    p3 = Place()

    a3 = Arc(t1, p2)
    a4 = Arc(t2, p3)
    arcs.extend([a1, a2, a3, a4])

    if n > 1:
        (inner_places_1, inner_transitions_1, inner_arcs_1) = buildForkPetriNet(n-1, p2)
        (inner_places_2, inner_transitions_2, inner_arcs_2) = buildForkPetriNet(n-1, p3)
    else:
        (inner_places_1, inner_transitions_1, inner_arcs_1) = ([p2], [], [])
        (inner_places_2, inner_transitions_2, inner_arcs_2) = ([p3], [], [])

    places.extend(inner_places_1)
    places.extend(inner_places_2)
    if len(inner_transitions_1) > 0: transitions.extend(inner_transitions_1)
    if len(inner_transitions_2) > 0: transitions.extend(inner_transitions_2)
    if len(inner_arcs_1) > 0: arcs.extend(inner_arcs_1)
    if len(inner_arcs_2) > 0: arcs.extend(inner_arcs_2)

    return places, transitions, arcs

evaluation_file = open("../benchmarks/benchmark.csv", "w")

for i in range(1, 11, 1):
    for n in range(1, 11, 1):
        (places, transitions, arcs) = buildForkPetriNet(n)
        net = PetriNetAnalysis(places, transitions, arcs)
        (models, timing, iterations) = net.run_analysis(bug=True)
        evaluation_file.write(str(i) + ";" + str(n) + ";" + "Fork" + ";" + "LPPN" + ";" + str(models) + ";" + str(timing) + ";\n")

        (places, transitions, arcs) = buildForkPetriNet(n)
        netEC = PetriNetEventCalculus(places, transitions, arcs)
        (models, timing) = netEC.solve(n)
        evaluation_file.write(str(i) + ";" + str(n) + ";" + "Fork" + ";" + "EC" + ";" + str(models) + ";" + str(timing) + ";\n")

    for n in range(1, 51, 5):
        (places, transitions, arcs) = buildSerialPetriNet(n)
        net = PetriNetAnalysis(places, transitions, arcs)
        (models, timing, iterations) = net.run_analysis()
        evaluation_file.write(str(i) + ";" + str(n) + ";" + "Serial" + ";" + "LPPN" + ";" + str(models) + ";" + str(timing) + ";\n")

        (places, transitions, arcs) = buildSerialPetriNet(n)
        netEC = PetriNetEventCalculus(places, transitions, arcs)
        (models, timing) = netEC.solve(n-1)
        evaluation_file.write(str(i) + ";" + str(n) + ";" + "Serial" + ";" + "EC" + ";" + str(models) + ";" + str(timing) + ";\n")

evaluation_file.close()
