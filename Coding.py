from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
n = int(input('Digite o número de participantes: '))
lista = []
salva = []
for i in range(0, n, 1):
    lista.append(input('Digite o nome do participante: '))
lista.sort()
for i in range(0, n, 2):
    print(f'{lista[i]} x {lista[i+1]}')
    salva.append(f'{lista[i]} x {lista[i+1]}\n')
name = input('Digite o nome do arquivo a ser salvo com o sorteio: ')
arquivo = open(f'{name}.txt', 'a')
x = n//2
for i in range(0, x, 1):
    arquivo.write(f'{salva[i]}')
print('Arquivo salvo com sucesso!\n')
layout = [
    [sg.Text(salva)]
]
janela = sg.Window('Tabela', layout)
eventos, valores = janela.read()
while True:
    if eventos == sg.WIN_CLOSED:
        break

