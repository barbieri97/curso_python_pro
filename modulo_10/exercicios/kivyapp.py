from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from apirm import requisicoes

azul = '#9CD9CE'
amarelo = '#F2EA77'
marrom = '#735A3C'
rosa = '#F2B8A2'
branco = '#FDFDFD'

class RickAndMorty(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.link = 'https://rickandmortyapi.com/api/character/'
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}

        # add imagem
        self.foto = Image(source='imagens/rickandmorty2.jpg')
        self.window.add_widget(self.foto)

        # label widget 
        self.greeting = Label (
            text='Digite um numero entre 1 e 826 e se supreenda com um personagem de Rick and morty!',
            color='#9CD9CE',
            font_size = 18,
            )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = TextInput(
                        multiline=False,
                        padding_y = (20,20),
                        size_hint = (1, 0.5)
                        )
        self.window.add_widget(self.user)

        # button widget
        self.button = Button(
                      text='enviar',
                      size_hint = (0.5, 0.5),
                      bold = True
                      )
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)
        
        return self.window
        
    def callback(self, instance):
        self.link += self.user.text
        n, s = requisicoes(self.link)
        self.greeting.text = f"Esse/a é o/a {n} e ele está {'Vivo' if s == 'Alive' else 'Morto'}"
        self.foto.source = f'imagens/{n}.jpeg'
        self.link = 'https://rickandmortyapi.com/api/character/'

if __name__ == "__main__":
    RickAndMorty().run()