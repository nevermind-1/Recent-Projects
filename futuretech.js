const factorial = (n) => {
    if (n === 0) return 1

    return n * factorial(n-1)
}

console.log(factorial(5), solve())

function solve() {
    const num1 = prompt("Enter the first number: ")
    const num2 = prompt("Enter the second number: ")

    console.log("'+'\n '-'\n '*'\n '/'\n'")
    const operator = prompt("Choose an operator: \nHere")

    if(operator === '+') {
        add()
    }else if(operator === '-') {
        subtract()
    }else if(operator === '*') {
        multiply()
    }else if(operator === '/') {
        divide()
    }else {
        console.log('invalid details')
    }
    
    
}

function add() {
    result = num1 + num2
}

function subtract() {
    return num1 - num2;
}

function multiply() {
    return num1 * num2;
}

function divide() {
    if(num2 ===0) return undefined;

    return num1 / num2;
}

function exponent() {
    return num1 ** num2
}