from manim import *

class S3g2(Scene):
    def construct(self):

        dots = VGroup()

        for i in range(0, 16):
            dots.add(Dot().scale(0.8))

        dots.arrange_in_grid(n_cols=4, buff=1)

        def get_location(number):
            line = Line(dots[number + 1], dots[number + 4])
            dot = Dot().move_to(line.get_center())
            return dot.get_center()

        def label_vert_location(number):
            line = Line(dots[number], dots[number + 4]).get_center()
            return Dot().next_to(line, LEFT).get_center()

        def label_hor_location(number):
            line = Line(dots[number], dots[number + 1]).get_center()
            return Dot().next_to(line, DOWN).get_center()

        def place_piece(piece, number):
            piece.shift(get_location(number))
            return piece

        def move_piece(piece, number):
            return piece.animate.move_to(get_location(number))

        def reset():
            place_piece(a1, 8),
            place_piece(b1, 9),
            place_piece(c1, 10),
            place_piece(a3, 0),
            place_piece(b3, 1),
            place_piece(c3, 2),

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
            Text("1").move_to(label_vert_location(8)).scale(0.5),
            Text("2").move_to(label_vert_location(4)).scale(0.5),
            Text("3").move_to(label_vert_location(0)).scale(0.5),
        )

        labels_hor = VGroup(
            Text("A").move_to(label_hor_location(12)).scale(0.5),
            Text("B").move_to(label_hor_location(13)).scale(0.5),
            Text("C").move_to(label_hor_location(14)).scale(0.5),
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

        self.add(chessboard, pieces)
        reset()

        self.play(
            move_piece(a1, 4),
        )

        self.play(
            move_piece(c3, 6),
        )

        self.play(
            move_piece(b1, 5),
        )

        self.play(
            move_piece(a1, 8),
            move_piece(b1, 9),
            move_piece(c1, 10),
            move_piece(a3, 0),
            move_piece(b3, 1),
            move_piece(c3, 2),
        )
