grammar Datalog;

// RULES: - les **EDB** devront **commencer** par une **lettre majuscule**. - les **IDB** doivent
// être en **minuscule**. - les **variables** devront être **composées seulement de majuscule**. -
// les **types de données** acceptés seront : - `bool` : true | false - `int`: [0-9] - **no float**
// - `string` : ‘hello world’, “hello”, “yoolo dsq q” ….

options {
	language = Python3;
}

// Parser rules

program: statement* EOF;

// TODO: change when we implement all of the rule for fact, idb and edbTypeDeclaration.
statement: fact | idbRule | edbTypeDeclaration;

// ===================== Typing and Defining EDB ===================== ✅
edbTypeDeclaration:
	ASSIGN 'type' LEFT_PAR edbTypeDefinition RIGHT_PAR DOT;

// Défini le type et déclare les nom de colonnes de l'edb.
edbTypeDefinition:
	EDB_RELATION_NAME LEFT_PAR columnType_l RIGHT_PAR # edbTypeDefinitionBase;

columnType_l:
	columnType						# columnTypeListBase
	| columnType COMA columnType_l	# columnTypeList;

columnType: ID_CHAR ':' typee # columnDecl;

typee: mytype = (INTTYPE | BOOLTYPE | STRINGTYPE) # basicType;

// ======================= EDB Insertion ======================= ✅ fact to create data in EDB
// relation. Artists(1, 'Bob Marley').
fact:
	EDB_RELATION_NAME LEFT_PAR term_l RIGHT_PAR DOT # edbInsertion;

term_l:
	atom				# termListBase
	| atom COMA term_l	# termList;

// ============ IDB Definition =========== TODO: q(x) :- p(x), r(x). for example.
idbRule: head ASSIGN body DOT;

head: IDB_NAME LEFT_PAR variable_l RIGHT_PAR;
body:
	predicates
	| aggregateFunction
	| predicates aggregateFunction;

predicates: predicate | predicates COMA predicates;

predicate: (
		idbPredicate = IDB_NAME
		| edbPredicate = EDB_RELATION_NAME
	) LEFT_PAR variable_l RIGHT_PAR # predicateDecl;

aggregateFunction: aggregateOp LEFT_PAR variable_l RIGHT_PAR;

variable_l:
	VARIABLE					# variableListBase
	| VARIABLE COMA variable_l	# variableList;

atom:
	INT					# intAtom
	| STRING			# stringAtom
	| (TRUE | FALSE)	# booleanAtom;

// Lexer rules

INTTYPE: 'int';
STRINGTYPE: 'string';
BOOLTYPE: 'bool';
TRUE: 'true';
FALSE: 'false';
aggregateOp: 'COUNT' | 'SUM' | 'AVG';

INT: [0-9]+;
STRING: '\'' (~'\'' | '\\\'')* '\'' | '"' (~'"' | '\\"')* '"';

EDB_RELATION_NAME: [A-Z][a-z]*;
ID_CHAR: [a-zA-Z0-9_] [a-zA-Z_0-9]*;
IDB_NAME: [a-z][a-z]*;
VARIABLE: [A-Z][A-Z]*;

ASSIGN: ':-';
COMA: ',';
DOT: '.';
LEFT_PAR: '(';
RIGHT_PAR: ')';

COMMENT:
	// % is a comment in Datalog.
	('%') ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;

