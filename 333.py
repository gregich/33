from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class myApp(App):

    def build(self):

        Window.size = (360, 800)
        layout = BoxLayout(padding=10, orientation='vertical')
        self.label = Label(text='Привет!')
        self.nigger = TextInput(text='Цвет...')
        layout.add_widget(self.label)
        layout.add_widget(self.nigger)

        self.colors = {'#ff0000': 'Красный',
                  '#ff8800': 'Оранжевый',
                  '#ffff00': 'Желтый',
                '#00ff00': 'Зеленый',
            '#00ffff': 'Голубой',
        '#0000ff': 'Синий',
        '#ff00ff': 'Фиолетовый'}

        for key in self.colors.keys():
            layout.add_widget(Button(text=key, background_color=key, background_normal='', on_press=self.change))
        return layout

    def change(self, instance):
        self.label.text = self.colors.get(instance.text)
        self.nigger.text = instance.text

if __name__ == "__main__":
    myApp().run()