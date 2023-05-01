# Generated from Datalog.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .DatalogParser import DatalogParser
else:
    from DatalogParser import DatalogParser

# This class defines a complete listener for a parse tree produced by DatalogParser.
class DatalogListener(ParseTreeListener):

    # Enter a parse tree produced by DatalogParser#program.
    def enterProgram(self, ctx:DatalogParser.ProgramContext):
        pass

    # Exit a parse tree produced by DatalogParser#program.
    def exitProgram(self, ctx:DatalogParser.ProgramContext):
        pass


    # Enter a parse tree produced by DatalogParser#statement.
    def enterStatement(self, ctx:DatalogParser.StatementContext):
        pass

    # Exit a parse tree produced by DatalogParser#statement.
    def exitStatement(self, ctx:DatalogParser.StatementContext):
        pass


    # Enter a parse tree produced by DatalogParser#edbTypeDeclaration.
    def enterEdbTypeDeclaration(self, ctx:DatalogParser.EdbTypeDeclarationContext):
        pass

    # Exit a parse tree produced by DatalogParser#edbTypeDeclaration.
    def exitEdbTypeDeclaration(self, ctx:DatalogParser.EdbTypeDeclarationContext):
        pass


    # Enter a parse tree produced by DatalogParser#edbTypeDefinitionBase.
    def enterEdbTypeDefinitionBase(self, ctx:DatalogParser.EdbTypeDefinitionBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#edbTypeDefinitionBase.
    def exitEdbTypeDefinitionBase(self, ctx:DatalogParser.EdbTypeDefinitionBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#columnTypeListBase.
    def enterColumnTypeListBase(self, ctx:DatalogParser.ColumnTypeListBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#columnTypeListBase.
    def exitColumnTypeListBase(self, ctx:DatalogParser.ColumnTypeListBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#columnTypeList.
    def enterColumnTypeList(self, ctx:DatalogParser.ColumnTypeListContext):
        pass

    # Exit a parse tree produced by DatalogParser#columnTypeList.
    def exitColumnTypeList(self, ctx:DatalogParser.ColumnTypeListContext):
        pass


    # Enter a parse tree produced by DatalogParser#columnDecl.
    def enterColumnDecl(self, ctx:DatalogParser.ColumnDeclContext):
        pass

    # Exit a parse tree produced by DatalogParser#columnDecl.
    def exitColumnDecl(self, ctx:DatalogParser.ColumnDeclContext):
        pass


    # Enter a parse tree produced by DatalogParser#basicType.
    def enterBasicType(self, ctx:DatalogParser.BasicTypeContext):
        pass

    # Exit a parse tree produced by DatalogParser#basicType.
    def exitBasicType(self, ctx:DatalogParser.BasicTypeContext):
        pass


    # Enter a parse tree produced by DatalogParser#edbInsertion.
    def enterEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
        pass

    # Exit a parse tree produced by DatalogParser#edbInsertion.
    def exitEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
        pass


    # Enter a parse tree produced by DatalogParser#termListBase.
    def enterTermListBase(self, ctx:DatalogParser.TermListBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#termListBase.
    def exitTermListBase(self, ctx:DatalogParser.TermListBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#termList.
    def enterTermList(self, ctx:DatalogParser.TermListContext):
        pass

    # Exit a parse tree produced by DatalogParser#termList.
    def exitTermList(self, ctx:DatalogParser.TermListContext):
        pass


    # Enter a parse tree produced by DatalogParser#idbRule.
    def enterIdbRule(self, ctx:DatalogParser.IdbRuleContext):
        pass

    # Exit a parse tree produced by DatalogParser#idbRule.
    def exitIdbRule(self, ctx:DatalogParser.IdbRuleContext):
        pass


    # Enter a parse tree produced by DatalogParser#head.
    def enterHead(self, ctx:DatalogParser.HeadContext):
        pass

    # Exit a parse tree produced by DatalogParser#head.
    def exitHead(self, ctx:DatalogParser.HeadContext):
        pass


    # Enter a parse tree produced by DatalogParser#body.
    def enterBody(self, ctx:DatalogParser.BodyContext):
        pass

    # Exit a parse tree produced by DatalogParser#body.
    def exitBody(self, ctx:DatalogParser.BodyContext):
        pass


    # Enter a parse tree produced by DatalogParser#predicates.
    def enterPredicates(self, ctx:DatalogParser.PredicatesContext):
        pass

    # Exit a parse tree produced by DatalogParser#predicates.
    def exitPredicates(self, ctx:DatalogParser.PredicatesContext):
        pass


    # Enter a parse tree produced by DatalogParser#predicateDecl.
    def enterPredicateDecl(self, ctx:DatalogParser.PredicateDeclContext):
        pass

    # Exit a parse tree produced by DatalogParser#predicateDecl.
    def exitPredicateDecl(self, ctx:DatalogParser.PredicateDeclContext):
        pass


    # Enter a parse tree produced by DatalogParser#aggregateFunction.
    def enterAggregateFunction(self, ctx:DatalogParser.AggregateFunctionContext):
        pass

    # Exit a parse tree produced by DatalogParser#aggregateFunction.
    def exitAggregateFunction(self, ctx:DatalogParser.AggregateFunctionContext):
        pass


    # Enter a parse tree produced by DatalogParser#variableListBase.
    def enterVariableListBase(self, ctx:DatalogParser.VariableListBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#variableListBase.
    def exitVariableListBase(self, ctx:DatalogParser.VariableListBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#variableList.
    def enterVariableList(self, ctx:DatalogParser.VariableListContext):
        pass

    # Exit a parse tree produced by DatalogParser#variableList.
    def exitVariableList(self, ctx:DatalogParser.VariableListContext):
        pass


    # Enter a parse tree produced by DatalogParser#intAtom.
    def enterIntAtom(self, ctx:DatalogParser.IntAtomContext):
        pass

    # Exit a parse tree produced by DatalogParser#intAtom.
    def exitIntAtom(self, ctx:DatalogParser.IntAtomContext):
        pass


    # Enter a parse tree produced by DatalogParser#stringAtom.
    def enterStringAtom(self, ctx:DatalogParser.StringAtomContext):
        pass

    # Exit a parse tree produced by DatalogParser#stringAtom.
    def exitStringAtom(self, ctx:DatalogParser.StringAtomContext):
        pass


    # Enter a parse tree produced by DatalogParser#booleanAtom.
    def enterBooleanAtom(self, ctx:DatalogParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by DatalogParser#booleanAtom.
    def exitBooleanAtom(self, ctx:DatalogParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by DatalogParser#aggregateOp.
    def enterAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        pass

    # Exit a parse tree produced by DatalogParser#aggregateOp.
    def exitAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        pass



del DatalogParser