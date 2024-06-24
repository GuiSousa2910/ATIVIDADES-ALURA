// parametros
// retorno

function exibir(nome) {
    console.log(nome);
}

function exibirInfo(nome, nota) {
    return `o nome é ${nome} e a nota é ${nota}`;
}

function semReturn(nome, nota) {
    console.log(`o nome é ${nome} e a nota é ${nota}`);
}

exibir('Guilherme');
console.log(exibirInfo('Guilherme', 10));
semReturn('Jose', 10);