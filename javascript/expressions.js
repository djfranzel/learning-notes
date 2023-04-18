
// Literal values
// these are actual literal values, not variables
'text'
123

// Variable references
// these are identifiers and the JS interpreter will try to find the associated value
// x
// price
// undefined

// the 'this' keyword will return the current object/context
this

// these are reserved words that evaluate to literal values
true
false
null

var sum = function (x, y) {
    return x + y;
}
console.log(sum(3, 4));

// this generates a new instance of the Object class
var obj = new Object();

// calls the parent object, but can I get an example
// would just work with classes like python or java, simply calls parent object from a class that extends it
super(arg1, arg2);



// 'spread' - this allows arrays to expand/spread their values into separate variables
function sum(a, b, c) {
    return a + b + c;
}
 
var items = [2, 3, 4];
var result = sum(...items); // 9

// this is convenient for modifying arrays and also for passing arguments in functions!
var motorVehicles = ['car', 'motorcycle', 'truck'];
var railedVehicles = ['train', 'tram'];
var vehicles = ['bicke', ...motorVehicles, 'airplane', 'ship', ...railedVehicles];
console.log(vehicles); // [ "bicke", "car", "motorcycle", "truck", "airplane", "ship", "train", "tram" ]