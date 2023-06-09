from typing import Dict, List, cast, Union
from DatalogParser import DatalogParser
from DatalogVisitor import DatalogVisitor
from datalog_types import Fact, Predicate, AggregateFunction, Rule


def create_dict(column_names: List[str], data: List):
    return dict(zip(column_names, data))


class MyDatalogVisitor(DatalogVisitor):
    def __init__(self):
        # Initialize any necessary data structures or variables here.
        # store all variable ids and values.
        self.dataPerEdbDictionnary = dict()
        self.database: List[Fact] = []
        # self.rulesToEvaluate: List[Union[Predicate, 'AggregateFunction']] = []
        self.rulesToEvaluate: List[Rule] = []
        # edb are keys and value are array of column name.
        self.edbColumnName = dict()
        # { Students: [id, name, age], ... }

    def visitIntConstant(self, ctx) -> int:
        return int(ctx.getText())

    def visitBooleanConstant(self, ctx) -> bool:
        return ctx.getText() == "true"  # return true rule.

    def visitStringConstant(self, ctx) -> str:
        return ctx.getText()[1:-1]  # Remove the ""

    def visitTermVariable(self, ctx) -> str:
        return ctx.getText()

    # Créer une liste avec les noms de colonnes.
    def visitColumnDecl(self, ctx) -> str:
        # add the column to an array set.
        return [ctx.IDENTIFIER().getText()]

    def visitColumnTypeList(self, ctx) -> List[str]:
        # Récupère la liste des noms de colonnes et la retournes.
        columnNameList: List[str] = self.visit(ctx.columnType_l())
        # On récupère et on ajoute le nom de la colonne courante.
        columnName: str = self.visit(ctx.columnType())[0]
        # To respect declaration order.
        # (Not optimized because it has to move all the elements of the array)
        columnNameList.insert(0, columnName)
        return columnNameList

    def visitEdbTypeDefinitionBase(self, ctx) -> None:
        # récupère la liste de nom de colonne.
        columnNameList: List[str] = self.visit(ctx.columnType_l())
        edbName: str = ctx.IDENTIFIER().getText()
        # initialise la liste des noms de colonne de l'edb avec ce que l'on a récupéré.
        self.edbColumnName[edbName] = columnNameList
        self.dataPerEdbDictionnary[edbName] = []

    def visitTermBase(self, ctx) -> str or int or bool:
        return [self.visit(ctx.term())]

    def visitTermList(self, ctx):
        valueList = self.visit(ctx.terms_l())
        # Récupère ce qui devrait être l'id du tuple à ajouter pour le mettre au début.
        value = self.visit(ctx.term())
        valueList.insert(0, value)
        return valueList

    def visitClauseFact(self, ctx) -> None:
        edb_name = self.visit(ctx.predicate_sym())
        edb_data = self.visit(ctx.terms_l())
        self.database.append(Fact(edb_name, edb_data))

    def visitPredicateRelationIdentifier(self, ctx):
        return ctx.IDENTIFIER().getText()

    def visitClauseRule(self, ctx):
        # Visit the IDB and create the relation in our memory array.
        headResult = self.visit(ctx.head)
        bodyResult = self.visit(ctx.body())
        self.rulesToEvaluate.append(Rule(headResult, bodyResult))

    def visitBodyBase(self, ctx):
        return [self.visit(ctx.literal())]

    def visitBodyList(self, ctx):
        predicate_list = self.visit(ctx.body())
        first_predicate = self.visit(ctx.literal())
        predicate_list.insert(0, first_predicate)
        return predicate_list

    def visitPredicateDecl(self, ctx):
        # Creating a Predicate Object using class decl
        predicate_name = self.visit(ctx.predicate_sym())
        variables = self.visit(ctx.terms_l())
        return Predicate(predicate_name, variables)

    def visitAggregateDecl(self, ctx):
        operation = ctx.AGGREGATE().getText()
        variables = self.visit(ctx.terms_l())
        if len(variables) > 2:
            return "Erreur: une aggregation prend 2 arguments (input_var, output_var)"
        else:
            input_var, output_var = variables
            return AggregateFunction(operation, input_var, output_var)
