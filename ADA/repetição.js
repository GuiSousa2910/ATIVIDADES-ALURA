const input = require('readline-sync')

const numeroSorteado = 5
let numero = Number(input.question('Informe o numero que voce escolhe \n'))

while (numero !== numeroSorteado) {

    console.log('Voce errou, Tente novamente...')
    numero = Number(input.question('Informe o numero que voce escolhe \n'))
 
}

console.log('Voce acertou!!')
