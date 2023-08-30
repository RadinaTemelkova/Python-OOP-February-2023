from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player.name} is already in the guild."
        elif player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        else:
            self.players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        for current_player in self.players:
            if current_player.name == player_name:
                current_player.guild = "Unaffiliated"
                self.players.remove(current_player)
                return f"Player {player_name} has been removed from the guild."

        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        players_info = '\n'.join(current_player.player_info() for current_player in self.players)
        return f"Guild: {self.name}\n{players_info}\n"


player = Player("George", 50, 100)
player_2 = Player("Mike", 60, 120)
print(player.add_skill("Shield Break", 20))
print(player_2.add_skill("Repair Armour", 30))
print(player.player_info())
print(player_2.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.assign_player(player_2))
print(guild.kick_player("Mike"))
print(guild.guild_info())
