// CONST => valor imutavel e nao é acessivel fora do bloco
const estudante = 'Caroline';
if (1 > 0) {
    console.log(estudante);
}

// LET => não pode ser acessado fora do bloco condicional
if (true) {
    let teste = 'Jose';
}
console.log(teste);

// VAR => pode ser acessado de qualquer lugar
if (true) {
    var teste2 = 'Jose';
}
console.log(teste2);


// TIPOS DE ESCOPO

// GLOBAL:
const nome = 'Camila';
function cumprimentar() {
    console.log(`Olá, ${nome}`);
}
cumprimentar();


// BLOCO:
if (true) {
    let nome = 'Ana';
    console.log(`Olá, ${nome}`);
}

// FUNÇÃO:
function ola() {
    const nome = 'Camila';
    const cumprimento = 'Olá';
   console.log(`${cumprimento}, ${nome}`);
}
