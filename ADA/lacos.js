const input = require('readline-sync')

let acumulador = 0

acumulador += 10
acumulador = acumulador + 2 
acumulador++

console.log(acumulador)
console.clear()

for (let i = 0 ; i < 10; i++){
    console.log("Repetir")
}
console.clear()

let soma = 0
let nota = 0
let i = 0

for ( i = 0; i < 3; i++){
    nota = Number(input.question(`Insira a nota ${i + 1} do aluno:\n`))

    soma = soma + nota
}

let media = soma / i
console.log("A média das notas do aluno é", media)

if(media >= 8){
    console.log("A média está excelente!")
}if(media === 7 || media === 6){
    console.log("A média está normal")
}if(media < 5){
    console.log("Está de recuperação")
}