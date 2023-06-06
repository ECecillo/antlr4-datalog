# Generated from Datalog.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
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


    # Enter a parse tree produced by DatalogParser#edbInsertion.
    def enterEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
        pass

    # Exit a parse tree produced by DatalogParser#edbInsertion.
    def exitEdbInsertion(self, ctx:DatalogParser.EdbInsertionContext):
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


    # Enter a parse tree produced by DatalogParser#assertionClause.
    def enterAssertionClause(self, ctx:DatalogParser.AssertionClauseContext):
        pass

    # Exit a parse tree produced by DatalogParser#assertionClause.
    def exitAssertionClause(self, ctx:DatalogParser.AssertionClauseContext):
        pass


    # Enter a parse tree produced by DatalogParser#queryInstruction.
    def enterQueryInstruction(self, ctx:DatalogParser.QueryInstructionContext):
        pass

    # Exit a parse tree produced by DatalogParser#queryInstruction.
    def exitQueryInstruction(self, ctx:DatalogParser.QueryInstructionContext):
        pass


    # Enter a parse tree produced by DatalogParser#retractionClause.
    def enterRetractionClause(self, ctx:DatalogParser.RetractionClauseContext):
        pass

    # Exit a parse tree produced by DatalogParser#retractionClause.
    def exitRetractionClause(self, ctx:DatalogParser.RetractionClauseContext):
        pass


    # Enter a parse tree produced by DatalogParser#clauseRule.
    def enterClauseRule(self, ctx:DatalogParser.ClauseRuleContext):
        pass

    # Exit a parse tree produced by DatalogParser#clauseRule.
    def exitClauseRule(self, ctx:DatalogParser.ClauseRuleContext):
        pass


    # Enter a parse tree produced by DatalogParser#clauseFact.
    def enterClauseFact(self, ctx:DatalogParser.ClauseFactContext):
        pass

    # Exit a parse tree produced by DatalogParser#clauseFact.
    def exitClauseFact(self, ctx:DatalogParser.ClauseFactContext):
        pass


    # Enter a parse tree produced by DatalogParser#bodyList.
    def enterBodyList(self, ctx:DatalogParser.BodyListContext):
        pass

    # Exit a parse tree produced by DatalogParser#bodyList.
    def exitBodyList(self, ctx:DatalogParser.BodyListContext):
        pass


    # Enter a parse tree produced by DatalogParser#bodyBase.
    def enterBodyBase(self, ctx:DatalogParser.BodyBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#bodyBase.
    def exitBodyBase(self, ctx:DatalogParser.BodyBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#literal.
    def enterLiteral(self, ctx:DatalogParser.LiteralContext):
        pass

    # Exit a parse tree produced by DatalogParser#literal.
    def exitLiteral(self, ctx:DatalogParser.LiteralContext):
        pass


    # Enter a parse tree produced by DatalogParser#predicateRelationIdentifier.
    def enterPredicateRelationIdentifier(self, ctx:DatalogParser.PredicateRelationIdentifierContext):
        pass

    # Exit a parse tree produced by DatalogParser#predicateRelationIdentifier.
    def exitPredicateRelationIdentifier(self, ctx:DatalogParser.PredicateRelationIdentifierContext):
        pass


    # Enter a parse tree produced by DatalogParser#predicateString.
    def enterPredicateString(self, ctx:DatalogParser.PredicateStringContext):
        pass

    # Exit a parse tree produced by DatalogParser#predicateString.
    def exitPredicateString(self, ctx:DatalogParser.PredicateStringContext):
        pass


    # Enter a parse tree produced by DatalogParser#external_sym.
    def enterExternal_sym(self, ctx:DatalogParser.External_symContext):
        pass

    # Exit a parse tree produced by DatalogParser#external_sym.
    def exitExternal_sym(self, ctx:DatalogParser.External_symContext):
        pass


    # Enter a parse tree produced by DatalogParser#termBase.
    def enterTermBase(self, ctx:DatalogParser.TermBaseContext):
        pass

    # Exit a parse tree produced by DatalogParser#termBase.
    def exitTermBase(self, ctx:DatalogParser.TermBaseContext):
        pass


    # Enter a parse tree produced by DatalogParser#termList.
    def enterTermList(self, ctx:DatalogParser.TermListContext):
        pass

    # Exit a parse tree produced by DatalogParser#termList.
    def exitTermList(self, ctx:DatalogParser.TermListContext):
        pass


    # Enter a parse tree produced by DatalogParser#termVariable.
    def enterTermVariable(self, ctx:DatalogParser.TermVariableContext):
        pass

    # Exit a parse tree produced by DatalogParser#termVariable.
    def exitTermVariable(self, ctx:DatalogParser.TermVariableContext):
        pass


    # Enter a parse tree produced by DatalogParser#termConstant.
    def enterTermConstant(self, ctx:DatalogParser.TermConstantContext):
        pass

    # Exit a parse tree produced by DatalogParser#termConstant.
    def exitTermConstant(self, ctx:DatalogParser.TermConstantContext):
        pass


    # Enter a parse tree produced by DatalogParser#identifierConstant.
    def enterIdentifierConstant(self, ctx:DatalogParser.IdentifierConstantContext):
        pass

    # Exit a parse tree produced by DatalogParser#identifierConstant.
    def exitIdentifierConstant(self, ctx:DatalogParser.IdentifierConstantContext):
        pass


    # Enter a parse tree produced by DatalogParser#stringConstant.
    def enterStringConstant(self, ctx:DatalogParser.StringConstantContext):
        pass

    # Exit a parse tree produced by DatalogParser#stringConstant.
    def exitStringConstant(self, ctx:DatalogParser.StringConstantContext):
        pass


    # Enter a parse tree produced by DatalogParser#intConstant.
    def enterIntConstant(self, ctx:DatalogParser.IntConstantContext):
        pass

    # Exit a parse tree produced by DatalogParser#intConstant.
    def exitIntConstant(self, ctx:DatalogParser.IntConstantContext):
        pass


    # Enter a parse tree produced by DatalogParser#booleanConstant.
    def enterBooleanConstant(self, ctx:DatalogParser.BooleanConstantContext):
        pass

    # Exit a parse tree produced by DatalogParser#booleanConstant.
    def exitBooleanConstant(self, ctx:DatalogParser.BooleanConstantContext):
        pass


    # Enter a parse tree produced by DatalogParser#aggregateOp.
    def enterAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        pass

    # Exit a parse tree produced by DatalogParser#aggregateOp.
    def exitAggregateOp(self, ctx:DatalogParser.AggregateOpContext):
        pass



del DatalogParser