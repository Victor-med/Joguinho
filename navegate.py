from PySimpleGUI import PySimpleGUI as sg
sg.theme('Reddit')
n = 0
lista = []
layout = [
    [sg.Text('Número de participantes? '), sg.Input(key = 'npart', size=(20,1))],
    [sg.Button('Enviar')]
]
janela = sg.Window('Tela inicial', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Enviar':
        if int(valores['npart'])%2 != 0:
            print('Não tem como realizar o camp')
        else:
            print('Tudo certo')
            n = int(valores['npart'])
            layout2 = [
                [sg.Text('Participante 1'), sg.Input(key='p_um', size=(20, 1))],
                [sg.Text('Participante 2'), sg.Input(key='p_dois', size=(20, 1))],
                [sg.Text('Participante 3'), sg.Input(key='p_tres', size=(20, 1))],
                [sg.Text('Participante 4'), sg.Input(key='p_quatro', size=(20, 1))],
                [sg.Button('Realizar sorteio')]
            ]
            janela2 = sg.Window('Tela de inserção de jogadores', layout2)
            ev, val = janela2.read()
            if ev == sg.WIN_CLOSED:
                break
            if ev == 'Realizar sorteio':
                lista.append(val['p_um'])
                lista.append(val['p_dois'])
                lista.append(val['p_tres'])
                lista.append(val['p_quatro'])
                lista.sort()
                for i in range(0, n, 1):
                    print(f'{lista[i]}')
                layout3 = [
                    [sg.Text(lista[0]), sg.Text('x'), sg.Text(lista[1])],
                    [sg.Text(lista[2]), sg.Text('x'), sg.Text(lista[3])]
                ]
                janela3 = sg.Window('Sorteio', layout3)
                evs, srs = janela3.read()
                if evs == sg.WIN_CLOSED:
                    break