from manim import *

class CheckerBoard(Scene):
    def construct(self):
        config.background_color=BLACK
        colour_scheme = [DARKER_GREY, WHITE]
        rects = VGroup()
        num_rects_row = 3
        num_rects_col = 3

        for row in range(num_rects_row):
            for col in range(num_rects_col): 
                if row % 2 == 0:
                    r_color = colour_scheme[(col + 1) % len(colour_scheme)]
                else:
                    r_color = colour_scheme[col % len(colour_scheme)]

                rect = Square(side_length=0.9, fill_color=r_color, color=r_color, fill_opacity=1)

                if row < 2 or row > 5:
                    if row == 0 and col % 2 == 1:
                        rect.add((Circle().set_stroke(color=BLACK, width=10)).scale(0.2))
                    elif row == 1 and col % 2 == 0:
                        rect.add((Circle().set_stroke(color=BLACK, width=10)).scale(0.2))
                    elif row == 6 and col % 2 == 1:
                        rect.add((Circle().set_stroke(color=WHITE, width=10)).scale(0.2))
                    elif row == 7 and col % 2 == 0:
                        rect.add((Circle().set_stroke(color=WHITE, width=10)).scale(0.2))

                rects.add(rect)
        rects.arrange_in_grid(buff=0)
        self.add(rects)
        self.play(LaggedStart(*[DrawBorderThenFill(x, run_time=0.35) for x in rects], lag_ratio=0.05))