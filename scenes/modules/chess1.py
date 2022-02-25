from cv2 import transform
from manim import *

class Test(Scene):
    def construct(self):

        figure1 = SVGMobject(file_name="figure1.svg").set_color(BLACK).set_stroke(color=BLUE, width=5).scale(1.5)

        timeline_line = Line(LEFT * 5, RIGHT * 5, color=YELLOW).set_stroke(width=3)
        up_line_1 = Line(UP * 0.1, DOWN * 0.1).set_stroke(color=YELLOW, width=3).next_to(timeline_line, LEFT - LEFT * 0.999)
        sub_1 = Text("3. Jahrhundert").set_color(WHITE).next_to(up_line_1, DOWN * 1).scale(0.5)

        up_line_2 = Line(UP * 0.1, DOWN * 0.1).set_stroke(color=YELLOW, width=3).next_to(timeline_line, RIGHT - RIGHT * 0.999)
        sub_2 = Text("6. Jahrhundert").set_color(WHITE).next_to(up_line_2, DOWN * 1).scale(0.5)

        timeline = VGroup(timeline_line, up_line_1, up_line_2, sub_1, sub_2)

        self.wait(1)
        self.play(Write(figure1), run_time=2)
        self.wait(2)
        self.play(
            #figure1.animate.shift(DOWN).scale(0.5),
            Transform(figure1, timeline)
        )
        self.wait(2)

        #self.add(timeline)
