from manim import *

# É importante definir essas configurações ANTES da sua classe Scene
# para que elas afetem a cena completa.
# Aumentando a largura do frame para 20 unidades (o padrão é 14).
# A altura será ajustada automaticamente para manter a proporção de aspecto.
config.frame_width = 20
# Se você quiser definir a altura explicitamente, pode fazer:
# config.frame_height = 12 # Exemplo: para uma proporção diferente ou específica

class Arthur(Scene):
    def construct(self):
        # O texto agora tem mais espaço para ser exibido.
        # Mantive o font_size original para mostrar que ele terá mais espaço.
        texto = Text("Arthur Molestador", font_size=96)

        # Centraliza o texto na cena.
        texto.center()

        self.play(Write(texto, run_time=2))
        self.wait(3)
        self.play(FadeOut(texto))
