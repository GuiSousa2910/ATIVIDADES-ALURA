// coerção explicita (Manual)
const numero = 10
console.log(numero, typeof numero)

const numeroString = String(numero)
console.log(numeroString, typeof numeroString)

const stringNumero = console.log(Number('12345'))
console.log(typeof stringNumero)

console.log(Boolean(-1111))
console.clear()

//COERÇÃO IMPLÍCITA (AUTOMÁTICA)

console.log('10' + 1)