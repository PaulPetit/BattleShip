from models import utils
from models.coordinates import Coordinates
from models.ship import Ship
import random


class Grid:

    def __init__(self):
        self.shipList = []
        self._set_ships()

    def print(self, position):

        if position == "right":
            utils.setCursorPos(30, 2)
        print("    A B C D E F G H I J")

        for y in range(10):
            if position == "right":
                utils.setCursorPos(30, y + 3)
            if y != 9:
                print("{}  ".format(y + 1), end="")
            else:
                print("{} ".format(y + 1), end="")
            for x in range(10):
                print("|{}".format(self.get_caracter(x, y)), end="")

            print("|")

    def _set_ships(self):
        # on crée tous les bateau
        # en vérifiant si ils ne se croisent pas

        # Porte avion 5 cellules

        ships_to_create = [5, 4, 3, 3, 2]  # les cell_num

        for ship in ships_to_create:
            error = True
            while error:
                origine = Coordinates(random.randrange(0, 9), random.randrange(0, 9))
                direction = random.randrange(1, 4)
                if self._validate_ship(origine, direction, ship):
                    self.shipList.append(Ship(origine, direction, ship))
                    error = False

    def _validate_ship(self, origine, direction, cell_num):
        if direction == 1:
            x_offset = 1
            y_offset = 0
        elif direction == 2:
            x_offset = 0
            y_offset = 1
        elif direction == 3:
            x_offset = -1
            y_offset = 0
        elif direction == 4:
            x_offset = 0
            y_offset = -1

        for coord in range(cell_num):
            # on vérifie si on reste dans le grille
            if origine.x + (x_offset * coord) < 0 or origine.x + (x_offset * coord) > 9 or origine.y + (
                    y_offset * coord) < 0 or origine.y + (y_offset * coord) > 9:
                # pas bon
                return False
            # on vérifie si on croise un bateau
            if self._contains_ship(origine.x + (x_offset * coord), origine.y + (y_offset * coord)):
                # pas bon
                return False

            # on vérifie si on est collé à un bateau
            if self._next_to_ship(origine.x + (x_offset * coord), origine.y + (y_offset * coord)):
                return False
        return True

    def _contains_ship(self, x, y):
        for ship in self.shipList:
            if ship.has_position(x, y):
                return True
        return False

    def get_caracter(self, x, y):
        if self._contains_ship(x, y):
            return self._get_ship_caracter(x, y)
        else:
            return "■"

    def _get_ship_caracter(self, x, y):
        for ship in self.shipList:
            if ship.has_position(x, y):
                return ship.displayCaracter

    def _next_to_ship(self, x, y):
        # chek droite
        if self._contains_ship(x + 1, y):
            return True
        if self._contains_ship(x, y + 1):
            return True
        if self._contains_ship(x - 1, y):
            return True
        if self._contains_ship(x, y - 1):
            return True

        return False
