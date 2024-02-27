let pessoa = {
    nome: "Gui",
    idade: "17",
    altura: "1.81"
}
console.log(pessoa)
console.log(pessoa.nome)
console.log(pessoa['nome'])
pessoa.namorada = true
console.log(pessoa)
console.clear()

for (let chave in pessoa){
    console.log(chave)
}