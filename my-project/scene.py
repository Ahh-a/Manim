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
        self.wait(2)
        self.play(FadeOut(texto))

class capa(Scene):
    def construct(self):
        # Nome principal no centro
        nome_principal = Text("Caravaggio", color = BLACK).scale(4.5)
        nome_principal.move_to(ORIGIN)

        nome_autor = Text("Jacqueline Maria Barbosa Vitorette",  color = BLACK).scale(1.7)
        nome_autor.next_to(nome_principal, DOWN)

        data = Text("Goiânia, 24 de junho de 2025",  color = BLACK).scale(0.7)
        data.next_to(nome_autor, DOWN)

        self.play(
            Write(nome_principal, run_time= 2),
            Write(nome_autor, run_time =2)
        )
        self.wait(2)
        self.play(Write(data))
        self.wait(2)
        self.play(
            Unwrite(nome_principal, run_time=2),
            Unwrite(nome_autor, run_time =2),
            Unwrite(data, run_time = 2)
        )
        self.wait(1)


