from enum import Enum


class AnnouncementsGame(Enum):
    allTrumps = "All trumps"
    noTrumps = "No trumps"


class AnnouncementsCards(Enum):
    belote = "belote"
    tierce = "tierce"
    quarte = "quarte"
    quinte = "quinte"
    carre = "carre"
