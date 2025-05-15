import matplotlib.pyplot as plt

temperatura = [30, 27, 27, 33, 25]
dias = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex']

plt.title("Temperatura máxima ao longo da semana")
plt.ylabel("Temperatura")
plt.xlabel("Dia da semana")
#plt.plot(dias, temperatura)

#plt.grid(True)
#plt.ylim(20, 35)
#plt.yticks(range(0, 35, 2))
#plt.plot(dias, temperatura, color="purple")

plt.bar(dias, temperatura, color="purple")

plt.show()