from manim import *

class S4(Scene):
    def construct(self):

        dots = VGroup()

        for i in range(0, 16):
            dots.add(Dot().scale(0.8))

        dots.arrange_in_grid(n_cols=4, buff=1)

        def get_location(chessboard, number):
            line = Line(chessboard[2][number + 1], chessboard[2][number + 4])
            dot = Dot().move_to(line.get_center())
            return dot.get_center()

        def label_vert_location(number):
            line = Line(dots[number], dots[number + 4]).get_center()
            return Dot().next_to(line, LEFT).get_center()

        def label_hor_location(number):
            line = Line(dots[number], dots[number + 1]).get_center()
            return Dot().next_to(line, DOWN).get_center()

        def place_piece(chessboard, piece, number):
            piece.shift(get_location(chessboard, number))
            return piece

        def move_piece(chessboard, piece, number):
            return piece.animate.move_to(get_location(chessboard, number))

        #def reset():
        #    place_piece(a1, 8),
        #    place_piece(b1, 9),
        #    place_piece(c1, 10),
        #    place_piece(a3, 0),
        #    place_piece(b3, 1),
        #    place_piece(c3, 2),

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

        labels_vert = VGroup(
        )

        labels_hor = VGroup(
        )

        self.add(dots, lines_vert, lines_hor)
        self.add(labels_vert, labels_hor)

        # Numbers for orientation

        #for i in range(0, 16):
        #    self.add(
        #        Text(str(i)).scale(0.4).move_to(dots[i]).set_color(YELLOW).set_z_index(5),
        #        Circle(radius=0.2).move_to(dots[i]).set_fill(color=BLACK, opacity=1).set_stroke(color=WHITE).set_z_index(2)
        #    )

        defender = Circle(radius=0.4).set_stroke(color=BLUE_C).set_fill(color="#071217", opacity=1)
        attacker = Circle(radius=0.4).set_stroke(color=RED_C).set_fill(color="#1b0b08", opacity=1)

        a1 = attacker.copy()
        b1 = attacker.copy()
        c1 = attacker.copy()

        a3 = defender.copy()
        b3 = defender.copy()
        c3 = defender.copy()

        attacker_group = VGroup(a1, b1, c1)
        defender_group = VGroup(a3, b3, c3)
        pieces = VGroup(attacker_group, defender_group).set_z_index(1)

        chessboard = VGroup(lines_vert, lines_hor, dots, labels_vert, labels_hor, pieces, dots)

        def reset(cb):
            place_piece(cb, cb[5][0][0], 8)
            place_piece(cb, cb[5][0][1], 9)
            place_piece(cb, cb[5][0][2], 10)
            place_piece(cb, cb[5][1][0], 0)
            place_piece(cb, cb[5][1][1], 1)
            place_piece(cb, cb[5][1][2], 2)

        self.add(chessboard)
        
        reset(chessboard)

        #self.play(
        #    Write(
        #        SurroundingRectangle(
        #            chessboard2[5][0][1]
        #        )
        #    ),
        #    Write(
        #        SurroundingRectangle(
        #            chessboard2[2][1]
        #        )
        #    )
        #)

        self.wait()

        self.play(
            chessboard.animate.scale(0.5).shift(UP * 2).set_stroke(width=2)
        )

        chessboard2 = chessboard.copy().shift(DOWN * 3 + LEFT * 2)
        chessboard3 = chessboard.copy().shift(DOWN * 3 + RIGHT * 2)

        line = Line(chessboard[1][3].get_center(), chessboard2[1][0].get_center()).set_stroke(width=2)
        line2 = Line(chessboard[1][3].get_center(), chessboard3[1][0].get_center()).set_stroke(width=2)

        lines_g1 = VGroup(line, line2)
        
        self.play(
            FadeIn(chessboard2),
            FadeIn(chessboard3),
            Write(lines_g1),
        )

        self.play(
            move_piece(chessboard2, chessboard2[5][0][0], 4),
            move_piece(chessboard3, chessboard3[5][0][1], 5),
        )

        chessboards_g1 = VGroup(chessboard, chessboard2, chessboard3, line, line2)

        self.play(
            chessboards_g1.animate.shift(UP).scale(0.5).set_stroke(width=2),
        )

        chessboard2_1 = chessboard2.copy().shift(DOWN * 2 + LEFT * 2)
        chessboard2_2 = chessboard2.copy().shift(DOWN * 2)

        chessboard3_1 = chessboard3.copy().shift(DOWN * 2)
        chessboard3_2 = chessboard3.copy().shift(DOWN * 2 + RIGHT * 2)

        line3 = Line(chessboard2[1][3].get_center(), chessboard2_1[1][0].get_center()).set_stroke(width=2)
        line4 = Line(chessboard2[1][3].get_center(), chessboard2_2[1][0].get_center()).set_stroke(width=2)

        line5 = Line(chessboard3[1][3].get_center(), chessboard3_1[1][0].get_center()).set_stroke(width=2)
        line6 = Line(chessboard3[1][3].get_center(), chessboard3_2[1][0].get_center()).set_stroke(width=2)

        lines_g2 = VGroup(line3, line4, line5, line6)
        chessboards_g2 = VGroup(chessboard2_1, chessboard2_2, chessboard3_1, chessboard3_2)

        self.play(
            FadeIn(chessboards_g2),
            Write(lines_g2),
        )

        self.play(
            move_piece(chessboard2_1, chessboard2_1[5][1][1], 4),
            move_piece(chessboard2_2, chessboard2_2[5][1][2], 6),

            move_piece(chessboard3_1, chessboard3_1[5][1][0], 4),
            move_piece(chessboard3_2, chessboard3_2[5][1][2], 6),
        )

        chessboards_g3 = VGroup(chessboards_g1, chessboards_g2, lines_g2)

        self.play(
            chessboards_g3.animate.shift(UP * 0.5).scale(0.8).set_stroke(width=1.5),
        )

        chessboard2_1_1 = chessboard2_1.copy().shift(DOWN * 1.5 + LEFT * 3)
        chessboard2_1_2 = chessboard2_1.copy().shift(DOWN * 1.5 + LEFT * 1.5)

        chessboard2_2_1 = chessboard2_2.copy().shift(DOWN * 1.5 + LEFT * 1.6)
        chessboard2_2_2 = chessboard2_2.copy().shift(DOWN * 1.5)

        chessboard3_1_1 = chessboard3_1.copy().shift(DOWN * 1.5)
        chessboard3_1_2 = chessboard3_1.copy().shift(DOWN * 1.5 + RIGHT * 1.6)

        chessboard3_2_1 = chessboard3_2.copy().shift(DOWN * 1.5 + RIGHT * 3)
        chessboard3_2_2 = chessboard3_2.copy().shift(DOWN * 1.5 + RIGHT * 1.5)

        chessboards_g4 = VGroup(chessboard2_1_1, chessboard2_1_2, chessboard2_2_1, chessboard2_2_2, chessboard3_1_1, chessboard3_1_2, chessboard3_2_1, chessboard3_2_2)

        line7 = Line(chessboard2_1[1][3].get_center(), chessboard2_1_1[1][0].get_center()).set_stroke(width=2)
        line8 = Line(chessboard2_1[1][3].get_center(), chessboard2_1_2[1][0].get_center()).set_stroke(width=2)

        line9 = Line(chessboard2_2[1][3].get_center(), chessboard2_2_1[1][0].get_center()).set_stroke(width=2)
        line10 = Line(chessboard2_2[1][3].get_center(), chessboard2_2_2[1][0].get_center()).set_stroke(width=2)

        line11 = Line(chessboard3_1[1][3].get_center(), chessboard3_1_1[1][0].get_center()).set_stroke(width=2)
        line12 = Line(chessboard3_1[1][3].get_center(), chessboard3_1_2[1][0].get_center()).set_stroke(width=2)

        line13 = Line(chessboard3_2[1][3].get_center(), chessboard3_2_1[1][0].get_center()).set_stroke(width=2)
        line14 = Line(chessboard3_2[1][3].get_center(), chessboard3_2_2[1][0].get_center()).set_stroke(width=2)

        lines_g3 = VGroup(line7, line8, line9, line10, line11, line12, line13, line14)

        self.play(
            FadeIn(chessboards_g4),
            Write(lines_g3),
        )

        chessboard2_1_1[5][0][1].set_z_index(2)
        chessboard2_2_2[5][0][0].set_z_index(2)
        chessboard3_1_1[5][0][1].set_z_index(2)
        chessboard3_2_1[5][0][1].set_z_index(2)

        self.play(
            move_piece(chessboard2_1_1, chessboard2_1_1[5][0][1], 4),
            move_piece(chessboard2_1_2, chessboard2_1_2[5][0][1], 5),

            move_piece(chessboard2_2_1, chessboard2_2_1[5][0][1], 5),
            move_piece(chessboard2_2_2, chessboard2_2_2[5][0][0], 1),

            move_piece(chessboard3_1_1, chessboard3_1_1[5][0][1], 2),
            move_piece(chessboard3_1_2, chessboard3_1_2[5][0][2], 6),

            move_piece(chessboard3_2_1, chessboard3_2_1[5][0][1], 0),
            move_piece(chessboard3_2_2, chessboard3_2_2[5][0][0], 4),
        )