const notaPrimeiroBi = 8;
const notaSegundaBi = 6.3;
const notaTerceiroBi = 7;
const notaQuartoBi = Number('9.3');

let total = (notaPrimeiroBi + notaSegundaBi + notaTerceiroBi + notaQuartoBi) / 4;

if (total >= 7) {
    total += total * 0.1
}

console.log('A média é ' + total.toFixed(2));