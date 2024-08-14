qntSegurancas = 5
salarioSegurancas = 3000
qntDocente = 16
salarioDocente = 6000
qntDiretoria = 1
salarioDiretoria = 12500

totalEmpregados = qntDocente + qntDiretoria + qntSegurancas
print(totalEmpregados)

diferencaSalario = salarioDiretoria - salarioSegurancas
print(diferencaSalario)

media = (qntSegurancas * salarioSegurancas + qntDocente * salarioDocente + qntDiretoria * salarioDiretoria) / (totalEmpregados)
print(media)