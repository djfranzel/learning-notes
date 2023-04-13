
// 'string' is an ordered sequence of 16-bit Unicode chars
// backslash char '\' allows the char that follows it to be interpreted differently
var test = 'Don\'t worry, I\'m fine.';
// normally this would cause an error as there are too many ' chars

var special_chars = 'single quote: \', dbl: \", backslash: \\, new line: \n, carriage return: \r, tab: \t'
console.log(special_chars)

// string is primitive, but there are methods, so how? 
// javascript can on the fly convert the primitive to type string to access methods
// this is more convenient since string manipulation is common
// strings are immutable, and so any method that changes a string value actually returns a new mutated string

// template literals! `` this is replacing '' or "" with backtick ``
// better for simple reading since escape chars aren't required and can splice in variables with ${} notation


var temp_string = 'triangle & rectangle';
console.log(temp_string.charAt(1));
console.log(temp_string.indexOf('a'));
console.log(temp_string.lastIndexOf('angle')); // searches from end, like rfind() in python
console.log(temp_string.localeCompare('triangle')); // is temp_string before 'triangle' - that's this question
console.log(temp_string.localeCompare('zebra')); // -1 because temp_string is alphabetically less
// does the localeCompare deal with codepoints?

console.log(temp_string.concat('temp')); // this simply returns a concatenated string, can add multiple args to concat many times
console.log(temp_string.slice(2, 5)); // returns indexes 2-4 (same inclusive/exclusive as python)
console.log(temp_string.slice(2)); // removes 0,1 indexes, returns the rest
console.log(temp_string.slice(-2)); // keeps only last two
console.log(temp_string.slice(2, -2)); // returns from index 2 to 2 from the end, exclusive

console.log(temp_string.substring(2, 4)); // same as slice operation (does not support negative values!!)

console.log(temp_string.substr(2, 4)); // similar to substring, but the second instead represents length (deprecated!)

console.log(temp_string.toLowerCase());
console.log(temp_string.toUpperCase());
console.log(temp_string.trim()); // removes trailing and leading whitespaces
console.log(temp_string.replace('tri', 'abc')); // single replace on first occurence - there is a way to globally do this

console.log(temp_string.split(' ')); // splits on the provided char (default of space, tab, newline)

console.log(temp_string); // through all this, the original string is the same since strings are immutable
// these all above create temp objects and return the mutated value which can then be set in another var