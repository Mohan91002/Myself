var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var Parent = /** @class */ (function () {
    function Parent() {
        this.a = 100;
        this.b = 200;
        console.log("hi");
    }
    Parent.prototype.getValues = function () {
        console.log(this.a);
        console.log(this.b);
    };
    return Parent;
}());
var Child = /** @class */ (function (_super) {
    __extends(Child, _super);
    function Child() {
        var _this = _super.call(this) || this;
        _this.c = 300;
        _this.d = 400;
        console.log("m");
        return _this;
    }
    Child.prototype.addition = function () {
        console.log(this.a + this.b + this.c + this.d);
        console.log(this.a + this.b + this.c - this.d);
        console.log(this.a + this.b * this.c + this.d);
        console.log(this.a / this.b + this.c + this.d);
    };
    return Child;
}(Parent));
var c1 = new Child();
c1.getValues();
c1.addition();
