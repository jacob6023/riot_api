import json
import window
# Assuming the JSON data is stored in a file named "players.json"


with open("playerStats.json", "r") as file:
    data = json.load(file)

    # Accessing information about the first player
for i in range(len(data["players"])):

    first_player = data["players"][i]
    puuid = first_player["puuid"]
    game_name = first_player["gameName"]
    tag_line = first_player["tagLine"]

    # Printing the information
    print("PUUID:", puuid)
    print("Game Name:", game_name)
    print("Tag Line:", tag_line)

