import unittest
from classes.team import Team
from classes.player import Player


class TestTeam(unittest.TestCase):
    def test_when_create_team_then_all_fields_initialized_correctly(self):
        team = Team("Wolf")

        self.assertEqual(team.name, "Wolf")
        self.assertEqual(team.players, [])

    def test_when_add_two_members_to_team_return_correctly(self):
        member1 = Player("Pesho")
        member2 = Player("Gosho")
        team = Team("Wolf")

        team.add_team_members([member1, member2])

        self.assertEqual(len(team.players), 2)
        self.assertTrue(team.players.__contains__(member1))
        self.assertTrue(team.players.__contains__(member2))

    def test_when_add_member_from_wrong_type_return_exception(self):
        member = Player("Pesho")
        member_type_string = "Acer"
        team = Team("Wolf")

        with self.assertRaises(TypeError):
            team.add_team_members([member, member_type_string])

    def test_when_add_more_members_from_2_exception(self):
        member1 = Player("Pesho")
        member2 = Player("Gosho")
        member3 = Player("Thosho")
        team = Team("Wolf")

        with self.assertRaises(ValueError):
            team.add_team_members([member1, member2, member3])


if __name__ == '__main__':
    unittest.main()
