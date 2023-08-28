from modules.team import *

players = ["Derice Bannock", "Sanka Coffie", "Junior Bevil", "Yul Brenner"]
team = Team("Cool Runnings", players, "Irv Blitzer")

# print(team.has_player("Junior Bevil"))  # True
# print(team.has_player("Usain Bolt"))  # False
# # print(team.has_player("Derice Bannock"))
# # print(team.has_player("Sanka Coffie"))


# # team.add_player("Roger")
# # print(players)
# # print(team.has_player("Roger"))  # True

team.play_game(True)
print(team.points)  # 3

team.play_game(False)
print(team.points)  # 3
