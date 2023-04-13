
// an identifier is the name of some var/object
// first char must be letter, $, or _
// subsequent can be letter, $, _, number
// uses UNICODE, but recommended to use ASCII - probably for common use?
// cannot use keywords or reserved words as identifiers!

// whitespaces don't technically impact anything, but use third for common standard/readability
var x =     10 ; 
var x=10;
var x = 10;

// semicolon is not technically required, but is good practice and allows code compression

if (x < 10) {
  x = x + 1;
  sum = sum + x;
}

if (x > 10)
  x = x - 1;

// both above are acceptable, for single statements in conditionals, no {} are required

// comments with '//' or '/* ...text... */' 
/*
text
*/

// keywords cannot be used as identifiers
// these are the typical if/break/else/default/do etc. 

// there is strict mode (what is this?) where more keywords are reserved - let, private, public etc.
// 'await' is reserved in module core (what is this?)

