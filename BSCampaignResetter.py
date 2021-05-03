import json

data = ""

missionIds = ["1", "2a", "2b", "3", "4a", "4b", "5a", "5b", "6a", "6b", "7a", "7b", "8a", "8b", "9a", "9b", "10", "11",
              "12a", "12b", "12c", "13a", "13b", "14a", "14b", "15", "16a", "16b", "17a", "17b", "18", "19a", "19b",
              "20a", "20b", "21", "22a", "22b", "23a", "23b", "24a", "24b", "24c", "25", "26", "27", "28a", "28b", "29",
              "30", "31"]

with open("PlayerData.dat") as json_file:
    data = json.load(json_file)
    for i in data["localPlayers"][0]["missionsStatsData"]:
        for j in missionIds:
            if i["missionId"] == j:
                i["cleared"] = False

with open("PlayerData.dat", "w") as out:
    json.dump(data, out)
