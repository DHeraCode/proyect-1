from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
#from kivy.uix.boxlayout import BoxLayout
import math


class MedicionApp(App):
    def build(self):
        # Crear el layout principal
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Crear un label
        label = Label(text="Medición Ciego 1", font_size=24)
        layout.add_widget(label)

        # Crear el campo de entrada solo para números
        self.medicion_input = TextInput(hint_text="Ingrese la medición en cm", input_filter='float',font_size=32, multiline=False)
        layout.add_widget(self.medicion_input)

        # Crear un botón que calcule la medición multiplicada por 4
        calculate_button = Button(text="Calcular volumen", on_press=self.calcular, font_size=28)
        layout.add_widget(calculate_button)

        # Crear un label para mostrar el resultado
        self.result_label = Label(text="Equivale a: ", font_size=20)
        layout.add_widget(self.result_label)

        return layout

    def calcular(self, instance):
        try:
            # Obtener el valor ingresado
            h = float(self.medicion_input.text)

            # Multiplicar la medición por 4

            resultado = 1.994 * 1000* (   ( (math.pi*0.5645**2)/2 )   + ( (0.01*h - 0.5645)*(math.sqrt(2*0.5645*0.01*h - (0.01*h)**2 ))     )    +   ( 0.5645**2 * math.asin((-0.5645+(0.01*h))/0.5645    )        )                               )
            #resultado = math.sqrt(2*0.5645*0.01*h - (0.01*h)**2)
            # Mostrar el resultado
            self.result_label.text = f"Equivale a: {resultado:.4f} litros"

        except ValueError:
            # Mostrar un mensaje de error si no es un número válido
            self.result_label.text = "Por favor ingrese un número válido."


# Ejecutar la aplicación
if __name__ == '__main__':
    MedicionApp().run()
