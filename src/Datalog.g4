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
//statement: fact | idbRule | edbTypeDeclaration;

// ======================= EDB Insertion ======================= ✅ fact to create data in EDB
fact:
	IDENTIFIER LEFT_PAR terms_l RIGHT_PAR DOT # edbInsertion;

//term_l: atom # termListBase | atom COMA term_l # termList;

// ============ IDB Definition =========== TODO: q(x) :- p(x), r(x). for example.
//idbRule: head ASSIGN body DOT;

//head: IDB_NAME LEFT_PAR variable_l RIGHT_PAR;

// body:
// 	predicates
// 	| aggregateFunction
// 	| predicates aggregateFunction;

statement
   : assertion
	 | edbTypeDeclaration
   | query
   ;

// ===================== Typing and Defining EDB ===================== ✅
edbTypeDeclaration:
	ASSIGN 'type' LEFT_PAR edbTypeDefinition RIGHT_PAR DOT;

// Défini le type et déclare les nom de colonnes de l'edb.
edbTypeDefinition:
	edb=IDENTIFIER LEFT_PAR columnType_l RIGHT_PAR # edbTypeDefinitionBase;

columnType_l:
	columnType						# columnTypeListBase
	| columnType COMA columnType_l	# columnTypeList;

columnType: IDENTIFIER ':' typee # columnDecl;

typee: mytype = (INTTYPE | BOOLTYPE | STRINGTYPE) # basicType;

assertion
   : clause DOT # assertionClause
   ;

// Used to access values in an edb or idb.
query
   : literal '?' # queryInstruction
   ;

// Used to remove clause in an edb or idb.
retraction
		: clause '~' # retractionClause
		;

clause:
	head=literal ASSIGN body # clauseRule
	| predicate_sym '(' terms_l ')' # clauseFact;

body
   : literal COMA body # bodyList
   | literal # bodyBase
   ;

// predicates: predicate | predicates COMA predicates;

literal:
	predicate_sym '(' ')'
	| predicate_sym '(' terms_l ')'
	| aggregateOp '(' terms_l ')'
	| predicate_sym
	| term '=' term
	| term '!=' term
	| VARIABLE ASSIGN external_sym '(' terms_l ')';

// predicate: (
// 		idbPredicate = IDB_NAME
// 		| edbPredicate = EDB_RELATION_NAME
// 	) LEFT_PAR variable_l RIGHT_PAR # predicateDecl;


// variable_l:
// 	VARIABLE					# variableListBase
// 	| VARIABLE COMA variable_l	# variableList;

predicate_sym
	 : IDENTIFIER # predicateRelationIdentifier
   | STRING # predicateString
   ;

external_sym: IDENTIFIER;

terms_l
   : term # termBase
   | term COMA terms_l # termList
   ;

// atom:
// 	INTEGER				# intAtom
// 	| STRING			# stringAtom
// 	| (TRUE | FALSE) # booleanConstant;

term:
		VARIABLE # termVariable
		| constant # termConstant;

constant:
	IDENTIFIER # identifierConstant
	| STRING # stringConstant
	| INTEGER # intConstant
	| (TRUE | FALSE) # booleanConstant;

// Lexer rules

INTTYPE: 'int';
STRINGTYPE: 'string';
BOOLTYPE: 'bool';
TRUE: 'true';
FALSE: 'false';
aggregateOp: 'COUNT' | 'SUM' | 'AVG';

//EDB_RELATION_NAME: [A-Z][a-z][a-z]*;
// VARIABLE: [A-Z][A-Z]*;
// IDB_NAME: [a-z][a-z]*;
//ID_CHAR: [a-zA-Z0-9_][a-zA-Z_0-9]*;

ASSIGN: ':-';
COMA: ',';
DOT: '.';
LEFT_PAR: '(';
RIGHT_PAR: ')';

// Conflict btwn VARIABLE AND EDB.
IDENTIFIER: [a-z] [a-zA-Z0-9_-]*;
VARIABLE: [A-Z] [a-zA-Z_]*;
//EDB_RELATION_NAME: [A-Z][a-z]+;

STRING: '\'' (~'\'' | '\\\'')* '\'' | '"' (~'"' | '\\"')* '"';

INTEGER: [0-9]+;

COMMENT:
	// % is a comment in Datalog.
	('%') ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;

