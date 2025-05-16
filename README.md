# 🤖 Chatbot Básico con Flet, OpenAI y OpenWeatherMap

Una aplicación de **chatbot interactivo con interfaz gráfica**, desarrollada en Python usando [Flet](https://flet.dev/). Permite mantener una conversación con inteligencia artificial o consultar el clima de cualquier ciudad en tiempo real.

---

## 🚀 Funcionalidades

✨ Dos modos disponibles:

- 🧠 **Chat con IA**: responde preguntas utilizando la API de OpenAI (`gpt-4o-mini`).
- 🌦️ **Clima actual**: consulta temperatura y descripción del clima usando OpenWeatherMap.

🎨 Interfaz moderna con:

- Modo oscuro integrado.
- Diseño adaptado para escritorio.
- Interacciones en tiempo real.

---

## 🔧 Requisitos

🔑 Necesitas dos claves API:

- `OPENAI_API_KEY` – Para usar el modelo de lenguaje de OpenAI.
- `OPENWEATHER_API_KEY` – Para obtener datos meteorológicos.

📦 Librerías utilizadas:

- `flet`
- `openai`
- `requests`
- `python-dotenv`

---

## 💡 Notas

- El modelo usado de OpenAI es **`gpt-4o-mini`**, lo cual requiere cuenta con acceso premium.
- Las respuestas del clima están en **español** y los valores de temperatura en **°C**.
