const estaAprovado = true;

if (estaAprovado) {
    console.log('aprovado');
}

if ('0' == 0) { // => 2 iguais compara os valores
    console.log('passou');
} else {
    console.log('nao passou');
}

if ('0' === 0) { // => 3 iguais compara tambem o tipo do dado
    console.log('passou');
} else {
    console.log('nao passou');
}