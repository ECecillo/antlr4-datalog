from typing import Dict, List, cast
from DatalogParser import DatalogParser
from DatalogVisitor import DatalogVisitor


def create_dict(column_names: List[str], data: List):
    return dict(zip(column_names, data))


class MyDatalogVisitor(DatalogVisitor):
    def __init__(self):
        # Initialize any necessary data structures or variables here.
        # store all variable ids and values.
        self.dataPerEdbDictionnary = dict()
        # {
        #     Students: [
        #         {id: 1, name: "John", age: 20},
        #         {...},
        #         ...
        #     ],
        #     ...
        # }
        # edb are keys and value are array of column name.
        self.edbColumnName = dict()
        # { Students: [id, name, age], ... }

    def visitIntAtom(self, ctx) -> int:
        return int(ctx.getText())

    def visitBooleanAtom(self, ctx) -> bool:
        return ctx.getText() == "true"  # return true rule.

    def visitStringAtom(self, ctx) -> str:
        return ctx.getText()[1:-1]  # Remove the ""

    # Créer une liste avec les noms de colonnes.
    def visitColumnDecl(self, ctx) -> str:
        # add the column to an array set.
        return [ctx.ID_CHAR().getText()]

    def visitColumnTypeList(self, ctx) -> List[str]:
        # Récupère la liste des noms de colonnes et les retournes.
        columnNameList: List[str] = self.visit(ctx.columnType_l())
        # On récupère et on ajoute le nom de la colonne courante.
        columnName: str = self.visit(ctx.columnType())[0]
        # To respect declaration order.
        columnNameList.insert(0, columnName)
        return columnNameList

    def visitEdbTypeDefinitionBase(self, ctx) -> None:
        # récupère la liste de nom de colonne.
        columnNameList: List[str] = self.visit(ctx.columnType_l())
        edbName = ctx.EDB_RELATION_NAME().getText()
        # initialise la liste des noms de colonne de l'edb avec ce que l'on a récupéré.
        self.edbColumnName[edbName] = columnNameList
        self.dataPerEdbDictionnary[edbName] = []
        print(edbName, self.edbColumnName[edbName])

    def visitTermListBase(self, ctx) -> str or int or bool:
        return [self.visit(ctx.atom())]

    def visitTermList(self, ctx):
        valueList = self.visit(ctx.term_l())
        # Récupère ce qui devrait être l'id du tuple à ajouter et le met au début.
        value = self.visit(ctx.atom())
        valueList.insert(0, value)
        return valueList

    def visitEdbInsertion(self, ctx) -> None:
        # Récupère le nom de la relation.
        edbName = ctx.EDB_RELATION_NAME().getText()
        # Récupère la liste des valeurs.
        valueList = self.visit(ctx.term_l())  # [1, "John", 20] for example.
        # Récupère la liste des colonnes pour leur associer les valeurs.
        columnsNameForEDB = self.edbColumnName[edbName]
        self.dataPerEdbDictionnary[edbName].append(
            create_dict(columnsNameForEDB, valueList))
        print(self.dataPerEdbDictionnary)
