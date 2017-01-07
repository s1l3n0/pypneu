import gringo
import sys

ctl = gringo.Control()
ctl.load("program.lp")
ctl.ground([("base", [])])
ctl.solve(on_model=lambda m: sys.stdout.write(str(m) + "\n"))