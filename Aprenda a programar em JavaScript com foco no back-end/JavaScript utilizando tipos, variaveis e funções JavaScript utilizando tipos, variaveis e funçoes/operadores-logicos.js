const notaFinal = 5;
const faltas = 7;
const advertencia = 0;

if (notaFinal < 7 || faltas > 4) {
    console.log('Reprovado');
} else {
    console.log('Aprovado');
}

if (notaFinal < 7 && faltas > 4) {
    console.log('Reprovado');
} else {
    console.log('Aprovado');
}

if (faltas >= 2 && !advertencia) {
console.log('Recebeu bonus')
}