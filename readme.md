# pypneu
*Python libraries for Logic Programming Petri Nets (LPPN)*

In contrast to `pneu`/`lppneu`, coded in `Groovy`/`Java` and relying on `lparse+smodels`, here we exploit the python module of `clingo`, an instance of the declarative bindings is maintained within the script, without requiring regrounding at each cycle.
Performances are much better!

## Modules

- **pypneu**: basic Petri Nets (PN) interpreter (execution, analysis) 
- **pypropneu**: propositional LPPNs interpreter providing two operational semantics 
  - *hybrid*: separating the procedural components (brute execution + backtracking) and the declarative components (determined by clingo)
  - *denotational*: translating the net to ASP using Event-Calculus, and calling `clingo`.
- **proplanguage**: propositional ASP-like language parser

## Dependencies:

**clingo** (the ASP solver)
- download the sources from [https://github.com/potassco/clingo]
- compile the python library following the instructions
- add the library to the project dependencies 

To work on the grammars, you need to download the ANTLR complete JAR file and the necessary Python module.
The easiest way is using pip.

> pip install antlr4-python2-runtime

