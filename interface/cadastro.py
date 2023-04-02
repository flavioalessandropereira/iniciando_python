from PySimpleGUI import PySimpleGUI as sg

# criando layout
sg.theme('HotDogStand')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar o login?', size=(20,1))],
    [sg.Button('Entrar')]
]

# criando janela
janela = sg.Window('Tela de Login', layout)

# Lendo e executando o evento
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Entrar':
        if valores['usuario'] == 'fap' and valores['senha'] == '123':
          print('Bem-vindo aqui!')
