# from http://www.cs.uni-potsdam.de/~torsten/Potassco/Talks/robotsIULP15.pdf

from gringo import Control, Model, Fun

class Player:
    def __init__(self, horizon, positions, files):
        self.last_positions = positions
        self.last_solution = None
        self.undo_external = []
        self.horizon = horizon
        self.ctl = Control(['-c', 'horizon={0}'.format(self.horizon)])

        for x in files:
            self.ctl.load(x)
            self.ctl.ground([("base", [])])

    def solve(self, goal):
        for x in self.undo_external:
            self.ctl.assign_external(x, False)
        self.undo_external = []
        for x in self.last_positions + [goal]:
            self.ctl.assign_external(x, True)
            self.undo_external.append(x)
        self.last_solution = None
        self.ctl.solve(on_model=self.on_model)
        return self.last_solution

    def on_model(self, model):
        self.last_solution = model.atoms()
        self.last_positions = []
        for atom in model.atoms(Model.ATOMS):
            if atom.name() == "pos" and len(atom.args()) == 4 and atom.args()[3] == self.horizon:
                self.last_positions.append(Fun("pos", atom.args()[:-1]))

horizon = 15

encodings = ["board.lp", "targets.lp", "ricochet.lp", "optimization.lp"]

positions = [
    Fun("pos", [Fun("red"), 1, 1]),
    Fun("pos", [Fun("blue"), 1, 16]),
    Fun("pos", [Fun("green"),  16,  1]),
    Fun("pos", [Fun("yellow"), 16, 16])]

sequence = [
    Fun("goal", [13]),
    Fun("goal", [4]),
    Fun("goal", [7])]

player = Player(horizon, positions, encodings)

for goal in sequence:
    print player.solve(goal)