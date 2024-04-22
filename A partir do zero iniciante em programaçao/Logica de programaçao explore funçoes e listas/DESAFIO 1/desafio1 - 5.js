function maior(x, y) {
    let n1 = x;
    let n2 = y;
    if (n1 > n2) {
        console.log(`${n1} é o maior`);
    }
    else {
        console.log(`${n2} é o maior`);
    }
}

let numero1 = prompt('Insira o primeiro numero:');
let numero2 = prompt('Insira o segundo numero:');

maior(numero1, numero2);