import os

from models.player import Player
from models.coordinates import Coordinates
from models.grid import Grid


class Engine:

    def __init__(self):
        self.is_running = True
        self._player1 = None
        self._player2 = None
        self._player_turn = True

    def start(self):
        # Nom des deux joueurs
        self.ask_name()
        self.render()

    def ask_name(self):
        name1 = input("Nom du premier joueur : ")
        name2 = input("Nom du deuxième joueur : ")

        self._player1 = Player(name1)
        self._player2 = Player(name2)

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self._player1.show_grid("left")
        self._player2.show_grid("right")

    def turn(self):
        self.render()
        current_player = self._player1 if self._player_turn == True else self._player2
        other_player = self._player1 if self._player_turn == False else self._player2

        error = True
        while error:
            # On demande la cible
            target = self._ask_target()

            # on regarde si on ne l'a pas déjà fait

            if current_player.validate_target(target.x, target.y):
                error = False
            else:
                print("Tir déjà éffectué")


        # on tire sur l'autre joueur
        status = other_player.get_shot(x,y)

        # Si tous les bateau du joueur adverse sont détruits, le joueur courant est vainqueur

        # on change de joueur
        self._player_turn = not self._player_turn

    def _ask_target(self):
        lettres = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'F', 'I', 'J']

        name = self._player1.name if self._player_turn == 1 else self._player2.name
        x = input("{} : choisir la lettre ".format(name)).upper()
        y = input("{} : choisir le chiffre ".format(name))

        return Coordinates(lettres.index(x), int(y)-1)
