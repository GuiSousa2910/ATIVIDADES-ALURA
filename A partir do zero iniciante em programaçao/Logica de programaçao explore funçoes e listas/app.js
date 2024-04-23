let lista = [];
let numeroLimite = 10;
let tentativa = 1;

function exibirTextoNaTela(tag, texto) {
    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
}

function exibirMensagemInicial() {
    exibirTextoNaTela('h1', 'Jogo do Número Secreto');
    exibirTextoNaTela('p', 'Escolha um número entre 1 e 10');
}

exibirMensagemInicial();

function verificarChute() {
    let chute = document.querySelector('input').value;

    if (chute == numeroAleatorio) {
        exibirTextoNaTela('h1', 'Acertou');

        let palavraTentativa = tentativa > 1 ? 'tentativas' : 'tentativa';

        console.log(tentativa);

        let mensagemTentativa = `Você descobriu com ${tentativa} ${palavraTentativa}`;

        exibirTextoNaTela('p', mensagemTentativa);

        document.getElementById('reiniciar').removeAttribute('disabled');
    }

    else {

        if (chute > numeroAleatorio) {
            exibirTextoNaTela('p', 'O número secreto é menor');
        }

        else {
            exibirTextoNaTela('p', 'O número secreto é maior');
        }

        tentativa++;
        limparCampo();
    }
}

function reiniciar() {
    exibirMensagemInicial();
    limparCampo();
    numeroAleatorio = gerarNumeroAleatorio();
    tentativa = 1;
    document.getElementById('reiniciar').setAttribute('disabled', true);
}

function gerarNumeroAleatorio() {
    let numeroEscolhido = parseInt(Math.random() * numeroLimite + 1);
    let qntElementosLista = lista.length;
    if (qntElementosLista == numeroLimite) {
        lista = [];
    }
    if (lista.includes(numeroEscolhido)) {
        return gerarNumeroAleatorio();
    } else {
        lista.push(numeroEscolhido);
        return numeroEscolhido;
    }
}

let numeroAleatorio = gerarNumeroAleatorio();

function limparCampo() {
    chute = document.querySelector('input');
    chute.value = '';
}