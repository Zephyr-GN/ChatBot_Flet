import flet 
from flet import Page, TextField, ElevatedButton, Column, Text, Colors, Container, alignment, Dropdown, dropdown
from openai import OpenAI
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
WEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city):
    """Obtener información del clima de una ciudad, nombre de la ciudad con la descripción del clima o error usando OpenWeather API"""
    try:
        # URL para la consulta del clima
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=es"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            # Extraer temperatura y descripción del clima
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"El clima en {city}: {description}, temperatura: {temp}°C"
        else:
            # Manejo de error si la ciudad no es encontrada o error en la consulta
            return f"Error al obtener el clima: {data.get('message', 'Ciudad no encontrada')}"
    except Exception as e:
        return f"Error al consultar el clima: {str(e)}"

def get_ai_response(prompt):
    """Función para obtener respuesta de OpenAI"""
    try:
        # Crear la solicitud de completado de chat a OpenAI usando el cliente, tener encuenta que esta seccion se tiene que tener la  version primium de chatgpt!!!!!
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Eres un asistente amigable y útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error al consultar a OpenAI: {str(e)}"

def main(page: Page):
    """Configura la interfaz gráfica y la lógica de la app con Flet"""
    # Configuración básica de la ventana y tema
    page.title = "ChatBot Prueba de Clima y ChatGPT"
    page.bgcolor = Colors.BLUE_GREY_900
    page.theme_mode = "dark"
    page.window_width = 800
    page.window_height = 600

    # Campo de texto para ingresar mensajes
    input_box = TextField(
        label="Escriba su mensaje",
        border_color=Colors.BLUE_200,
        focused_border_color=Colors.BLUE_400,
        text_style=flet.TextStyle(color=Colors.WHITE),
        expand=True
    )

    # Menú desplegable para seleccionar modo: chat con IA o consulta de clima
    mode_dropdown = Dropdown(
        options=[
            dropdown.Option("chat", "Chat con IA"),
            dropdown.Option("weather", "Consultar clima")
        ],
        value="chat", 
        label="Modo",
        border_color=Colors.BLUE_200,
        color=Colors.WHITE
    )

    chat_area = Column(scroll='auto', expand=True)

    def send_message(e):
        """Función que se ejecuta al presionar el botón enviar"""
        user_message = input_box.value
        if not user_message:
            return

        # Mostrar mensaje del usuario en la pantalla
        chat_area.controls.append(Text(f"Usuario: {user_message}", color=Colors.WHITE))

        # Determinar qué función usar según el modo seleccionado
        if mode_dropdown.value == "weather":
            response = get_weather(user_message)
        else:
            response = get_ai_response(user_message)

        # Mostrar respuesta del chatbot o clima
        chat_area.controls.append(Text(f"ChatBot: {response}", color=Colors.BLUE_200))

        # Limpiar el campo de texto y actualizar la interfaz
        input_box.value = ""
        page.update()

    # Botón para enviar mensaje
    send_button = ElevatedButton(
        text="Enviar",
        on_click=send_message,
        bgcolor=Colors.BLUE_700,
        color=Colors.WHITE
    )

    # Contenedor para los mensajes del chat
    chat_container = Container(
        content=chat_area,
        bgcolor=Colors.BLUE_GREY_800,
        padding=10,
        border_radius=10,
        expand=True
    )

    # Contenedor para el input, modo y botón en una fila
    input_container = Container(
        content=flet.Row(
            controls=[mode_dropdown, input_box, send_button],
            spacing=10
        )
    )

    # Agregar contenedores a la página
    page.add(chat_container, input_container)

# Iniciar la aplicación Flet
if __name__ == "__main__":
    flet.app(target=main)
