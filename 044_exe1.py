"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos
saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
A saída do programa deve ser conforme o exemplo abaixo:
 
Atleta: Rodrigo Curvêllo
  
Primeiro Salto: 6.5
Segundo Salto: 6.1
Terceiro Salto: 6.2
Quarto Salto: 5.4
Quinto Salto: 5.3
 
Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
num_saltos = 5
saltos = ['Primeiro','Segundo','Terceiro','Quarto','Quinto']
notas = []
mensagem = "Resultado final:\n"

nome = input("Digite o nome do atleta: ")

if nome != '':
	for salto in saltos:
		nota = float(input("%s Salto: "%salto))
		notas.append(nota)

	mensagem += "Atleta: " + nome + '\n' + "Saltos: "

	for i in range(num_saltos):
		if i == 4:
			mensagem += str(notas[i])+'\n'
		else:
			mensagem += str(notas[i])+' - '

	mensagem += "Média dos saltos: "+str(sum(notas)/len(notas))+" m"

print(mensagem)
