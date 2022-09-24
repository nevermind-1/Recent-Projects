function checkPrice(){
var fruits = document.getElementById("fruits").value;
switch(fruits){
  case "mango":
    var amount = "$1.5";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    break;
    case "banana":
    var amount = "$2.5";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    break;
    case "apple":
    var amount = "$3.5";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    break;
    case "pineapple":
    var amount = "$4.5";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    break;
    case "cashew":
    var amount = "$0.5";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    break;
    case "orange":
    var amount = "$1.25";
    document.getElementById("price").innerHTML = "The price of " + fruits + " is " + amount;
    
    
}



}