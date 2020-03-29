from enum import Enum


class AnnouncementsGame(Enum):
    allTrumps = "All trumps"
    noTrumps = "No trumps"


class AnnouncementsCards(Enum):
    belote = 20
    tierce = 20
    quarte = 50
    quinte = 100
    carre_of_9s_ = 150
    carre_of_10_Q_K_A = 100
    carre_of_Js = 200

