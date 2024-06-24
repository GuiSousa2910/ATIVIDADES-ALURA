const numeros = (n1, n2, n3) => {
    if ((n1 > n2) && (n1 > n3)) {
        return `n1 é o maior de todos`;
    }
    else if ((n2 > n1) && (n2 > n3)) {
        return `n2 é o maior de todos`;
    } else {
        return `n3 é o maior de todos`;
    }
};

console.log(numeros(1, 2, 3));
console.log(numeros(3, 2, 1));
console.log(numeros(3, 4, 1));