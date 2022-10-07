var Employee = /** @class */ (function () {
    function Employee() {
        this.eid = 123;
        this.ename = "mumna";
        this.esal = 12345.00;
        console.log("the values are initialized");
    }
    Employee.prototype.showValues = function () {
        console.log(this.eid);
        console.log(this.ename);
        console.log(this.esal);
    };
    return Employee;
}());
var e1 = new Employee();
e1.showValues();
console.log();
var Employeee = /** @class */ (function () {
    function Employeee() {
        console.log("the values are initialized");
    }
    Employeee.prototype.getValues = function () {
        this.eid = 123;
        this.ename = "mumna";
        this.esal = 12345.00;
    };
    Employeee.prototype.showValues = function () {
        console.log(this.eid);
        console.log(this.ename);
        console.log(this.esal);
    };
    return Employeee;
}());
var e = new Employeee();
e.getValues();
e.showValues();
