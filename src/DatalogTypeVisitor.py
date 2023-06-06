from typing import List, NoReturn, Dict
from DatalogVisitor import DatalogVisitor
from DatalogParser import DatalogParser

from enum import Enum


class BaseType(Enum):
    Integer, Boolean, String = range(3)

# Only handle type checking.


class DatalogTypeVisitor(DatalogVisitor):

    def __init__(self) -> None:
        # { Students: [id: int, name : string, age: int], ... }
        self.typePerEdbDictionnary = dict()
        self.edbColumnName = dict()  # { Students: [id, name, age], ... }

    def visitBasicType(self, ctx):
        assert ctx.mytype is not None
        type = ctx.mytype.type
        if type == DatalogParser.INTTYPE:
            return BaseType.Integer
        elif type == DatalogParser.BOOLTYPE:
            return BaseType.Boolean
        elif type == DatalogParser.STRINGTYPE:
            return BaseType.String
        else:
            raise Exception("Unknown type")

    def visitIntAtom(self, ctx) -> int:
        return BaseType.Integer

    def visitBooleanAtom(self, ctx) -> bool:
        return BaseType.Boolean

    def visitStringAtom(self, ctx) -> str:
        return BaseType.String

    def visitColumnDecl(self, ctx):
        # add the column to an array set.
        type = self.visit(ctx.typee())  # get the type of the column.
        columnName = ctx.ID_CHAR().getText()
        columnTypePair = dict()
        columnTypePair[columnName] = type
        return [columnTypePair]

    def visitColumnTypeList(self, ctx) -> List[str]:
        # Récupère une liste de dictionnaire des noms de colonnes et type associé.
        columnTypeDictList = self.visit(ctx.columnType_l())
        # On récupère et on ajoute le nom de la première colonne avec son type à la liste.
        columnTypeDict = self.visit(ctx.columnType())[0]
        # To respect declaration order.
        columnTypeDictList.insert(0, columnTypeDict)
        return columnTypeDictList

    def visitEdbTypeDefinitionBase(self, ctx) -> None:
        # récupère la liste de tous les dictionnaires avec leur nom de colonne et leur type
        columnNameWithTypeList = self.visit(ctx.columnType_l())
        edbName = ctx.EDB_RELATION_NAME().getText()
        # initialise la liste avec les types des colonnes associés à l'edb.
        self.typePerEdbDictionnary[edbName] = columnNameWithTypeList
        print(self.typePerEdbDictionnary)
