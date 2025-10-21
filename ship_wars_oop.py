#!/usr/bin/env python
#  -*- coding: utf-8 -*-

def is_valid_integer(int_str):
    """Retourne True si int_str représente un nombre entier valide :
    supprime les éventuels espaces en début et fin de chaîne → cleaned_int_str
    détermine l'indice de départ dans cleaned_int_str du nombre entier
    en admettant qu'un signe puisse être présent en premier caractère,
    immédiatement suivi par la valeur absolue du nombre
    """
    cleaned_int_str = int_str.strip()
    int_index = 1 if cleaned_int_str[0] in ('-', '+') else 0
    return cleaned_int_str[int_index:].isdigit()


class Game:
    def __init__(self, size: int):
        self.size = size
        self.board = [["~" for _ in range(size)] for _ in range(size)]


class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Boat:
    def __init__(self, length: int, orientation: int, x: int, y: int):
        self.length = length
        self.orientation = orientation
        self.position = Coordinates(x, y)


class Board:
    def __init__(self, game: Game):
        self.game = game
        N = self.game.size
        self.view = [["~" for _ in range(N + 1)] for _ in range(N + 1)]
        self.boats = []  # type: ignore


    def show(self):
        # Add column labels
        print("  " + " ".join(chr(65 + i) for i in range(self.game.size)))
        for i, row in enumerate(self.view):
            if i < self.game.size:
                # Add row labels
                print(chr(65 + i) + " " + " ".join(row[1:]))


    def add_boat(self, boat: Boat):
        if boat.orientation == 0:  # Horizontal
            for x in range(boat.position.x, boat.position.x + boat.length):
                if x < self.game.size:
                    self.view[x][boat.position.y] = "X"
            self.boats.append(boat)
        else:  # Vertical
            for y in range(boat.position.y, boat.position.y + boat.length):
                if y < self.game.size:
                    self.view[boat.position.x][y] = "X"
            self.boats.append(boat)


    def add_fleet(self, boats):
        for boat in boats:
            self.add_boat(boat)


    def shoot(self, x: int, y: int):
        if 0 <= x < self.game.size and 0 <= y < self.game.size:
            if self.view[x][y] == "X":
                self.view[x][y] = "H"  # Hit
                print(f"Hit at ({x}, {y})!")
            else:
                self.view[x][y] = "M"  # Miss
                print(f"Miss at ({x}, {y})!")
        else:
            print("Invalid coordinates!")

def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if is_valid_integer(user_input):
            return int(user_input)
        else:
            print("Invalid input. Please enter a valid integer.")


if __name__ == '__main__':
    size = 9
    game = Game(size)

    view = Board(game)

    aircraft = Boat(5, 0, 2, 2)
    cruiser = Boat(4, 1, 1, 4)
    destroyer = Boat(3, 1, 3, 5)
    submarine = Boat(3, 0, 8, 5)
    torpedo = Boat(2, 0, 5, 9)
    view.add_fleet([aircraft, cruiser, destroyer, submarine, torpedo])
    view.show()

    # Example of shooting with user input
    x = get_user_input("Enter x coordinate: ")
    y = get_user_input("Enter y coordinate: ")
    view.shoot(x, y)
    view.show()