# pypneu
*Python library for Logic Programming Petri Nets (LPPN)*

LPPN integrates procedural aspects specified by Petri Nets with declarative aspects relative to objects and events specified in Logic Programming (ASP). 
`pypneu` exploits the python module of `clingo`; this means that an instance of the declarative bindings is maintained without requiring regrounding at each cycle, thus improving performances.

current limitations: *only propositional logic*

## usage

Execution of a LPPN with hybrid operational semantics: brute force execution for the Petri Net, ASP solving for bindings on places and on transitions
```
net = PetriNetExecution(PetriNetStructure(places, transitions, arcs, p_bindings, t_bindings))
iterations = net.run_simulation(nsteps)
```

Analysis of a LPPN with hybrid operational semantics: extends execution with backtracking for identifying all possible paths:
```
net = PetriNetAnalysis(places, transitions, arcs, p_bindings, t_bindings)
(models, timing, iterations) = net.run_analysis(nsteps)
```

Analysis of a LPPN via denotational semantics: mapping the LPPN to a ASP program using event calculus (EC) and solving it:
```
netEC = PetriNetEventCalculus(places, transitions, arcs, p_bindings, t_bindings)
(models, timing) = netEC.solve(nsteps)
```

## files

- **pypneu**: basic Petri Nets (PN) interpreter (execution, analysis) 
- **pypropneu**: propositional LPPNs interpreter providing two operational semantics 
  - *hybrid*: separating the procedural components (brute execution + backtracking) and the declarative components (determined by clingo)
  - *denotational*: translating the net to ASP using Event-Calculus, and calling `clingo`.
- **proplanguage**: propositional ASP-like language parser

## dependencies

**clingo** (the ASP solver)
- download the sources from [https://github.com/potassco/clingo]
- compile the python library following the instructions
- add the library to the project dependencies 

To work on the grammars, you need to download the ANTLR complete JAR file and the necessary Python module.
The easiest way is using pip.

> pip install antlr4-python2-runtime

