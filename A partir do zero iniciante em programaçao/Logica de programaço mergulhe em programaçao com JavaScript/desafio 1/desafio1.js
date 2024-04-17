alert('Boas vindas ao nosso site!');

let nome = 'Lua';
let idade = 25;
let numeroDeVendas = 50;
let saldoDisponivel = 1000;

let erro = 'Erro! Preencha todos os campos';
alert(erro);

nome = prompt('Seu nome:');
idade = prompt('Sua idade');

if (idade >= 18) {
    alert('Pode dirigir');
}