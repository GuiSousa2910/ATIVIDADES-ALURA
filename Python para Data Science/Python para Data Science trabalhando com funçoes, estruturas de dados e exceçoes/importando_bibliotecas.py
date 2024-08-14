import matplotlib.pyplot as plt
from random import choices

estudantes = ['Joao', 'Maria', 'Gui']
notas = [8.5, 9, 6.5]
plt.bar(x = estudantes, height=notas)
plt.show()

estudantes_2 = ['Joao', 'Maria', 'Gui', 'Ana', 'Duda']
estudante = choices(estudantes_2)
print(estudante)