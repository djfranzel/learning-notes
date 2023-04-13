

// this declares the variable
var volume;
console.log(volume); // will return undefined, since it is simply empty

var height, weight;
var height = 175, weight = 70;

// this will also declare the variable, but it is now stored as part of the global object
// not generally recommended as can cause bugs
// does this really transcend scope and go up levels?? 
quantity = 11;

function test() {
  temp = 12;
}

test(); // initialize the function

// this logs 'temp' var out, adding 'var' before 'temp' in its declaration would cause this to error!
// console.log(temp)

// 'let' is initializing a block-scoped variable which is limited in accessibility to its container scope
// introduced in ECMAScript 2015
let size = 12;

// all variables are loosely-typed, meaning that a var can contain a number, and then be reassigned to a string later
var speed = 100;
speed = "fast";

// accessing a var that doesn't exist results in 'ReferenceError'

// 3 scopes! global, local, block
// local is 'var' within a function, and no matter if in an 'if' statement, will show up anywhere in the function
// function params are also local
// block is 'let' (or const?) within the block, which may be an 'if' statement

// var globalVariable = "A"; // a global variable
// function testScope1() {
//   var localVariable = "B"; // a local variable
//   document.write(globalVariable); // A
//   document.write(localVariable); // B
// }

// document.write(globalVariable); // A
// document.write(localVariable); // ReferenceError

// // below blockVariable is not accessible outside of the 'if' block
// function testScope2() {
//   if (true) {
//       var localVariable = "X"
//       let blockVariable = "Y";
//   }
//   document.writeln(localVariable); // X
//   document.writeln(blockVariable); // ReferenceError
// }

// this is hoisting, which is idiosyncratic to javascript
// when a variable's value is called, it is hoisted, or moved to the top of the file
// the reference exists, but the value of the reference does not
// this causes 'undefined' errors, but not 'ReferenceErro
var x = 1;
function testHoisting() {
  // console.log(test_ref_error) // this causes a reference error
  console.log(x); // displays undefined
  var x = 2;
  console.log(x); // displays 2
  /* 
  adding this declaration within the function scope causes the above 'x' value to get confused
  'x' is declared in the scope, and also the scope above, but javascript does not grab the parent scope
  instead it says - there is an 'x' in this scope, thus we use that reference, but it isn't assigned a value yet
  so it is undefined!
  this would not be valid if there wasn't another 'x' value in the parent scope
  */
}
console.log(x)
testHoisting()
