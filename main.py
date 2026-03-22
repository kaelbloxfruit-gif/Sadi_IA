from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
import requests
import re

# Configuración de colores estilo Hacker
Window.clearcolor = (0.05, 0.05, 0.05, 1)

class SadiApp(App):
    def build(self):
        self.title = "SADI - Sistema de Inteligencia & Ciberseguridad"
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Pantalla de Chat (Consola)
        self.chat_log = Label(
            text="[ SADI v1.0 ]\nSistemas listos. Esperando comando o IP...\n", 
            color=(0, 1, 0, 1), 
            size_hint_y=None, 
            halign='left', 
            valign='top',
            markup=True,
            font_size='14sp'
        )
        self.chat_log.bind(texture_size=self.chat_log.setter('size'))
        
        scroll = ScrollView(size_hint=(1, 0.8), bar_width=5)
        scroll.add_widget(self.chat_log)
        
        # Entrada de texto
        self.user_input = TextInput(
            hint_text="Escribe a SADI o una IP para rastrear...", 
            multiline=False, 
            size_hint=(1, 0.1),
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1),
            cursor_color=(0, 1, 0, 1)
        )
        self.user_input.bind(on_text_validate=self.procesar_entrada)
        
        # Botón de Ejecutar
        btn = Button(
            text="EJECUTAR", 
            size_hint=(1, 0.1),
            background_color=(0, 0.4, 0, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.procesar_entrada)
        
        layout.add_widget(scroll)
        layout.add_widget(self.user_input)
        layout.add_widget(btn)
        return layout

    def procesar_entrada(self, instance):
        texto = self.user_input.text.strip()
        if not texto:
            return

        self.chat_log.text += f"\n[USER]: {texto}"
        self.user_input.text = ""

        # Comprobar si es una dirección IP (Formato: num.num.num.num)
        es_ip = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", texto)

        if es_ip:
            self.rastrear_ip(texto)
        else:
            self.hablar_con_ia(texto)

    def rastrear_ip(self, ip):
        self.chat_log.text += f"\n[SADI]: Iniciando rastreo de satélite en {ip}..."
        try:
            r = requests.get(f"http://ip-api.com/json/{ip}").json()
            if r['status'] == 'success':
                lat, lon = r['lat'], r['lon']
                mapa = f"https://www.google.com/maps?q={lat},{lon}"
                
                reporte = (
                    f"\n[🛰️ REPORTE DE RASTREO]"
                    f"\n📍 IP: {r['query']}"
                    f"\n🌍 País: {r['country']}"
                    f"\n🏙️ Ciudad: {r['city']}"
                    f"\n🏢 ISP: {r['isp']}"
                    f"\n🌐 Coordenadas: {lat}, {lon}"
                    f"\n🗺️ Mapa: {mapa}\n"
                )
                self.chat_log.text += reporte
            else:
                self.chat_log.text += "\n[!] Error: IP no encontrada o privada.\n"
        except Exception as e:
            self.chat_log.text += f"\n[!] Error en el rastreo: {str(e)}\n"

    def hablar_con_ia(self, pregunta):
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            # Tu llave API de Groq
            headers = {"Authorization": "# En lugar de una sola línea, haz esto:
parte1 = "gsk_5HLttXCBX2Zy4qDGDijV"
parte2 = "WGdyb3FYdFosyXlqgJQxEY9YMRfJveJg"
headers = {"Authorization": f"Bearer {parte1}{parte2}"}
"}
            data = {
                "model": "llama-3.1-8b-instant",
                "messages": [{"role": "user", "content": pregunta}]
            }
            res = requests.post(url, headers=headers, json=data).json()
            respuesta = res['choices'][0]['message']['content']
            self.chat_log.text += f"\n[SADI]: {respuesta}\n"
        except Exception as e:
            self.chat_log.text += f"\n[!] ERROR DE IA: {str(e)}\n"

if __name__ == '__main__':
    SadiApp().run()
