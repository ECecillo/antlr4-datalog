grammar Datalog;

options {
	language = Python3;
}

// Parser rules

program: statement* EOF;

// ======================= EDB Insertion ======================= 
fact:
	IDENTIFIER LEFT_PAR terms_l RIGHT_PAR DOT # edbInsertion;

//term_l: atom # termListBase | atom COMA term_l # termList;

// ============ IDB Definition =========== 

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

literal:
	predicate_sym '(' ')' # emptyPredicateDecl
	| predicate_sym '(' terms_l ')' # predicateDecl
	| AGGREGATE '(' terms_l ')' # aggregateDecl
	| predicate_sym # idbQuery
	| term '=' term # eqPredicate
	| term '!=' term # notEqualPredicate
	| VARIABLE ASSIGN external_sym '(' terms_l ')' # somthing;

predicate_sym
	 : IDENTIFIER # predicateRelationIdentifier
   | STRING # predicateString
   ;

external_sym: IDENTIFIER;

terms_l
   : term # termBase
   | term COMA terms_l # termList
   ;

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
AGGREGATE: 'COUNT' | 'SUM' | 'AVG';

ASSIGN: ':-';
COMA: ',';
DOT: '.';
LEFT_PAR: '(';
RIGHT_PAR: ')';

IDENTIFIER: [a-z] [a-zA-Z0-9_-]*;
VARIABLE: [A-Z_] [a-zA-Z_]*;

STRING: '\'' (~'\'' | '\\\'')* '\'' | '"' (~'"' | '\\"')* '"';

INTEGER: [0-9]+;

COMMENT:
	// % is a comment in Datalog.
	('%') ~[\r\n]* -> skip;

WS: [ \t\r\n]+ -> skip;

