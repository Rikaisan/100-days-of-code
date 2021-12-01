from turtle import Turtle


class Snake:
    def __init__(self, death_function, segments: int = 3, start_direction: int = 0 , color: str = 'black'):
        self.death_function = death_function
        self.initial_segments = segments
        self.head = Turtle()
        self.head.setpos(0, 0)
        self.head.shape('square')
        self.head.color(color)
        self.head.setheading(start_direction)
        self.head.penup()
        self._body = [self.head]
        for n in range(segments - 1):
            self.add_segment()

    def add_segment(self):
        part = self._body[-1].clone()
        self._body.append(part)

    def move(self):
        for idx, segment in enumerate(self._body[::-1]):
            if idx == len(self._body) - 1:
                self._body[0].forward(20)
            else:
                next_pos = self._body[::-1][idx + 1].pos()
                segment.setpos(next_pos)
        self.check_collision()

    def change_direction(self, angle: int):
        if (angle + 180) % 360 != self._body[0].heading():
            self._body[0].setheading(angle)

    def check_collision(self):
        for segment in self._body[1:]:
            if self.head.distance(segment) < 5:
                self.death_function()

    def pos(self):
        return self.head.pos()

    def body(self):
        return self._body

    def hide(self):
        for segment in self._body:
            segment.hideturtle()

    def __repr__(self):
        return f"Facing: {self.head.heading()}, Position: {self.head.pos()}, Length: {len(self._body)}"
