# Generated from Datalog.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DatalogParser import DatalogParser
else:
    from DatalogParser import DatalogParser

# This class defines a complete generic visitor for a parse tree produced by DatalogParser.

class DatalogVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by DatalogParser#program.
    def visitProgram(self, ctx:DatalogParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#statement.
    def visitStatement(self, ctx:DatalogParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbTypeDeclaration.
    def visitEdbTypeDeclaration(self, ctx:DatalogParser.EdbTypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbTypeDefinitionBase.
    def visitEdbTypeDefinitionBase(self, ctx:DatalogParser.EdbTypeDefinitionBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnTypeListBase.
    def visitColumnTypeListBase(self, ctx:DatalogParser.ColumnTypeListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnTypeList.
    def visitColumnTypeList(self, ctx:DatalogParser.ColumnTypeListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#columnDecl.
    def visitColumnDecl(self, ctx:DatalogParser.ColumnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#basicType.
    def visitBasicType(self, ctx:DatalogParser.BasicTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#edbInsertion.
    def visitEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termListBase.
    def visitTermListBase(self, ctx:DatalogParser.TermListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#termList.
    def visitTermList(self, ctx:DatalogParser.TermListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#idbRule.
    def visitIdbRule(self, ctx:DatalogParser.IdbRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#head.
    def visitHead(self, ctx:DatalogParser.HeadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#body.
    def visitBody(self, ctx:DatalogParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#predicates.
    def visitPredicates(self, ctx:DatalogParser.PredicatesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#predicateDecl.
    def visitPredicateDecl(self, ctx:DatalogParser.PredicateDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#aggregateFunction.
    def visitAggregateFunction(self, ctx:DatalogParser.AggregateFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#variableListBase.
    def visitVariableListBase(self, ctx:DatalogParser.VariableListBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#variableList.
    def visitVariableList(self, ctx:DatalogParser.VariableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#intAtom.
    def visitIntAtom(self, ctx:DatalogParser.IntAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#stringAtom.
    def visitStringAtom(self, ctx:DatalogParser.StringAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#booleanAtom.
    def visitBooleanAtom(self, ctx:DatalogParser.BooleanAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by DatalogParser#aggregateOp.
    def visitAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        return self.visitChildren(ctx)



del DatalogParser