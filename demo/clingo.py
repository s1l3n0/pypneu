from gringo import Control, Model, Fun

import sys
import pprint

def on_model(model):
    solution = model.atoms()
    positions = []
    for atom in model.atoms(Model.ATOMS):
        print atom

ctl = Control()

ctl.load("program.lp")
ctl.ground([("base", [])])
with ctl.solve_iter() as it:
    for m in it: print m

# ctl.solve([], on_model)

#ctl.solve(on_model=lambda m: sys.stdout.write(str(m) + "\n"))

#with ctl.solve_iter() as it:
#    for m in it: print m



