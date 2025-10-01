const CryptoJS = require("crypto-js");
n=new Date().getTime().toString()

a=CryptoJS["HmacSHA1"](n, "xxxooo")["toString"]();
console.log(n)
console.log(a)