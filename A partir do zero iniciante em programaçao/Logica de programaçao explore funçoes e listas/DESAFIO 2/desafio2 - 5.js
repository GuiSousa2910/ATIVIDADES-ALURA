let numero = 2;
function tabuada(x) {
    for (var contador = 1; contador <= 10; contador++) {
        var conta = x * contador;
        alert(`${x} x ${contador} = ${conta}`);
    }
}

tabuada(numero);