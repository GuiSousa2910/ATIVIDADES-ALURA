console.clear()
let array = ["Gui", 24, 13.3, true]
console.log("Primeiro item da array é", array[0])
console.log("O tamanho da array é de", array.length)

for(let i = 0 ; i < array.length ; i++){
    console.log(array[i])
}
console.clear()

const array1 = [30, 23, 40, 21, 57]

console.log("Os 2 primeiros itens do array:",array1.slice(0,2))

console.log("Antes de adicionar:", array1)
array1.push(43, 3)
console.log("Depois de adicionar:", array1)

console.log("Antes de adicionar com unshift:", array1)
array1.unshift(9, 31)
console.log("Depois de adicionar com unshift:", array1)

console.log("Antes de remover com pop:", array1)
array1.pop()
console.log("Depois de remover com pop:", array1)

console.log("Antes de remover com shift:", array1)
array1.shift()
console.log("Depois de remover com shift:", array1)

const array2 = [1, 2, 3, 4]
const array3= [10, 9 , 8, 7]
console.log("Concatenados",array2.concat(array3))

let lugarNoArray = array1.indexOf(21)
console.log('O numero 21, está em que posição na array?', lugarNoArray)

console.log("O numero 10 existe nessa array?",array1.includes(10))

console.log("Array invertida",array1.reverse())