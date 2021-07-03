import PySimpleGUI as sg

class TelaPython():
    def __init__(self):
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0))],
            [sg.Button('Enviar dados')]

        ]
        #Layout
        #Janela
        janela = sg.Window('Dado dos usuário').layout(layout)
        #Dados da Tela
        self.button, self.values = janela.Read()

    def iniciar(self):
        print(self.values)

tela = TelaPython()
tela.iniciar()