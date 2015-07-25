import base64
import copy
import os
import re
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


class vcfManager:
    vcfdata = ""
    vcfs = []
    upperTxts = ["rset", "kv", "kve", "sap", "cs", "cse", "s1s2"]
    users = []
    user_data = {
        "name": "",
        "phone": [],
        "email": [],
        "url": [],
        "photo": [],
        "dob": [],
        "addr": "",
    }
    knwn = ["BEGIN", "PHOTO", "TEL", "FN", "VERSION",
            "END", "URL", "EMAIL", "BDAY", "X-STARRED",
            "X-NICKNAME", "NOTE", "X-TIMES_CONTACTED",
            "X-LAST_TIME_CONTACTED", "ADR"]

    def __init__(self):
        pass

    def fb(self, data):
        # Extract images from FB
        if data['name'] != "" and len(data['email']) != 0:
            for u in data['email']:
                try:
                    te = "https://www.facebook.com/public?query=" + u
                    x = urllib2.urlopen(te).read()
                    fid = re.findall("[0-9]+_([0-9]+)_[0-9]+", x)
                    if len(fid) > 0:
                        data['url'].append("https://www.facebook.com/" + fid[0])
                        bs = BeautifulSoup(urllib2.urlopen("https://www.facebook.com/photo.php?fbid=" + fid[0]).read())
                        pUrl = bs.find("img", {"id": "fbPhotoImage"})['src']
                        urllib.urlretrieve(pUrl, "pics/" + data['name'] + ".jpg")
                except:
                    print "Error: " + data['name']
        return data

    def parseVCF(self, file):
        self.vcfdata = file.read()
        self.vcfs = self.vcfdata.split("END:VCARD")
        for vcf in self.vcfs:
            data = copy.deepcopy(self.user_data)

            # Extract name

            raw_name, name = re.findall("^FN:([^\n]*)\n", vcf, re.MULTILINE), ""
            if len(raw_name) == 1:
                name = self.verifyName(raw_name[0])
            if name == "":
                # print "Error: [No Name] : \n" + vcf
                pass
            else:
                data['name'] = name

            # Extract Phone
            raw_phone = re.findall("^TEL;([\+:a-zA-Z 0-9;-]*)\n", vcf, re.MULTILINE)
            # Loop to get the preferred number
            for num in raw_phone:
                if "PREF;" in num:
                    n = self.checkPhone(num)
                    if n != "":
                        data['phone'].append(n)
            for num in raw_phone:
                if "PREF;" not in num:
                    n = self.checkPhone(num)
                    if n != "" and n not in data['phone']:
                        data['phone'].append(n)

            # Extract E-Mails
            raw_email = re.findall("^EMAIL;([\.:a-zA-Z0-9;-_@]*)\n", vcf, re.MULTILINE)
            for mail1 in raw_email:
                mail = mail1.split(":")[1]
                data['email'].append(mail)

            # Extract DOB
            raw_dob = re.findall("^BDAY:([^\n]*)\n", vcf, re.MULTILINE)
            if len(raw_dob) > 1:
                for dobtemp in raw_dob:
                    if dobtemp.startswith("0000"):
                        raw_dob.remove(dobtemp)
            data['dob'] = raw_dob

            # Extract URL
            raw_url = re.findall("^URL:([^\n]*)\n", vcf, re.MULTILINE)
            for url in raw_url:
                if url not in data['url']:
                    data['url'].append(url)

            #  Extract Address
            raw_adr = re.findall("^ADR:([^\n]*)\n", vcf, re.MULTILINE)
            for adr in raw_adr:
                data['addr'] = adr


            # Extract Images
            raw_images = re.findall("^PHOTO;ENCODING=BASE64;([^\n]*)",
                                    vcf.replace("\n\n", "~~`@`~~").replace("\n ", "").replace("~~`@`~~", "\n"),
                                    re.MULTILINE)

            if len(raw_images) > 0:
                for img in raw_images:
                    ext = ".jpg" if "JPEG" in img else ""
                    ext = ".png" if "PNG" in img else ext
                    f_name = "pics/" + data['name'] + ext
                    tn = 0
                    while os.path.exists("pics/" + f_name):
                        f_name = "pics/" + data['name'] + "_" + str(tn) + ext
                        tn += 1
                    open(f_name, "wb").write(base64.b64decode(img.split(":")[1]))

            imgs = os.listdir("pics/")
            for img in imgs:
                img_1 = img.replace(".jpg", "").replace(".png", "").replace("_0", "").replace("_1", "").replace("_2", "")
                if data['name'] == img_1:
                    data['photo'].append("pics/" + img)


            if data['name'] != "":
                self.users.append(data)
                # print data
            # else:
            #     print data

        return self.users

    def verifyName(self, n):

        # data = n.split(";")[1] + " " + n.split(";")[0] + " " + n.split(";")[2] + " " + n.split(";")[3]
        data = n
        data = data.strip()

        # Verification
        # #Alphabets nd nums only
        data = data.replace(".", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
        if "@" in data:
            return ""
        al, num = 0, 0
        for i in data:
            if i.isalpha():
                al += 1
            elif i.isdigit():
                num += 1
        if al < num:
            return ""
        # Parse
        sp = data.split(" ")
        for i in range(0, len(sp)):
            if len(sp[i]) > 2:  # Sentence case
                sp[i] = str(sp[i]).lower().strip()
                sp[i] = str(sp[i][0]).upper() + str(sp[i][1:])

                if sp[i].lower() in self.upperTxts:  # if rset, cse, kve etc
                    sp[i] = sp[i].upper()
            if len(sp[i]) < 3:  # If initials
                sp[i] = sp[i].upper()
        name = " ".join(sp)
        return name

    def checkPhone(self, num):
        # remove spaces
        t = num
        num = num.replace(" ", "").replace("-", "")
        num = num.split(":")[1]
        if "+" not in num:
            num = "+91" + num
        if not re.match("\+[0-9]", num):
            print "Error [Number format]: " + t
            return ""
        else:
            return num

    def saveVCF(self, data, fileName):
        op = open(fileName, "w")
        if ".vcf" in fileName:
            order = [3, 1, 2, 0]
            for u in data:
                FN = "FN:" + u['name']
                ORG = "ORG:"
                if "," in u['name']:
                    ORG = u['name'].split(",")[-1].strip()
                name = u['name'].replace("," + ORG, "")
                Nraw = (" " + name).split(" ")
                N = "N:"
                for i in order:
                    try:
                        N += Nraw[i]
                    except:
                        pass
                    N += ";"
                N += ORG.split(":")[-1]
                TEL = []
                for i in range(0, len(u['phone'])):
                    num = u['phone'][i]
                    t = "TEL"
                    if len(num) == 13:
                        t += ";CELL"
                    elif len(num) > 13:
                        t += ";HOME"
                    if i == 0:
                        t += ";PREF"
                    t += ":" + num
                    TEL.append(t)

                BDAY = ""
                try:
                    BDAY = "BDAY:" + u['dob'][0]
                except:
                    pass

                EMAIL = []
                for em in u['email']:
                    EMAIL.append("EMAIL:" + em)

                URL = []
                for ur in u['url']:
                    URL.append("URL:" + ur)

                PHOTO = []
                for ph in u['photo']:
                    phtxt = "PHOTO;ENCODING=BASE64;JPEG:"
                    b64 = base64.b64encode(open(ph, "rb").read())
                    phtxt += b64[0:47] + "\n"
                    b64 = "".join(b64[47:])
                    while True:
                        phtxt += " " + b64[0:73] + "\n"
                        b64 = "".join(b64[73:])
                        if len(b64) < 73:
                            phtxt += " " + b64
                            break
                    PHOTO.append(phtxt)

                ADR = ""
                if len(u['addr']) > 2:
                    ADR = "ADR:;;" + u['addr'].replace("\n", ", ") + ";;;;"

                details = [i for i in
                           [N, FN, "\n".join(TEL), BDAY, "\n".join(EMAIL), "\n".join(URL), ADR, "\n".join(PHOTO)]
                           if len(i) > 3]

                vcf = "\nBEGIN:VCARD\nVERSION:2.1\n"
                vcf += "\n".join(details)
                vcf += "\n\nEND:VCARD\n"
                op.write(vcf)
            else:
                pass