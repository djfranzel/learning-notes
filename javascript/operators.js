
// basic arithmetic is nothing to be surprised about
// + - = * / % **

// Unary plus! this is new to me
// this converts a value to a number
// works like the Number() function

console.log(+'3.4'); // 3.4
console.log(+false); // 0
console.log(+'abc'); // NaN

// Unary negation! 
// works the same as + on non numbers
// negation
console.log(-false);

var x = 6;
var result = -x; // -6
var result = -'def'; // NaN

// Increment ++

var x = 2;
var y = ++x; // this is 3 because the ++ is before
var t = 2;
var u = t++; // this is still 2, since the ++ doesn't get applied
console.log(y); // 3
console.log(t); // 3
console.log(u); // 2

// 't' is incremented, but after the assigment

// Decrement --
// same as increment, just minus

// assignment operator, also potential combinations
// x += y
// x -= y
// x *= y
// x /= y
// x %= y

// Destructuring - way to extract multiple values from data in arrays and objects

// this can set independent variables to values of indexes
var container = [1, 'two', {x : 3}, 'test'];
// var [a, b, c] = container; // same as below, just alternative
var a, b, c;
[a, b, c] = container;
console.log(a); // 1
console.log(b); // two
console.log(c); // Object { x: 3 }

// works the same way with objects, just instead of indexes, uses key/value pairs to cast
// important to note that it doesn't keep the key, just the value
var obj = {alpha: 100, beta: 'dev'};
var {alpha, beta} = obj;
// ({delta, gamma} = obj2); // alternative - how does this work? it's funky
console.log(alpha); // 100
console.log(beta); // dev

// Comparison operators 
// == Equality
// this checks if values are the same - will do type conversion which results in broader equality results
console.log(0 == false); // true!
console.log(3 == '3'); // true! 

// != is inequality, same as ==
// === or !== is strict equality, checks type in addition to value of type'

// < less than operates similarly to == in the sense that it will convert type
// 
console.log(5 <= '5');

// && is Logical AND
// returns true only if both its operands return true
// || is Logical OR
// returns true if one of operands returns true
// ! is Logical NOT
// this is a unary operator
// will return true ONLY if operand can be converted to false

// Bitwise operators: & | ^ ~
// these are rarely used and operate on a low-level binary representation of numbers

// shorthand conditionals
var type = (x <= 90) ? 'light' : 'heavy';
