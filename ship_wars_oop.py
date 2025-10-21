#!/usr/bin/env python
#  -*- coding: utf-8 -*-


class Game:
    def __init__(self, size: int):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Boat:
    def __init__(self, length: int, orientation: int, position: Coordinate):
        self.length = length
        self.orientation = orientation
        self.position = position


class Board:
    def __init__(self, game: Game):
        self.game = game
        N = self.game.size
        self.view = [[" " for _ in range(N + 1)] for _ in range(N + 1)]


    def show(self):
        for row in self.view:
            print(row)


    def add_boat(self, boat: Boat):
        if boat.orientation == 0:
            for x in range(boat.position.x, boat.length + boat.position.x):
                self.view[x][boat.position.y] = "X"
        else:
            for y in range(boat.position.y, boat.length + boat.position.y):
                self.view[boat.position.x][y] = "X"


if __name__ == '__main__':
    size = 9
    game = Game(size)

    view = Board(game)

    aircraft = Boat(5, 1, Coordinate(1,2))
    view.add_boat(aircraft)
    view.show()
