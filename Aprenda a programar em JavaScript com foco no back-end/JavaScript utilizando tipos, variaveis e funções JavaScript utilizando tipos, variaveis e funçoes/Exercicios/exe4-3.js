const palindromo = (palavra) => {
    let palavraReversa = palavra.reverse();
    if (palavra === palavraReversa) {
        return 'é um palindromo';
    }
    else {
        return 'nao é um palindromo';
    }
};

console.log(palindromo('mirim'));
console.log(palindromo('gato'));