import subprocess

p = subprocess.Popen("android\\adb2 pull \"/storage/emulated/legacy/WhatsApp/Profile Pictures/\" 1/", shell=True)























#
# order = [3, 1, 2, 0]
# u = {
#     "name": "Sarath S Menon"
# }
# FN = u['name']
# ORG = ""
# if "," in u['name']:
#     ORG = u['name'].split(",")[-1].strip()
# name = u['name'].replace("," + ORG, "")
# Nraw = (" " + name).split(" ")
# N = ""
# for i in order:
#     try:
#         N += Nraw[i]
#     except:
#         pass
#     N += ";"
# N += ORG
#
#
#
#
#
#
#


#
#
# import base64
# x = base64.b64encode(open("androidInstructions.png", "rb").read())
# print x

# open("s.csv", "w").write(x)
#
# # open("a.jpg", "wb").write(base64.b64decode(x))
# import base64
# import copy
# import difflib
# import re
#
#
# d = open("final.vcf", "r").read()
# a = d.split("END:VCARD")
# for i in a:
#     # print re.findall("^N:([^\n]*)\n", i, re.MULTILINE)
#     # print re.findall("^TEL;([\+:a-zA-Z 0-9;-]*)\n", i, re.MULTILINE)
#     # print re.findall("^EMAIL;([\.:a-zA-Z0-9;-_@]*)\n", i, re.MULTILINE)
#     # print re.findall("^BDAY:([^\n]*)\n", i, re.MULTILINE)
#     # print re.findall("^URL:([^\n]*)\n", i, re.MULTILINE)
#     ph = re.findall("^PHOTO;ENCODING=BASE64;([^\n]*)",
#                      i.replace("\n\n", "~~`@`~~").replace("\n ", "").replace("~~`@`~~", "\n"), re.MULTILINE)
#     if len(ph)>0:
#         open("aww.jpg", "wb").write(base64.b64decode(ph[0].split(":")[1]))
#         exit(0)
# print len(a)
#
#

# def verifyName(n):
#
#         data = n.split(";")[1] + " " + n.split(";")[0] + " " + n.split(";")[2] + " " + n.split(";")[3]
#         data = data.strip()
#         upperTxts = ["rset", "kv", "kve", "sap", "cs", "cse", "s1s2"]
#         # Verification
#         # #Alphabets nd nums only
#         data = data.replace(".", " ").replace("  ", " ").replace("  ", " ").replace("  ", " ")
#         if "@" in data:
#             return ""
#         al, num = 0, 0
#         for i in data:
#             if i.isalpha():
#                 al += 1
#             elif i.isdigit():
#                 num += 1
#         if al < num:
#             return ""
#         # Parse
#         sp = data.split(" ")
#         for i in range(0, len(sp)):
#             if len(sp[i]) > 2:  # Sentence case
#                 sp[i] = str(sp[i]).lower().strip()
#                 sp[i] = str(sp[i][0]).upper() + str(sp[i][1:])
#
#                 if sp[i].lower() in upperTxts:  # if rset, cse, kve etc
#                     sp[i] = sp[i].upper()
#             if len(sp[i]) < 3:  # If initials
#                 sp[i] = sp[i].upper()
#         name = " ".join(sp)
#         return name
#
# d = open("googcal.txt", "r").read()
# a = d.split("END:VEVENT")
# names = []
# dts = []
# for i in a:
#     icon = re.findall("X-GOOGLE-CALENDAR-CONTENT-ICON:([^\n]*)", i, re.MULTILINE)
#     if len(icon)>0 and icon[0] == "https://calendar.google.com/googlecalendar/i":
#         name = re.findall("DESCRIPTION:This is ([^']*)'s birthday!", i, re.MULTILINE)
#         if len(name) > 0 and name[0] not in names:
#             names.append(name[0])
#             dt = re.findall("DTSTART;VALUE=DATE:([0-9]*)\n", i, re.MULTILINE)[0]
#             d = "0000-" + dt[4:6] + "-" + dt[6:8]
#             dts.append(d)
# vcfdata = open("final.vcf", "r").read()
# vcfs = vcfdata.split("END:VCARD")
# for vcf in vcfs:
#
#     raw_name, name = re.findall("^N:([^\n]*)\n", vcf, re.MULTILINE), ""
#     if len(raw_name) == 1:
#         name = verifyName(raw_name[0])
#     if name == "":
#         # print "Error: [No Name] : \n" + vcf
#         pass
#     else:
#         i = name
#         nm = difflib.get_close_matches(i, names)
#         # if len(nm) == 0:
#         #     open("mod.vcf", "a").write(vcf+"\nEND:VCARD\n")
#         # for j in nm:
#         #     t = dts[names.index(j)]
#         #     print i, j
#         #     ans = raw_input(">>")
#         #     if ans == "":
#         #         continue
#         #     else:
#         #         open("mod.vcf", "a").write(vcf.replace("VERSION:2.1", "VERSION:2.1\nBDAY:" + t) + "\nEND:VCARD\n")