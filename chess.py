# -*- coding: utf-8 -*-
"""
chess
"""
# RNBQKBNR
# PPPPPPPP
# --------
# --------
# --------
# --------
# PPPPPPPP
# RNBQKBNR


from enum import Enum


class Color(Enum):
    WHITE = 1
    BLACK = 2


class Figure:
    def __init__(self, color: Color, letter: str, number: int):
        self.color = color
        self.current_letter = letter
        self.current_number = number

    def move(self, new_letter, new_number):
        if ord(new_letter) > ord('H') or ord(new_letter) < ord('A'):
            raise ValueError('Incorrect move. Letter is not in A..H')
        if new_number > 8 or new_number < 1:
            raise ValueError('Incorrect move. Number is not in 1..8')
        self.current_letter = new_letter
        self.current_number = new_number


class Pawn(Figure):
    def __init__(self, color, letter):
        if color == Color.WHITE:
            number = 2
        elif color == Color.BLACK:
            number = 7
        else:
            raise ValueError('Incorrect color')
        super().__init__(color, letter, number)

    def move(self, new_letter, new_number):
        if self.current_number in (2, 7):
            if self.color == Color.WHITE:
                if new_number in (3, 4):
                    self.current_number = new_number
                else:
                    raise ValueError('Incorrect move')
            if self.color == Color.BLACK:
                if new_number in (5, 6):
                    self.current_number = new_number
                else:
                    raise ValueError('Incorrect move')

    def chop_left(self):
        if self.color == Color.WHITE:
            self.current_number = self.current_number + 1
            self.current_letter = chr(ord(self.current_letter) - 1)
        if self.color == Color.BLACK:
            self.current_number = self.current_number - 1
            self.current_letter = chr(ord(self.current_letter) + 1)

    def chop_right(self):
        if self.color == Color.WHITE:
            self.current_number = self.current_number + 1
            self.current_letter = chr(ord(self.current_letter) + 1)
        if self.color == Color.BLACK:
            self.current_number = self.current_number - 1
            self.current_letter = chr(ord(self.current_letter) - 1)


    def change(self):
        if self.color == Color.WHITE and self.current_number == 8:
            pass
            # TODO: turn to other figure
        if self.color == Color.BLACK and self.current_number == 1:
            pass
            # TODO: turn to other figure


class Knight(Figure):
    def move(self, new_letter, new_number):
        horizontal_distance = ord(new_letter) - ord(self.current_letter)
        vertical_distance = new_number - self.current_number
        if horizontal_distance == 1 and vertical_distance == 2:
            super().move(new_letter, new_number)
        elif horizontal_distance == 2 and vertical_distance == 1:
            super().move(new_letter, new_number)
        else:
            raise ValueError(
                'Incorrect move. Number is not in 1..8 or letter ic not A..H'
            )


class Bishop(Figure):
    def move(self, new_letter, new_number):
        horizontal_distance = ord(new_letter) - ord(self.current_letter)
        vertical_distance = new_number - self.current_number
        if horizontal_distance == vertical_distance:
            super().move(new_letter, new_number)
        else:
            raise ValueError(
                'Incorrect move. Number is not in 1..8 or letter ic not A..H'
            )


class Rook(Figure):
    def move(self, new_letter, new_number):
        horison_distance = ord(new_letter) - ord(self.current_letter)
        verical_distance = new_number - self.current_number
        if horison_distance == verical_distance:
            super().move(new_letter, new_number)
        else:
            raise ValueError(
                'Incorrect move. Number is not in 1..8 or letter ic not A..H'
            )


class Queen(Figure):
    def move(self, new_letter, new_number):
        pass


class King(Figure):
    def move(self, new_letter, new_number):
        horizontal_distance = ord(new_letter) - ord(self.current_letter)
        vertical_distance = new_number - self.current_number
        if ...:
            pass


pawn1 = Pawn(Color.WHITE, 'A')
pawn2 = Pawn(Color.WHITE, 'B')
pawn1.move('A', 4)
pawn2.move('B', 3)
