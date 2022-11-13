import json
import os
from json import JSONDecodeError

commandsJsonLocation = "resources/command.json"

def isSongValid(data):
    code = data["status"]["code"]
    if code == 0:
        return True
    else:
        return False

def executeTheSong(data):
    code = data["status"]["code"]

    if code == 0:
        title = data["metadata"]["music"][0]["title"]
        album_name = data["metadata"]["music"][0]["album"]["name"]
        dataFile = open(commandsJsonLocation)
        try:
            commandData = json.load(dataFile)
        except JSONDecodeError:
            commandData = json.load(json.dump(dataFile))
        dataFile.close()

        for command in commandData:
            if command["title"] == title:
                os.system(command["command"])
                print("It's "+title+"!")
                print(command["comment"])
                return

def addSongCommand(data,command,comment):
    code = data["status"]["code"]

    if code == 0:
        title = data["metadata"]["music"][0]["title"]
        album_name = data["metadata"]["music"][0]["album"]["name"]
        dataFile = open(commandsJsonLocation)
        commandData = json.load(dataFile)
        newCommand = {"title": title,"album-name": album_name,"command":command,"comment":comment}
        commandData.append(newCommand);
        dataFile.close()
        commandDataString = json.dumps(commandData)
        newCommandFile = open(commandsJsonLocation,"w")
        newCommandFile.write(commandDataString)
        newCommandFile.close()
