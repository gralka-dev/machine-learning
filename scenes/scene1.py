from cv2 import transform
from manim import *

class S1(Scene):
    def construct(self):

        figure1 = SVGMobject(file_name="figure1.svg").set_color(BLACK).set_stroke(color=BLUE, width=5).scale(1.5).set_z_index(2)
        circle = Circle(radius=0.6).set_stroke(color=BLUE, width=10).set_fill(color=BLACK, opacity=0.8).set_z_index(1)

        timeline_line = Line(LEFT * 5, RIGHT * 5, color=YELLOW).set_stroke(width=4)
        up_line_1 = Line(UP * 0.1, DOWN * 0.1).set_stroke(color=YELLOW, width=4).next_to(timeline_line, LEFT - LEFT * 0.999)
        sub_1 = Text("3. Jahrhundert").set_color(WHITE).next_to(up_line_1, DOWN * 1).scale(0.5)

        up_line_2 = Line(UP * 0.1, DOWN * 0.1).set_stroke(color=YELLOW, width=4).next_to(timeline_line, RIGHT - RIGHT * 0.999)
        sub_2 = Text("6. Jahrhundert").set_color(WHITE).next_to(up_line_2, DOWN * 1).scale(0.5)

        timeline = VGroup(timeline_line, up_line_1, up_line_2, sub_1, sub_2)

        fcc_text = Text("Fidelity Chess Challenger")

        self.wait(1)
        self.play(Write(figure1), run_time=2)
        self.wait(2)
        self.play(
            #figure1.animate.shift(DOWN).scale(0.5),
            figure1.animate.scale(0.5).set_stroke(color=YELLOW),
            Write (circle),
            Write(timeline),
        )
        self.wait(2)
        self.play(
            Unwrite(timeline),
            Unwrite(circle),
        )
        self.wait()

        figure1_c1 = figure1.copy()
        figure1_c2 = figure1.copy()

        self.play(

            figure1.animate.set_stroke(color=WHITE).scale(1.2).shift(UP * 0.8),
            figure1_c1.animate.set_stroke(color=RED).scale(0.8).shift(UP * 0.8 + LEFT * 2).set_stroke(width=3),
            figure1_c2.animate.set_stroke(color=BLUE).scale(0.8).shift(UP * 0.8 + RIGHT * 2).set_stroke(width=3),

            FadeIn(fcc_text),
            fcc_text.animate.shift(DOWN * 1.2)
        )

        self.wait(5)

        self.play(

            figure1.animate.scale(0.8).shift(DOWN * 0.8),
            figure1_c1.animate.scale(0.2).shift(RIGHT * 2 + DOWN * 0.8).set_opacity(0),
            figure1_c2.animate.scale(0.2).shift(LEFT * 2 + DOWN * 0.8).set_opacity(0),

            fcc_text.animate.shift(UP * 1.2),
            FadeOut(fcc_text)
        )

        dots = VGroup()

        for i in range(0, 16):
            dots.add(Dot().scale(0.8))

        dots.arrange_in_grid(n_cols=4, buff=1)

        lines_vert = VGroup(
            Line(dots[0], dots[12]),
            Line(dots[1], dots[13]),
            Line(dots[2], dots[14]),
            Line(dots[3], dots[15])
        )

        lines_hor = VGroup(
            Line(dots[0], dots[3]),
            Line(dots[4], dots[7]),
            Line(dots[8], dots[11]),
            Line(dots[12], dots[15])
        )

        self.play(
            ReplacementTransform(figure1, dots),
        )

        self.play(
            Write(lines_vert, run_time=2, rate_func=rate_functions.ease_in_out_quad),
            Write(lines_hor, run_time=2, rate_func=rate_functions.ease_in_out_quad),
        )

        self.wait(2)
