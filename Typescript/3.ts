function show():void
{
       console.log("munna")
}
show();
console.log()

function add(a:number,b:number):void
{
       var result:number;
       result = a + b;
       console.log("The add",result)
}
add(12,13);
console.log()

function add1(a:number,b:number):number
{
       var result:number;
       result = a + b;
       return result;
}
var result:number;
result = add1(12,13);
console.log("The add",result)
console.log()

// var object = new class
var num = new Number(100);
console.log("num value",num)
var str = new String("hello")
console.log(str)
console.log(Number.MAX_VALUE)
console.log(Number.MIN_VALUE)