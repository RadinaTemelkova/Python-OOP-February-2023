from project.player import Player
from project.team import Team


player_1 = Player("John", 2, 4, 6, 8)

print("Player name:", player_1.name)
print("Points sprint:", player_1._Player__sprint)
print("Points dribble:", player_1._Player__dribble)
print("Points passing:", player_1._Player__passing)
print("Points shooting:", player_1._Player__shooting)

print("\ncalling the __str__ method")
print(player_1)

print("\nAbout the team")
team_1 = Team("Winning Team", 10)
print("Team name:", team_1._Team__name)
print("Teams points:", team_1._Team__rating)
print("Teams players:", len(team_1._Team__players))
print(team_1.add_player(player_1))
print(team_1.add_player(player_1))
print("Teams players:", len(team_1._Team__players))
print(team_1.remove_player("John"))
print(team_1.remove_player("John"))
