import os
import shutil
import subprocess
import time

try:
    os.remove("app.apk")
except:
    pass
shutil.copy("..\\VCFandroid\\app\\build\\outputs\\apk\\app-debug.apk", "app.apk")
inst = subprocess.Popen("adb2 install app.apk", shell=True)
inst.wait()
subprocess.Popen("adb2 shell am start -W -n t90.vcfandroid/.MainActivity", shell=True)
subprocess.Popen("adb2 logcat -c", shell=True)

p = subprocess.Popen('adb2 logcat -s "VCFSTATUS"', shell=True, stdout=subprocess.PIPE)
lines_iterator = iter(p.stdout.readline, b"")

filepath = ""
for line in lines_iterator:
    if "success" in line:
        filepath = line.split(",")[-1].replace("/0/", "/legacy/")
        break

files = os.listdir(".")
for i in files:
    if i.endswith(".vcf"):
        try:
            os.mkdir("bkp")
        except:
            pass
        shutil.move(i, "bkp/" + str(int(time.time() * 1000)) + "__" + i)

pull = subprocess.Popen("adb2 pull " + filepath, shell=True)
pull.wait()
subprocess.Popen("adb2 uninstall t90.vcfandroid", shell=True)
