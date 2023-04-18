
// there are three major categories for controlling flow in javascript

// 1. conditionals (if, else, else if, switch)
// 2. loops (while, do while, for , for in, for of)
// 3. jumps (break, continue, labeled statement)

switch (true) {
    case false:
        console.log('yay!');
        break;
    case true:
        console.log('yay true!');
        break;
    default:
        console.log('default')
}

// the above switch only runs default if no conditions match
// 'break' is necessary to prevent default from running


// loops! 
// this is actually an infinite loop, as it will keep executing while the condition is true
while (true) {
    console.log('yay!');
}

// same as above, but runs one iteration before conditional is checked
do {
    console.log('yay!');
} while (true);

// most basic for loop, start, condition to match, increment expression
// not common, but important to not that these are all flexible and can be customized
for (var i = 0; i < 10; i++) {
    console.log(i)
}

// JS 'in' iterates all key/value pairs of the object
var obj = { x: 5, y: 'abc', z: true };
for (var prop in obj) {
    console.log(prop + " = " + obj[prop]);
}

// JS 'of' will iterate an array, map, set and others
var elements = ['a', 'b', 5, 6];
for (var element of elements) {
    console.log(element);
}

// jumps! 
// break will exit any loop or switch/case
// adding a label (break [label]) will break the iteration of that named object
// if no label, will break the loop or switch currently in context

// continue [label]
// this will break the current iteration of the loop and skip to the next
// can add a label, which will instruct the program which iteration to break/skip

var i, j;

outerLoop: // this provides a label for the loop that continue or break can access if nested deeper
for (i = 0; i < 3; i++) {
    j = 0;
    while (j < 3) {
        if (i === 1 && j === 1) {
            continue outerLoop;
        }
        console.log('i = ' + i + ', j= ' + j);
        j++;
    }
}
// Output:
// i = 0, j= 0
// i = 0, j= 1
// i = 0, j= 2
// i = 1, j= 0
// i = 2, j= 0
// i = 2, j= 1
// i = 2, j= 2