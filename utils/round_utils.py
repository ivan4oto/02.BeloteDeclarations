from enum import Enum


class AnnouncementsGame(Enum):
    allTrumps = "All trumps"
    noTrumps = "No trumps"
    clubs = "Clubs"
    diamonds = "Diamonds"
    hearts = "Hearts"
    spades = "Spades"


class AnnouncementsCards(Enum):
    belote = "belote"
    tierce = "tierce"
    quarte = "quarte"
    quinte = "quinte"
    carre_of_9s_ = "carre_of_9s_"
    carre_of_10_Q_K_A = "carre_of_10_Q_K_A"
    carre_of_Js = "carre_of_Js"



class AnnouncementsCardsValue(Enum):
    belote = 20
    tierce = 20
    quarte = 50
    quinte = 100
    carre_of_9s_ = 150
    carre_of_10_Q_K_A = 100
    carre_of_Js = 200
