alert('Boas Vindas ao Jogo do Número Secreto');

let numeroSecreto = 29;
console.log(numeroSecreto);
let chute = prompt('Escolha um número entre 1 e 30');

if(numeroSecreto == chute){
    alert(`Isso aí! Você acertou o número secreto ${numeroSecreto}`);
} else{
    alert('Você errou');
}
