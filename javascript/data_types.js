
// 7 total datatypes in JS
// undefined, null, boolean, number, string, symbol (new in ES6), object

// 'typeof' operator will return all above plus 'function' - what datatype is function? an object? 

// undefined means there is no definition or object reference stored
// null means the object reference exists, but no data within - empty object pointer
// booleans, strings, numbers are primitive values
// object is a collection of properties
// array is a special object with ordered/numbered collection of values
// function is a special object with executable code


// good practice to initialize var to null since that creates the object reference
var product = null;
// assign object
if (product === null) {
  product = { name: 'chocolate' };
}

var amount;
var isDataAvailable = false;
if (!isDataAvailable) {
  // there is no data available to calculate amount and null is set
  amount = null;
}

// both null and undefined have an absence of value, so == evaluates true, not the case for ===
console.log(null == undefined); // true
console.log(null === undefined); // false


// booleans have only two potential values - true/false
// conditionals will convert '', 0, NaN, null, undefined to boolean 'false'
// conditionals will convert nonempty strings, nonzero nums, objects to 'true'
var test1 = false;
var test2 = true;

var a = 5, b = 5;
var test3 = (a == 5); // true
var test4 = (a === 5); // true

// symbols - what the heck are these? 
// created with Symbol() function
// NOT a constructor, but rather a factory
// they are always unique even if containing the same string value
// often used for private properties or methods

// var symbol = new Symbol('symbol'); // TypeError: Symbol is not a constructor 
// correct way:
var symbol = Symbol('mySymbol');
console.log(symbol); // Symbol(mySymbol)

var p1 = Symbol('p');
var p2 = Symbol('p');
var p3 = Symbol('p');
var object = {
  p: 1, // this is knocked out since another 'p' key is declared
  p: 2,
  [p1]: 1, // these are not since each Symbol is unique
  [p2]: 2,
};
object[p3] = 3;
console.log(object)

const NAME = Symbol()
const person = {
  [NAME]: 'Flavio'
}

person[NAME] //'Flavio'

const RUN = Symbol()
person[RUN] = () => 'Person is running'
console.log(person[RUN]()) //'Person is running'

// symbols are not enumerated, so skipped when running thru loops
// also not in Object.keys() or Object.getOwnPropertyNames()
// must use Object.getOwnPropertySymbols()

console.log(Object.getOwnPropertySymbols(person))