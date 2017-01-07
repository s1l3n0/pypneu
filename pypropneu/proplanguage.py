import pprint

class Atom:
    # -- Fields --
    # name : String
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Literal(Atom):
    # -- Fields --
    # neg : Boolean
    def __init__(self, name, neg = False):
        Atom.__init__(self, name)
        self.neg = neg

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class ExtLiteral(Literal):
    # -- Fields --
    # naf : Boolean
    def __init__(self, name, neg = False, naf = False):
        Literal.__init__(self, name, neg)
        self.naf = naf

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Formula:
    # -- Fields --
    # operator : Operator
    # inputFormulas : Formula list
    # inputTerms : Term list
    def __init__(self, operator, inputFormulas = (), inputTerms = ()):
        self.operator = operator
        self.inputFormulas = inputFormulas
        self.inputTerms = inputTerms

    def __str__(self):
        return str(self.__dict__)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

class Operator:
    POS = 1
    NEG = 2
    NAF = 3
    AND = 4
    OR = 5
    XOR = 6
    IF = 7
    CHOICE = 8

class Rule:
    # -- Fields --
    # head : Expression
    # body : Expression
    def __init__(self, head = None, body = None):
        self.head = head
        self.body = body
