#!/usr/bin/python3.4
import json
import requests
import subprocess

THEJSON = "https://launchermeta.mojang.com/mc/game/version_manifest.json" #JSON from mojang to determine most recent version

r = requests.get(THEJSON)  #gets THEJSON

parsed_json = r.json() 
thelatest = parsed_json["latest"]
currentver = thelatest["release"]

toget = "https://s3.amazonaws.com/Minecraft.Download/versions/" + currentver + "/minecraft_server." + currentver + ".jar"
#this is the .jar file with the latest version

subprocess.call(["wget", "-q", toget]) #grabs the latest .jar

listo = toget.split("/")
end = len(listo)
thefile = listo[end-1]

subprocess.call(["nohup java -Xms1G -Xmx1G -jar {} nogui &".format(thefile)],shell=True)
#runs the server with nohangup and in the background so you can start it remotely

exit()
