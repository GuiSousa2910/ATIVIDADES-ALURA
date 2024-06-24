const verificar = function (idade) {
    if (idade >= 18) {
        return 'Maior de idade';
    }
    else {
        return 'Menor de idade';
    }
};
console.log(verificar(10));