grammar LparseInput;

@header {}

/*----------------
* PARSER RULES
*----------------*/

/** The overall program consists of directives, facts and rules. */
program : (directive | aspfact | asprule)* EOF ;

/** We consider the directives '#domain', 'hide' and 'show' */
directive
: DOMAIN list_literals DOT
| ( 'hide' | 'show' ) (list_literals)? DOT ;

/** A rule can be a normal rule or a constraint. */
asprule : normrule | constraint ;

/** A fact is the head followed by a dot, or a range. */
aspfact : ( head | rangedef ) DOT ;

/** Ranges relate interger values to an identifier */
rangedef : identifier LPAR rangemin=INTEGER RANGELEX rangemax=INTEGER RPAR;

/** A normal rule has a head and body. */
normrule : head ENTAILS body DOT ;

/** A constraint has NO head, only a body. */
constraint : ENTAILS body DOT ;

/** A choice operator has curly brackets . */
choice : ( choicemin=INTEGER )? LACC list_literals RACC ( choicemax=INTEGER )? ;

/** The head consists of a literal or a choice. */
head : literal | choice ;

/** The body consists of a list of literals or expressions separated or a choice construct. */
body : list_ext_literals_expressions | choice ;

/** A list of literals is separated by comma */
list_literals : literal ( COMMA list_literals )? ;

/** A list of literals and expressions is separated by comma */
list_ext_literals_expressions : ( ext_literal | expression ) ( COMMA list_ext_literals_expressions )? ;

/** An expression is a boolean function operating variables and constants */
expression : ( identifier | variable | INTEGER | num_expression ) ( EQ | NEQ | LT | LE | GT | GE ) ( IDENTIFIER | VARIABLE | INTEGER | num_expression) ;

/** A numeric expression is an integer expression made by numeric variables and constants */
num_expression : (variable | INTEGER) (PLUS | MINUS) (variable | INTEGER) ;

/** An extended literal adds the default negation to the classic literal */
ext_literal : ( NOT )? literal ;

/** A literal can be positive or negative. */
literal : ( MINUS )? pos_literal ;

/** A positive literal consists of symbols (no predicates) or symbols and terms (atom literal). */
pos_literal : predicate ( LPAR list_parameters RPAR )? ;

/** Parameters are identifiers or variables, separated by comma. */
list_parameters :  (identifier | variable | (MINUS)? constant | pos_literal | num_expression ) (COMMA list_parameters)? ;

predicate : IDENTIFIER ;
identifier : IDENTIFIER ;
constant : INTEGER ;
variable : VARIABLE ;


/*----------------
* LEXER RULES
*----------------*/

WS : (' ' | '\t' | '\n' | '\r' | '\f')+ -> skip ;

ENTAILS : ':-' ;

DOT : '.' ;
COMMA : ',' ;

LPAR : '(' ;
RPAR : ')' ;
LACC : '{' ;
RACC : '}' ;

EQ : '=' ;
NEQ : '!=' ;
GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;

NOT : 'not' ; // default negation
PLUS : '+' ;
MINUS : '-' ; // both for strong negation and arithmetic deletion

UNDERSCORE : '_' ;

DOMAIN : '#domain' ;

RANGELEX : '..' ;
INTEGER : '0' | [1-9] ([0-9])* ;
IDENTIFIER: [a-z] ([0-9a-zA-Z_])* ;
VARIABLE: [A-Z] ([0-9a-zA-Z_])* ;

// in addition to ASP comments (%) I added the standard C, Java comment style.
SINGLE_LINE_COMMENT : ('%' | '//') ~('\n'|'\r')* -> channel(HIDDEN) ;
MULTILINE_COMMENT : '/*' .*? ( '*/' | EOF ) -> channel(HIDDEN) ;