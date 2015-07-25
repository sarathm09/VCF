from sys import argv
from PySide.QtGui import *
from PySide.QtCore import *
import qdarkstyle
import ui
from sui import Ui_Dialog
from vcfP import vcfManager
import AndroidConnect


class VCFEditor(QDialog, ui.Ui_VCFEditor):

    data = []
    deleted = []

    def __init__(self):
        super(VCFEditor, self).__init__()

        self.setupUi(self)
        self.setStyleSheet(qdarkstyle.load_stylesheet())
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.resizeEvent = self.ui_resize
        self.ui_resize("")

        self.initUi()

    def initUi(self):
        self.buttonsLinker()
        vcfFile = ""

        self.ui = Ui_Dialog()
        while self.ui.exec_():
            pass
        op = self.ui.option

        if "exit" in op:
            exit(0)

        if op == "vcf":
            vcfFile = QFileDialog.getOpenFileName(self, "Open VCF file", ".", "*.vcf")

        if op == "android":
            f = AndroidConnect.connect()
            print f
            if f == "":
                exit(0)
            vcfFile = [f, ""]

        if vcfFile[0] == "":
            exit(0)
        else:
            self.data = vcfManager().parseVCF(open(vcfFile[0], "r"))
        self.data = sorted(self.data, key=lambda k: k['name'])
        for u in self.data:
            self.namelist.addItem(u['name'])
        self.namelist.currentItemChanged.connect(self.loadUser)
        self.namelist.setFocus()
        self.namelist.setCurrentRow(0)
        self.show()

    def buttonsLinker(self):
        self.ui_exit.clicked.connect(self.close)
        self.ui_min.clicked.connect(self.showMinimized)
        self.ui_help.clicked.connect(self.help)

        self.u_add.clicked.connect(self.addUser)
        self.u_delete.clicked.connect(self.deleteUser)

        self.u_export.clicked.connect(self.exportUsers)

        self.u_save.clicked.connect(self.saveUser)
        self.u_cancel.clicked.connect(self.loadUser)

        self.u_img1_del.clicked.connect(lambda: self.imageUpdater(1, "del"))
        self.u_img2_del.clicked.connect(lambda: self.imageUpdater(2, "del"))
        self.u_img3_del.clicked.connect(lambda: self.imageUpdater(3, "del"))

        self.u_img1_sel.clicked.connect(lambda: self.imageUpdater(1, "sel"))
        self.u_img2_sel.clicked.connect(lambda: self.imageUpdater(2, "sel"))
        self.u_img3_sel.clicked.connect(lambda: self.imageUpdater(3, "sel"))

        self.u_img1_set.clicked.connect(lambda: self.imageUpdater(1, "set"))
        self.u_img2_set.clicked.connect(lambda: self.imageUpdater(2, "set"))
        self.u_img3_set.clicked.connect(lambda: self.imageUpdater(3, "set"))

        self.ui_exit.installEventFilter(self)
        self.ui_min.installEventFilter(self)
        self.ui_help.installEventFilter(self)

        self.u_add.installEventFilter(self)
        self.u_delete.installEventFilter(self)

        self.u_export.installEventFilter(self)

        self.u_cancel.installEventFilter(self)
        self.u_save.installEventFilter(self)

        self.u_img1_sel.installEventFilter(self)
        self.u_img1_set.installEventFilter(self)
        self.u_img1_del.installEventFilter(self)
        self.u_img2_sel.installEventFilter(self)
        self.u_img2_set.installEventFilter(self)
        self.u_img2_del.installEventFilter(self)
        self.u_img3_sel.installEventFilter(self)
        self.u_img3_set.installEventFilter(self)
        self.u_img3_del.installEventFilter(self)

        self.namelist.installEventFilter(self)

    def deleteUser(self):
        ind = self.namelist.currentRow()
        self.deleted.append(self.data[ind])
        self.data.pop(ind)
        self.namelist.takeItem(ind)
        self.loadUser()

    def addUser(self):
        self.namelist.addItem("Un-named Contact")
        self.data.append(vcfManager.user_data)
        item = self.namelist.findItems("Un-named Contact", Qt.MatchExactly)
        if len(item) > 0:
            self.namelist.setCurrentItem(item[0])


    def exportUsers(self):
        fileName = QFileDialog.getSaveFileName(self, "Export Contacts", ".", "*.vcf;;*.csv")
        print fileName[0].split(".")[-1]
        vcfManager().saveVCF(self.data, fileName[0])

    def saveUser(self):
        ind = self.namelist.currentRow()
        try:
            self.data[ind]['name'] = self.u_name.text()
            self.data[ind]['phone'] = [self.u_ph1.text(), self.u_ph2.text(), self.u_ph3.text()]
            self.data[ind]['email'] = [self.u_email1.text(), self.u_email2.text(), self.u_email3.text()]
            self.data[ind]['dob'] = self.u_dob.text()
            self.data[ind]['url'] = [self.u_url1.text(), self.u_url2.text()]
            self.data[ind]['addr'] = self.u_addr.toPlainText()
            self.namelist.currentItem().setText(self.u_name.text())
        except:
            self.setStatus("error,SaveError")

    def imageUpdater(self, num, action):
        imgs = [self.u_img1, self.u_img2, self.u_img3]
        img = imgs[num-1]
        user = self.data[self.namelist.currentRow()]

        if action == "sel":
            fileName = QFileDialog.getOpenFileName(self, "Open Image", "pics/", "Image Files (*.png *.jpg *.bmp)")
            if fileName[0] != "":
                try:
                   user['photo'][num-1] = fileName[0]
                except:
                    user['photo'].append(fileName[0])
                im = QPixmap(fileName[0], "jpeg")
                img.setPixmap(im)
                pass

        elif action == "set":
            try:
                user['photo'][0], user['photo'][num-1] = user['photo'][num-1], user['photo'][0]
            except:
                self.setStatus("error, NoImageToSetDefault")
            self.loadUser()

        elif action == "del":
            try:
                user['photo'].pop(num-1)
            except:
                self.setStatus("error, NoImageToDelete")
            self.loadUser()

    def loadUser(self):
        index = self.namelist.currentRow()
        user = self.data[index]

        # Load Name
        self.u_name.setText(user['name'])

        # Load Phones
        self.u_ph1.clear()
        self.u_ph2.clear()
        self.u_ph3.clear()
        try:
            self.u_ph1.setText(user['phone'][0])
        except:
            self.u_ph1.setText("")
        try:
            self.u_ph2.setText(user['phone'][1])
        except:
            self.u_ph2.setText("")
        try:
            self.u_ph3.setText(user['phone'][2])
        except:
            self.u_ph3.setText("")

        # Load Emails
        self.u_email1.clear()
        self.u_email2.clear()
        self.u_email3.clear()
        try:
            self.u_email1.setText(user['email'][0])
        except:
            self.u_email1.setText("")
        try:
            self.u_email2.setText(user['email'][1])
        except:
            self.u_email2.setText("")
        try:
            self.u_email3.setText(user['email'][2])
        except:
            self.u_email3.setText("")

        # Load DOB
        self.u_dob.clear()
        self.u_dob.setText(", ".join(user['dob']))

        # Load URL
        urlIP = [self.u_url1, self.u_url2, self.u_url3]
        unum = 0
        for u in user['url']:
            urlIP[unum].clear()
            urlIP[unum].setText(u)
            unum += 1

        # Load Address
        self.u_addr.clear()
        self.u_addr.setText(user['addr'])

        # Load Image
        self.u_img1.clear()
        self.u_img2.clear()
        self.u_img3.clear()

        imgs = [self.u_img1, self.u_img2, self.u_img3]
        imgCount = 0
        for im in user['photo']:
            img = QPixmap(im, "jpeg")
            imgs[imgCount].setPixmap(img)
            imgCount += 1

    def ui_resize(self, event):
        w = (self.u_imgs.width()-10)/3

        self.u_img1.setFixedWidth(w)
        self.u_img2.setFixedWidth(w)
        self.u_img3.setFixedWidth(w)

        self.u_imgs.setFixedHeight(w+100)

    def help(self):
        helpndabt = QDialog(self)
        helpndabt.setWindowTitle("Help and About")
        helpndabt.setModal(True)

        lay = QVBoxLayout(helpndabt)

        title = QLabel(self)
        title.setText("Help and About")
        font = QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        title.setFont(font)
        title.setAlignment(Qt.AlignCenter)
        title.setMargin(20)

        info = QLabel(self)
        info.setText("VCF Editor v1.0")
        info.setAlignment(Qt.AlignCenter)

        helptxt = QLabel(self)
        helptxt.setText("sdf")
        helptxt.setAlignment(Qt.AlignJustify)

        lay.addWidget(title)
        lay.addWidget(info)
        lay.addWidget(helptxt)

        helpndabt.show()

    def setStatus(self, msg):
        status = ""
        if msg == "min":
            status = "Click to minimize the app"
        if msg == "exit":
            status = "Click to close the app"
        if msg == "help":
            status = "Help and About this app"

        if msg == "delBtn":
            status = "Delete current contact"
        if msg == "addBtn":
            status = "Add new contact"

        if msg == "expBtn":
            status = "Export all contact details"
        if msg == "selContact":
            status = "Click on any contact to edit"
        if msg == "selImg":
            status = "Select an image for the contact"
        if msg == "setImg":
            status = "Set this image as default"
        if msg == "delImg":
            status = "Delete this image"
        if msg == "saveBtn":
            status = "Save changes to the contact"
        if msg == "cancelBtn":
            status = "Revert all changes since last save"

        if msg == "add":
            status = "New contact added"
        if msg == "del":
            status = "Contact deleted"

        if msg == "exp":
            status = "Contacts exported"

        if msg == "imgSel":
            status = "New image added to contact details"
        if msg == "imgDel":
            status = "Contact image deleted"
        if msg == "imgSet":
            status = "Contact image set as default"
        if msg == "save":
            status = "Details saved"

        if "error" in msg:
            status = "Oops!!! Some error occurred [Code: " + msg.split(",")[1] + "]"

        self.ui_status.setText(status)

    def eventFilter(self, ob, event):

        statusMsgs = {
            self.ui_exit: ["exit", ""],
            self.ui_min: ["min", ""],
            self.ui_help: ["help", ""],

            self.u_add: ["addBtn", "add"],
            self.u_delete: ["delBtn", "del"],

            self.u_export: ["expBtn", "exp"],

            self.u_cancel: ["cancelBtn", "undo"],
            self.u_save: ["saveBtn", "save"],

            self.u_img1_sel: ["selImg", "imgSel"],
            self.u_img1_set: ["setImg", "imgSet"],
            self.u_img1_del: ["selImg", "imgDel"],
            self.u_img2_sel: ["selImg", "imgSel"],
            self.u_img2_set: ["setImg", "imgSet"],
            self.u_img2_del: ["selImg", "imgDel"],
            self.u_img3_sel: ["selImg", "imgSel"],
            self.u_img3_set: ["setImg", "imgSet"],
            self.u_img3_del: ["selImg", "imgDel"],

            self.namelist: ["selContact", ""]
        }

        if event.type() == QEvent.Type.HoverEnter:
            self.setStatus(statusMsgs[ob][0])
        if event.type() == QEvent.MouseButtonPress:
            self.setStatus(statusMsgs[ob][1])
            self.namelist.setFocus()

        self.ui_contacts.setText(str(len(self.data)))
        self.ui_deleted.setText(str(len(self.deleted)))

        return False


a = QApplication(argv)
vcf = VCFEditor()
a.exec_()