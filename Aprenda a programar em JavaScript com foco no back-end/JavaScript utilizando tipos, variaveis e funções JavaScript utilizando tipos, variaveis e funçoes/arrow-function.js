const estudanteReprovou = (notaFinal, faltas) => {
    if (notaFinal < 7 && faltas > 4) {
        return true;
    }
    else {
        return false;
    }
};

const exibirNome = (nome) => nome // por so ter 1 return nao precisa colocar a {} nem a palavra return

console.log(estudanteReprovou(6, 5));
console.log(estudanteReprovou(10, 2));
console.log(exibirNome('Gui'))