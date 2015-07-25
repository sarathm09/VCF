import os
import shutil
import subprocess
import time
from zipfile import ZipFile


def connect():
    # if not os.path.exists("android/"):
    with ZipFile('data.zip') as zf:
        zf.extractall(pwd='rset123')
    inst = subprocess.Popen("android\\adb2 install android\\app.apk", shell=True)
    inst.wait()
    subprocess.Popen("android\\adb2 shell am start -W -n t90.vcfandroid/.MainActivity", shell=True)
    subprocess.Popen("android\\adb2 logcat -c", shell=True)

    p = subprocess.Popen('android\\adb2 logcat -s "VCFSTATUS"', shell=True, stdout=subprocess.PIPE)
    lines_iterator = iter(p.stdout.readline, b"")

    filepath = ""
    for line in lines_iterator:
        print line
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

    subprocess.Popen("android\\adb2 pull \"/storage/emulated/legacy/WhatsApp/Profile Pictures/\" pics/", shell=True)

    pull = subprocess.Popen("android\\adb2 pull " + filepath, shell=True)
    pull.wait()
    uninstall = subprocess.Popen("android\\adb2 uninstall t90.vcfandroid", shell=True)
    uninstall.wait()
    ki = subprocess.Popen("taskkill -f -im adb2.exe", shell=True)
    ki.wait()
    time.sleep(2)
    files = os.listdir(".")
    for i in os.listdir("android/"):
        os.remove("android/" + i)
    for i in files:
        if i.endswith(".vcf"):
            return i
    return ""


if __name__ == '__main__':
    print "dsfg: " + connect()