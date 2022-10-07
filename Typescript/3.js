function show() {
    console.log("munna");
}
show();
console.log();
function add(a, b) {
    var result;
    result = a + b;
    console.log("The add", result);
}
add(12, 13);
console.log();
function add1(a, b) {
    var result;
    result = a + b;
    return result;
}
var result;
result = add1(12, 13);
console.log("The add", result);
console.log();
// var object = new class
var num = new Number(100);
console.log("num value", num);
var str = new String("hello");
console.log(str);
console.log(Number.MAX_VALUE);
console.log(Number.MIN_VALUE);
console.log(Number.isInteger(-12.5));