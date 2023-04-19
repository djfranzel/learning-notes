
// can throw an exception of any data type
throw 10;
throw true;
throw "Error 1";
throw { name: "MyError" };

// once thrown, program will go to nearest exception handler
// while any type can be thrown, try to use prebuilt types
Error
ReferenceError
SyntaxError
RangeError
TypeError
InternalError
EvalError
URIError

// type Error is the most generic, so I assume the parent most error object
throw new Error('Error has occurred');

class MyError extends Error {
    constructor(message) {
        super(message);
        this.name = 'MyError';
    }
}

// OR

// but, why would I do this? I think it's better to just create classes
function MyException(message) {
    this.name = 'MyException';
    this.message = message;
}

throw new MyException("Not allowed operation");

// this is an example of catching error by type
// I like python's way of catching them better
try {
    // Some code that may throw an error
} catch (error) {
    if (error instanceof TypeError) {
        // Handle the TypeError
        console.error("Caught a TypeError:", error.message);
    } else if (error instanceof RangeError) {
        // Handle the RangeError
        console.error("Caught a RangeError:", error.message);
    } else {
        // Handle other types of errors
        console.error("Caught an error:", error.message);
    }
} finally {
    console.log('finally hit')
}
