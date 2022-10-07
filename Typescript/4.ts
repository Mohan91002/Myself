class Employee
{
       eid    : number;
       ename  : string;
       esal   : number;
       constructor()
       {
              this.eid    = 123;
              this.ename  = "mumna" 
              this.esal   = 12345.00
              console.log("the values are initialized");
       }
       showValues():void
       {
              console.log(this.eid);
              console.log(this.ename);
              console.log(this.esal);
       }
}
var e1 = new Employee();
e1.showValues();
console.log()

class Employeee
{
       eid    : number;
       ename  : string;
       esal   : number;
       constructor()
       {
              console.log("the values are initialized");
       }
       getValues():void
       {
              this.eid    = 123;
              this.ename  = "mumna" 
              this.esal   = 12345.00
       }
       showValues():void
       {
              console.log(this.eid);
              console.log(this.ename);
              console.log(this.esal);
       }
}
var e = new Employeee();
e.getValues();
e.showValues();