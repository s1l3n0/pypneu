# Generated from /Users/giovanni/dev/pypneu/grammars/ASPProgram.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ASPProgramParser import ASPProgramParser
else:
    from ASPProgramParser import ASPProgramParser

# This class defines a complete generic visitor for a parse tree produced by ASPProgramParser.

class ASPProgramVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ASPProgramParser#program.
    def visitProgram(self, ctx:ASPProgramParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#directive.
    def visitDirective(self, ctx:ASPProgramParser.DirectiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#asprule.
    def visitAsprule(self, ctx:ASPProgramParser.AspruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#aspfact.
    def visitAspfact(self, ctx:ASPProgramParser.AspfactContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#rangedef.
    def visitRangedef(self, ctx:ASPProgramParser.RangedefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#normrule.
    def visitNormrule(self, ctx:ASPProgramParser.NormruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#constraint.
    def visitConstraint(self, ctx:ASPProgramParser.ConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#choice.
    def visitChoice(self, ctx:ASPProgramParser.ChoiceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#head.
    def visitHead(self, ctx:ASPProgramParser.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#body.
    def visitBody(self, ctx:ASPProgramParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#list_literals.
    def visitList_literals(self, ctx:ASPProgramParser.List_literalsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#list_ext_literals_expressions.
    def visitList_ext_literals_expressions(self, ctx:ASPProgramParser.List_ext_literals_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#expression.
    def visitExpression(self, ctx:ASPProgramParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#num_expression.
    def visitNum_expression(self, ctx:ASPProgramParser.Num_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#ext_literal.
    def visitExt_literal(self, ctx:ASPProgramParser.Ext_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#literal.
    def visitLiteral(self, ctx:ASPProgramParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#pos_literal.
    def visitPos_literal(self, ctx:ASPProgramParser.Pos_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#list_parameters.
    def visitList_parameters(self, ctx:ASPProgramParser.List_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#predicate.
    def visitPredicate(self, ctx:ASPProgramParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#identifier.
    def visitIdentifier(self, ctx:ASPProgramParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#constant.
    def visitConstant(self, ctx:ASPProgramParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ASPProgramParser#variable.
    def visitVariable(self, ctx:ASPProgramParser.VariableContext):
        return self.visitChildren(ctx)



del ASPProgramParser