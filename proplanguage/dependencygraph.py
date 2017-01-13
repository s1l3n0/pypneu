import pydot
import ASPProgramLoader


class Vertex:
    # -- Fields --
    # name
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __hash__(self):
        return id(self)

    def to_pydot_node(self):
        return pydot.Node(str(self.content))


class Edge:
    # -- Fields --
    # source
    # target
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class DependencyGraph:
    # -- Fields --
    # rule_list
    # vertices
    # positive_edges
    # negative_edges

    def __init__(self, program):
        rule_list = program.rule_list
        self.vertices = []
        self.pos_edges = []
        self.neg_edges = []

        atoms = []
        for rule in rule_list:
            for atom in rule.extract_literals():
                if atom not in atoms:
                    atoms.append(atom)

        atom2vertex = {}

        for atom in atoms:
            vertex = Vertex(atom)
            self.vertices.append(vertex)
            atom2vertex[atom] = vertex

        for rule in rule_list:
            if (rule.is_norm_rule()):
                for source in rule.head.extract_asserted_literals():
                    for target in rule.body.extract_asserted_literals():
                        self.pos_edges.append(Edge(atom2vertex[source], atom2vertex[target]))
                    for target in rule.body.extract_naf_literals():
                        self.neg_edges.append(Edge(atom2vertex[source], atom2vertex[target]))

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def to_pydot_graph(self):
        graph = pydot.Dot(graph_type='digraph')
        vertex2node = {}

        for vertex in self.vertices:
            node = pydot.Node(str(vertex.content))
            graph.add_node(node)
            vertex2node[vertex] = node

        for edge in self.pos_edges:
            graph.add_edge(pydot.Edge(vertex2node[edge.source], vertex2node[edge.target]))

        for edge in self.neg_edges:
            graph.add_edge(pydot.Edge(vertex2node[edge.source], vertex2node[edge.target], color="red"))

        return graph

if __name__ == '__main__':
    program = ASPProgramLoader.parse_string("b :- a. c :- -a. d :- not a.")
    dependency_graph = DependencyGraph(program)
    dependency_graph.to_pydot_graph().write_png('../tmp/dependencyGraph.png')
    from PIL import Image
    img = Image.open('../tmp/dependencyGraph.png')
    img.show()
