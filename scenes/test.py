from manim import *

class Test(Scene):
    def construct(self):
        circle = Circle()
        self.play(Write(circle), run_time=5)
        self.wait(2)