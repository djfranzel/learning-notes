
// there is only one type for numbers in JS!
// represents both int and float types found in other languages

var i = 5;
var i2 = 100;
var i3 = 1523;

// above is base 10 representation of a number
// below, can also represent numbers in hexadecimal (base 16) hex = 6, dec = 10
// can also do octal (base 8) 

// this is hexadecimal representation of 100
var i = 0x64; // 100 (in base 10)
console.log(i)

// this is octal representation of 100
var i = 0o144;
console.log(i)
var i = 0123;
console.log(i); // this is 83 in octal

// this generally isn't useful, but sometimes it is
// memory addresses are often in hexadecimal, so it might be useful there
// some values like CSS colors are written in base 16/hexadecimal
// #f2f2f2 converts to 15921906, the former is easier to write

// floats and exponential notation - also of type 'number'

var f = 120.45;
var f = 9.231e15; // 9.231 x 1015
var f2 = 3.87e-16; // 3.87 x 10-16


// there are rounding errors based on how these numbers are stored(?) - binary can't represent every number perfectly
// 0.1 is a repeating 0.000110011001100110011... in binary, so infinite and not possible to represent
var a = 0.1 + 0.7;
console.log(a); // 0.7999999999999999
var b = 0.3 + 0.5;
console.log(b); // 0.8

console.log(Number.MIN_VALUE); // 5e-324
console.log(Number.MAX_VALUE); // 1.7976931348623157e+308

// the above are very small and very large numbers, but JS can only represent numbers within this range
// if result is outside this range, result is Infinity, positive or negative

// NaN means not a number - can be result of failed arithmetic operation
// it is special in that NaN != NaN, must use 'isNaN(NaN)' function to check

// not totally sure, something about checking if exactly able to be represented in binary
console.log(Number.isSafeInteger(253))


// .toFixed() is a good rounding function - returns strings! must convert back
var numberObject = 123.4567;
console.log(numberObject.toFixed()); // 123
console.log(numberObject.toFixed(1)); // 123.5
console.log(numberObject.toFixed(2)); // 123.46
console.log(numberObject.toFixed(3)); // 123.457

// also returns strings, and hits total number precision, not decimals
// rounds to set digit number
var numberObject = 1.4567;
console.log(numberObject.toPrecision()); // 1.4567
console.log(numberObject.toPrecision(1)); // 1
console.log(numberObject.toPrecision(2)); // 1.5
console.log(numberObject.toPrecision(3)); // 1.46

// build in value from Math module
console.log(Math.PI)

// Date() is an object that once set, has many built in methods for accessing parts of that date
console.log(new Date())