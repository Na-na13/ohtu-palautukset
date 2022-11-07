import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89) 
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_onko_pelaajaa_pelaajalistassa(self):
        self.assertEqual(self.statistics.search("Kurri").name, "Kurri")
        self.assertEqual(self.statistics.search("Selänne"), None)

    def test_joukkueen_pelaajat(self):
        edmonton = self.statistics.team("EDM")
        rangers = self.statistics.team("NYR")

        self.assertGreater(len(edmonton), 0)
        self.assertEqual(len(rangers), 0)

    def test_top_3_pisteet(self):
        top_3_list = self.statistics.top(2,SortBy.POINTS)
        names = []
        for player in top_3_list:
            names.append(player.name)
        self.assertEqual(names, ["Gretzky","Lemieux","Yzerman"])

    def test_top_3_maalit(self):
        top_3_list = self.statistics.top(2,SortBy.GOALS)
        names = []
        for player in top_3_list:
            names.append(player.name)
        self.assertEqual(names, ["Lemieux","Yzerman","Kurri"])

    def test_top_3_syotot(self):
        top_3_list = self.statistics.top(2,SortBy.ASSISTS)
        names = []
        for player in top_3_list:
            names.append(player.name)
        self.assertEqual(names, ["Gretzky","Yzerman","Lemieux"])

    def test_top_pisteet_lista_sama_ilman_toista_parametria(self):
        list_with_enum = self.statistics.top(2,SortBy.POINTS)
        list_without_enum = self.statistics.top(2)

        names = []
        for player in list_with_enum:
            names.append(player.name)
        second_names = []
        for player in list_without_enum:
            second_names.append(player.name)
        self.assertEqual(names, ["Gretzky","Lemieux","Yzerman"])
        self.assertEqual(second_names, ["Gretzky","Lemieux","Yzerman"])
