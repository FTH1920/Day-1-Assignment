from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

KV = '''
BoxLayout:
    orientation: 'vertical'
    
    MDTextField:
        id: input_field
        hint_text: "Masukan ekspresi matematika"
        multiline: False
        padding: [10, 10, 10, 10]
        
    GridLayout:
        cols: 4
        spacing: 10
        padding: [10, 10, 10, 10]
        
        MDRaisedButton:
            text: '('
            on_release: app.update_input_field('(')
            
        MDRaisedButton:
            text: ')'
            on_release: app.update_input_field(')')
            
        MDRaisedButton:
            text: 'x^'
            on_release: app.update_input_field('**')
            
        MDRaisedButton:
            text: '%'
            on_release: app.update_input_field('%')
        
        MDRaisedButton:
            text: '7'
            on_release: app.update_input_field('7')
            
        MDRaisedButton:
            text: '8'
            on_release: app.update_input_field('8')  
            
        MDRaisedButton:
            text: '9'
            on_release: app.update_input_field('9')  
        
        MDRaisedButton:
            text: '/'
            on_release: app.update_input_field('/')  
            
        MDRaisedButton:
            text: '4'
            on_release: app.update_input_field('4')  
            
        MDRaisedButton:
            text: '5'
            on_release: app.update_input_field('5')  
            
        MDRaisedButton:
            text: '6'
            on_release: app.update_input_field('6')
            
        MDRaisedButton:
            text: '*'
            on_release: app.update_input_field('*')  
            
        MDRaisedButton:
            text: '1'
            on_release: app.update_input_field('1')
        
        MDRaisedButton:
            text: '2'
            on_release: app.update_input_field('2')  
        
        MDRaisedButton:
            text: '3'
            on_release: app.update_input_field('3')    
            
        MDRaisedButton:
            text: '-'
            on_release: app.update_input_field('-')  
        
        MDRaisedButton:
            text: '0'
            on_release: app.update_input_field('0')  
        
        MDRaisedButton:
            text: '.'
            on_release: app.update_input_field('.')
            
        MDRaisedButton:
            text: '='
            on_release: app.calculate_result()
            
        MDRaisedButton:
            text: '+'
            on_release: app.update_input_field('+')
              
'''


class CalculatorApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def update_input_field(self, value):
        current_text = self.root.ids.input_field.text
        self.root.ids.input_field.text = f'{current_text}{value}'

    def calculate_result(self):
        try:
            expression = self.root.ids.input_field.text
            result = eval(expression)
            self.root.ids.input_field.text = str(result)
        except Exception as e:
            self.root.ids.input_field.text = "Error"


CalculatorApp().run()
