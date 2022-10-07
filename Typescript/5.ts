class Parent
{
       a:number;
       b:number;
       constructor()
       {
              this.a = 100;
              this.b = 200;
              console.log("hi");
       }
       getValues():void
       {
              console.log(this.a);
              console.log(this.b);
       }

}
class Child extends Parent
{
       c:number;
       d:number;
       constructor()
       {
              super();
              this.c = 300;
              this.d = 400;
              console.log("m");
       }
       addition():void
       {
              console.log(this.a+this.b+this.c+this.d);
              console.log(this.a+this.b+this.c-this.d);
              console.log(this.a+this.b*this.c+this.d);
              console.log(this.a/this.b+this.c+this.d);
       }
}
var c1 = new Child();
c1.getValues();
c1.addition();