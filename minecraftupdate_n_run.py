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

filelist = subprocess.check_output("ls", universal_newlines=True) #does a search of the directory
filelist = filelist.split() #splits the string and makes it a list, easier to search


listo = toget.split("/")
end = len(listo)
thefile = listo[end-1]

#only gets the new version of the server if you dont already have it
if thefile not in filelist:
        subprocess.call(["wget", "-q", toget])

subprocess.call(["nohup java -Xms1G -Xmx1G -jar {} nogui &".format(thefile)],shell=True)
#runs the server with nohangup and in the background so you can start it remotely

exit()
