
// multiple ways to declare a function
function info(name, surname) {
    var message = "Hello " + name + " " + surname;
    alert(message);
}

var info = function (name, surname) {
    var message = "Hello " + name + " " + surname;
    alert(message);
};

// this is like a clumsy version of python lambdas
// (8) invokes the function and the whole thing is condensed on one line
// could be useful to get dynamically generated strings or object, but is rather clumsy
var repeatedCharA = (function (length) { var s = ''; for (var i = 0; i < length; i++) { s += 'A' } return s; }(8));
console.log(repeatedCharA)

// I think the above is an example of an anonymous function - no name included, executes automatically
// advantage of this is it pulls context/variables out of the global scope

// this is cool! 
// object with a function
var calculation = {
    factor: 2,
    multiply: function (value) {
        return value * this.factor;
    },
    divide: function (value) {
        return this.factor / value;
    }
};
// while {} is an object literal, javascript can access Object() methods on this
// does JS convert to type Object on the fly like it does for string?
console.log(calculation.hasOwnProperty('factor'))

var result = calculation.multiply(5); // returns 10
console.log(result)

// 'this' refers to current context
// can reference outer scope if adding new variable accessible in nested scopes
var obj = {
    meth: function () {
        var that = this;
        func();

        function func() {
            console.log(obj === this); // false
            console.log(obj === that); // true
        }

    }
};

// this function provides a default value as the second argument
// exactly the same as python
function power(x, n = 2) {
    result = 1;
    for (let i = 1; i <= n; i++) {
        result = result * x;
    }
    return result;
}

console.log(power(2, 3)); // 8
console.log(power(2)); // 4

// a function stores arguments in a list called 'arguments'
// they are explicityly set in the (x, y), but actually exist in the 'arguments' variable
function add(x, y) {
    var result = 0;
    if (arguments.length == 2) {
        result = x + y;
    } else {
        for (let i = 0; i < arguments.length; i++) {
            result = result + arguments[i];
        }
    }
    return result;
}

var result = add(3, 5); // 8
var result2 = add(3, 5, 6); //14
console.log(result);
console.log(result2)

// a little bit nicer lambda
var calculator = {};
calculator.multiply = function (x, y) { return x * y; };
var result = calculator.multiply(3, 2); // 6

// this is similar to closures, but the function is passed in
function calculations(a, b, operation) {
    a = parseInt(a);
    b = parseInt(b);
    return operation(a, b);
}

var result = calculations('2', '5', function (x, y) {
    return 2 ** (x + y);
}); // 14
console.log(result)


// since 'temp' doesn't have 'var', it will be global by default
function getHalf(value) {
    temp = 2;
    return value / temp;
}

var half = getHalf(10); // 5
console.log(temp); // 2

// three JS scopes - global, block, local

// arrow functions!
// these are anonymous and do not have 'this', 'arguments', or 'super'
// can pass arguments, but don't have the local variable
var numbers = [1, 3, 4, 7];
var numbersIncreasedBy10 = numbers.map(x => x + 10);
var numbersIncreasedBy10 = numbers.map(x => { return x + 10 });
console.log(numbersIncreasedBy10)


// using 'call' function on objects
// this changes the scope so that the execution context becomes the 'this'
const person = {
    fullName: function () {
        return this.firstName + " " + this.lastName;
    }
}

const person1 = {
    firstName: "John",
    lastName: "Doe"
}

const person2 = {
    firstName: "Jane",
    lastName: "Doe"
}

firstName = 'David';
lastName = 'Franzel';

// this calls the fullName function and the 'this' in the function refers to the context of execution
console.log(person.fullName.call());

// Call the fullName() function of the person object using person1 as the "this" value
const fullName1 = person.fullName.call(person1); // returns "John Doe"
console.log(fullName1);

// Call the fullName() function of the person object using person2 as the "this" value
const fullName2 = person.fullName.call(person2); // returns "Jane Doe"
console.log(fullName2);

// apparently apply() function just requires an array instead of an object
console.log(person.fullName.apply());

// I can't think of any use cases where it would be useful to pass a different context in a function
// this sounds like complicated code perhaps
// might be some though
// I should probably understand this deeper than I do

