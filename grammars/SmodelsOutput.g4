grammar SmodelsOutput;

@header {}

/*----------------
* PARSER RULES
*----------------*/

program : (statement_list)? EOF ;

statement_list : statement (statement_list)? ;

statement
: SMODELSHEADER
  answerset_list
  FALSE
  DURATION ': ' FLOAT
  CHOICEPOINTS ': ' INTEGER
  WRONGCHOICES ': ' INTEGER
  ATOMS ': ' INTEGER
  RULES ': ' INTEGER
  PICKEDATOMS ': ' INTEGER
  FORCEDATOMS ': ' INTEGER
  TRUTHASSIGNMENTS ': ' INTEGER
  SIZESEARCHSPACE ': ' INTEGER ' (' INTEGER ')'
;

answerset_list : (answerset)+ ;

answerset
: ANSWERHEADER ': ' INTEGER
  STABELMODELHEADER ': ' fact_list ;

fact_list : literal (fact_list)? ;

/** A literal can be positive or negative. */
literal : ( MINUS )? pos_literal ;

/** A positive literal consists of symbols (no predicates) or symbols and terms (atom literal). */
pos_literal : predicate ( LPAR list_parameters RPAR )? ;

/** Parameters are identifiers, constants or other positive literals, separated by comma. */
list_parameters :  (identifier | constant | pos_literal) (COMMA list_parameters)? ;

predicate : IDENTIFIER ;
identifier : IDENTIFIER ;
constant : INTEGER ;

/*----------------
* LEXER RULES
*----------------*/

SMODELSHEADER : 'smodels version 2.34. Reading...done' ;
ANSWERHEADER : 'Answer' ;
STABELMODELHEADER : 'Stable Model' ;
FALSE : 'False' ;
DURATION : 'Duration' ;
CHOICEPOINTS : 'Number of choice points' ;
WRONGCHOICES : 'Number of wrong choices' ;
ATOMS : 'Number of atoms' ;
RULES : 'Number of rules' ;
PICKEDATOMS : 'Number of picked atoms' ;
FORCEDATOMS : 'Number of forced atoms' ;
TRUTHASSIGNMENTS : 'Number of truth assignments' ;
SIZESEARCHSPACE : 'Size of searchspace (removed)' ;

MINUS : '-' ;
COMMA : ',' ;
LPAR : '(' ;
RPAR : ')' ;

INTEGER : '0' | [1-9] (([0-9])*)? ;
FLOAT : [0-9] ('.' ([0-9])*)? ;
IDENTIFIER: [a-z] ([0-9a-zA-Z_])* ;

// necessary to remove trailing spaces
SPACES : [ \u000B\t\r\n] -> channel(HIDDEN) ;