const verdade = true;
const falso = false;

if (verdade && falso) {
    console.log('Passou no &&');
}
else if (verdade || falso) {
    console.log('Passou no ||');
}