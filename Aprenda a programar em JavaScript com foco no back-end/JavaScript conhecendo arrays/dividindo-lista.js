const listaNomes = [
    'Ana', 'Bruno', 'Carlos', 'Diana', 'Eduardo',
    'Fernanda', 'Gabriel', 'Helena', 'Igor', 'Juliana',
    'Kleber', 'Laura', 'Marcos', 'Natália', 'Otávio',
    'Paula', 'Rafael', 'Sofia', 'Thiago', 'Úrsula', 'Vinícius'
];

const sala1 = listaNomes.slice(0, listaNomes.length / 2);
const sala2 = listaNomes.slice(listaNomes.length / 2);
console.log(sala1);
console.log(sala2);