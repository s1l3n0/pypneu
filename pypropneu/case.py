from pypropneu import Place, Transition, Arc, PetriNetExecution, Binding, BindingOperator, PetriNetAnalysis
from pyecpropneu import PetriNetEventCalculus

p1 = Place()
t1 = Transition(name="buy")
p2 = Place()
t2 = Transition(name="sell")
p3 = Place()

a1 = Arc(p1, t1)
a2 = Arc(t1, p2)
a3 = Arc(p2, t2)
a4 = Arc(t2, p3)

net = PetriNetEventCalculus((p1, p2, p3), (t1, t2), (a1, a2, a3, a4))

print net.build_event_calculus_program(0)