from tkinter import CENTER
from manim import *

class S7(Scene):
    def construct(self):

        alexa = SVGMobject(file_name="alexa.svg")[0].set_color(WHITE).scale(0.3)
        google = SVGMobject(file_name="google.svg").scale(0.1).set_color(WHITE)
        apple = SVGMobject(file_name="apple.svg").set_color(WHITE).scale(0.3)

        dot = Dot(color=WHITE, radius=0.1).shift(DOWN * 3)

        self.play(
            FadeIn(google, run_time=2),
            google.animate.scale(4),
            FadeIn(apple, run_time=2),
            apple.animate.shift(LEFT * 4),
            FadeIn(alexa, run_time=2),
            alexa.animate.shift(RIGHT * 4),
        )

        self.wait(2)

        aldot = Dot(color=WHITE, radius=0).move_to(alexa).shift(DOWN * 0.8)
        aldot2 = Dot(color=WHITE, radius=0).move_to(alexa).shift(DOWN * 2)

        gdot = Dot(color=WHITE, radius=0).move_to(google).shift(DOWN * 1)
        gdot2 = Dot(color=WHITE, radius=0.1).move_to(google).shift(DOWN * 2)

        apdot = Dot(color=WHITE, radius=0).move_to(apple).shift(DOWN * 0.8)
        apdot2 = Dot(color=WHITE, radius=0).move_to(apple).shift(DOWN * 2)

        line1 = Line(aldot, aldot2).set_color(WHITE)
        line2 = Line(gdot, gdot2).set_color(WHITE)
        line3 = Line(apdot, apdot2).set_color(WHITE)
        line4 = Line(aldot2, gdot2).set_color(WHITE)
        line5 = Line(gdot2, dot).set_color(WHITE)
        line6 = Line(apdot2, gdot2).set_color(WHITE)

        dot2 = Dot(color=WHITE, radius=0.1).shift(DOWN * 6.5)
        line7 = Line(gdot2, dot2).set_color(WHITE)

        text = Text("Hey Siri, spiel \"It Runs Through Me\".").move_to(dot2.get_center() + DOWN * 1).scale(0.5)

        self.add(text)

        lines = VGroup(line1, line2, line3, line4, line5, line6, line7, gdot2)

        all1 = VGroup(apple, alexa, google, lines, text)

        self.play(
            FadeIn(gdot2),
            Write(lines, run_time=2),
            Write(line7),
            all1.animate.shift(UP * 7),
        )

        text2 = Text("Hier ist \"It Runs Through Me\" von Tom Misch.").move_to(text).scale(0.5).shift(DOWN * 0.8)

        text1_2 = VGroup(text, text2)

        self.play(
            Unwrite(line7, run_time=0.5),
            text.animate.set_opacity(0.5).scale(0.5),
            FadeIn(text2),
            text1_2.animate.shift(UP),
        )

        self.wait(2)

        self.play(
            FadeOut(text1_2, run_time=1, rate_func=rate_functions.ease_in_out_cubic),
        )

        self.wait()
