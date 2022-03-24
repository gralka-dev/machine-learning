from manim import *

class S3(Scene):
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
        
        reset(chessboard)

        chessboard.scale(0.8)

        self.wait()

        chessboard2 = chessboard.copy().shift(LEFT * 3).scale(0.8)
        chessboard3 = chessboard.copy().shift(RIGHT * 3).scale(0.8)

        chessboards_g1 = VGroup(chessboard2, chessboard3)
        
        self.play(
            FadeIn(chessboard),

            FadeIn(chessboards_g1),

            chessboard2.animate.scale(1.2).shift(LEFT),
            chessboard3.animate.scale(1.2).shift(RIGHT),
        )

        self.play(
            move_piece(chessboard, chessboard[5][0][2], 6),
            move_piece(chessboard2, chessboard2[5][0][0], 4),
            move_piece(chessboard3, chessboard3[5][0][1], 5),
        )

        self.wait()

        arrow1 = Arrow(chessboard3[5][1][0].get_center(), get_location(chessboard3, 5)).set_color(BLUE_C).set_z_index(5)
        arrow2 = Arrow(chessboard3[5][1][2].get_center(), get_location(chessboard3, 5)).set_color(BLUE_C).set_z_index(5)

        arrow3 = Arrow(chessboard2[5][1][1].get_center(), get_location(chessboard2, 4)).set_color(BLUE_C).set_z_index(5).set_opacity(0.5)
        arrow4 = Arrow(chessboard[5][1][1].get_center(), get_location(chessboard, 6)).set_color(BLUE_C).set_z_index(5).set_opacity(0.5)

        chessboard3_g = VGroup(chessboard3, arrow1, arrow2)
        chessboard2_g = VGroup(chessboard2, arrow3)
        chessboard_g = VGroup(chessboard, arrow4)

        self.play(
            FadeIn(arrow1),
            FadeIn(arrow2),
            FadeIn(arrow3),
            FadeIn(arrow4),
            chessboard2_g.animate.scale(0.8).set_opacity(0.5),
            chessboard_g.animate.scale(0.8).set_opacity(0.5),
            chessboard3.animate.scale(1.2),
        )
        
        arrows_g = VGroup(arrow1, arrow2, arrow3, arrow4)

        self.wait(3)

        self.play(
            FadeOut(arrow4),
            chessboard2_g.animate.scale(1.2).shift(RIGHT).set_opacity(0),
            chessboard3_g.animate.scale(0.8).shift(LEFT).set_opacity(0),
            chessboard.animate.scale(1.5625).set_opacity(1),
        )

        self.play(
            move_piece(chessboard, chessboard[5][0][2], 10),
        )

        self.remove(chessboard2_g, chessboard3_g)

        self.wait()