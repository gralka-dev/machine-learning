from manim import *

class CheckerBoard(Scene):
    def construct(self):
        colour_scheme = [DARKER_GREY, WHITE]
        rects = VGroup()
        num_rects_row = 8
        num_rects_col = 8
        chess_pieces = {
            (0, 0) : "figure1.svg",
            (0, 1) : "figure1.svg",
            (0, 2) : "figure1.svg",
            (0, 3) : "figure1.svg",
            (0, 4) : "figure1.svg",
            (0, 5) : "figure1.svg",
            (0, 6) : "figure1.svg",
            (0, 7) : "figure1.svg",
            (1, 1) : "figure1.svg",
            (6, 1) : "figure1.svg",
            (7, 0) : "figure1.svg",
            (7, 1) : "figure1.svg",
            (7, 2) : "figure1.svg",
            (7, 3) : "figure1.svg",
            (7, 4) : "figure1.svg",
            (7, 5) : "figure1.svg",
            (7, 6) : "figure1.svg",
            (7, 7) : "figure1.svg",
        }

        for row in range(num_rects_row):
            for col in range(num_rects_col): 
                if row % 2 == 0:
                    r_color = colour_scheme[(col + 1) % len(colour_scheme)]
                else:
                    r_color = colour_scheme[col % len(colour_scheme)]

                address = (row, col)
                if row == 1:
                        address = (1, 1)
                elif row == 6:
                        address = (6, 1)
                if address in chess_pieces.keys():
                    rects.add(SVGMobject(chess_pieces[address]).set_stroke(color=BLUE, width=5))

                rect = Square(side_length=0.9, fill_color=r_color, color=r_color, fill_opacity=1)
                rects.add(rect)
        rects.arrange_in_grid(buff=0)
        self.add(rects)
        self.play(LaggedStart(*[DrawBorderThenFill(x, run_time=0.35) for x in rects], lag_ratio=0.05))