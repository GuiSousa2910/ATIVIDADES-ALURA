function imc(x, y) {
    let media = (x / (y * y));
    console.log(`Seu IMC é: ${media}`);
}

let peso = parseFloat(prompt('Insira seu peso em kg:'));
let altura = parseFloat(prompt('Insira sua altura em metros:'));

imc(peso, altura);