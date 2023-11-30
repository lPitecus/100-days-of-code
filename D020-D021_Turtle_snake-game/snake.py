from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.squares = []
        self.pos = 0
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        """Creates the inicial snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        """Updates the snakes position in the screen"""
        # após a cabeça realizar um movimento, atualiza as posições dos quadrados restantes com base no movimento feito.
        for sqr_num in range(len(self.squares) - 1, 0, -1):  # o range começa na caudada cobra
            # (quadrado na posição len(squares)) e para na cabeça.
            # O quadrado selecionado irá ocupar a posição do quadrado da frente.
            new_x = self.squares[sqr_num - 1].xcor()
            new_y = self.squares[sqr_num - 1].ycor()
            # Coloca o quadrado selecionado na posição do quadrado da frente.
            self.squares[sqr_num].goto(x=new_x, y=new_y)
            # Exemplo: a cauda está selecionada.
            # A posição da cauda ficará na posição do quadrado após a cauda.
            # Coloca a cauda na nova posição.
            # Volta ao início do for loop
            # o quadrado após a cauda está selecionado.
            # A posição do quadrado após a cauda ficará na posição da cabeça
            # coloca o quadrado após a cauda na nova posição
        # quando o for loop terminar de atualizar as posições dos quadrados, a cobra faz um novo movimento para a
        # cabeça se mexer.
        self.squares[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
