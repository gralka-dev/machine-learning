from manim import *

class table(Scene):
  def construct(self):
    chess = Table(
      [['•','•'],['•','•']],
      include_outer_lines=True)
    for i in range(2):
      for j in range(2):
        chess.add_highlighted_cell((i,j), color=None)
    self.add(chess)