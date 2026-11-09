from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.result = TextInput(font_size=32, readonly=True, halign='right', multiline=False)
        
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.result)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]

        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                btn = Button(text=label, font_size=32)
                btn.bind(on_press=self.on_button_press)
                h_layout.add_widget(btn)
            layout.add_widget(h_layout)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        text = instance.text
        if text == 'C':
            self.result.text = ''
        elif text == '=':
            try:
                self.result.text = str(eval(current))
            except Exception:
                self.result.text = 'Error'
        else:
            self.result.text = current + text

if __name__ == '__main__':
    CalculatorApp().run()
  
