# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Sat Jul 25 22:16:23 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_VCFEditor(object):
    def setupUi(self, VCFEditor):
        VCFEditor.setObjectName("VCFEditor")
        VCFEditor.resize(719, 671)
        VCFEditor.setStyleSheet("background-color: rgb(241, 241, 241);")
        VCFEditor.setSizeGripEnabled(True)
        VCFEditor.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(VCFEditor)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upframe = QtGui.QFrame(VCFEditor)
        self.upframe.setStyleSheet("")
        self.upframe.setFrameShape(QtGui.QFrame.Box)
        self.upframe.setFrameShadow(QtGui.QFrame.Raised)
        self.upframe.setLineWidth(5)
        self.upframe.setMidLineWidth(3)
        self.upframe.setObjectName("upframe")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.upframe)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_3 = QtGui.QFrame(self.upframe)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_3 = QtGui.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Raised)
        self.label_3.setLineWidth(3)
        self.label_3.setMidLineWidth(3)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_10.addWidget(self.label_3)
        self.frame_4 = QtGui.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_4.setLineWidth(0)
        self.frame_4.setMidLineWidth(0)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_11 = QtGui.QHBoxLayout(self.frame_4)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ui_help = QtGui.QPushButton(self.frame_4)
        self.ui_help.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ui_help.setAutoDefault(False)
        self.ui_help.setFlat(True)
        self.ui_help.setObjectName("ui_help")
        self.horizontalLayout_6.addWidget(self.ui_help)
        self.ui_min = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_min.sizePolicy().hasHeightForWidth())
        self.ui_min.setSizePolicy(sizePolicy)
        self.ui_min.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ui_min.setToolTip("")
        self.ui_min.setStatusTip("")
        self.ui_min.setWhatsThis("")
        self.ui_min.setShortcut("")
        self.ui_min.setAutoDefault(False)
        self.ui_min.setFlat(True)
        self.ui_min.setObjectName("ui_min")
        self.horizontalLayout_6.addWidget(self.ui_min)
        self.ui_exit = QtGui.QPushButton(self.frame_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui_exit.sizePolicy().hasHeightForWidth())
        self.ui_exit.setSizePolicy(sizePolicy)
        self.ui_exit.setMaximumSize(QtCore.QSize(30, 16777215))
        self.ui_exit.setStyleSheet("")
        self.ui_exit.setAutoDefault(False)
        self.ui_exit.setFlat(True)
        self.ui_exit.setObjectName("ui_exit")
        self.horizontalLayout_6.addWidget(self.ui_exit)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10.addWidget(self.frame_4)
        self.horizontalLayout_10.setStretch(0, 50)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.frame = QtGui.QFrame(self.upframe)
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.namelist = QtGui.QListWidget(self.frame)
        self.namelist.setStyleSheet("")
        self.namelist.setObjectName("namelist")
        self.verticalLayout_2.addWidget(self.namelist)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(3)
        self.horizontalLayout_13.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.u_add = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_add.sizePolicy().hasHeightForWidth())
        self.u_add.setSizePolicy(sizePolicy)
        self.u_add.setMinimumSize(QtCore.QSize(50, 50))
        self.u_add.setMaximumSize(QtCore.QSize(50, 50))
        self.u_add.setObjectName("u_add")
        self.horizontalLayout_13.addWidget(self.u_add)
        self.u_delete = QtGui.QPushButton(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_delete.sizePolicy().hasHeightForWidth())
        self.u_delete.setSizePolicy(sizePolicy)
        self.u_delete.setMinimumSize(QtCore.QSize(50, 50))
        self.u_delete.setMaximumSize(QtCore.QSize(50, 50))
        self.u_delete.setStyleSheet("")
        self.u_delete.setObjectName("u_delete")
        self.horizontalLayout_13.addWidget(self.u_delete)
        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.verticalLayout_2.setStretch(0, 12)
        self.verticalLayout_2.setStretch(1, 1)
        self.horizontalLayout_8.addLayout(self.verticalLayout_2)
        self.widget = QtGui.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.scrollArea_2 = QtGui.QScrollArea(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy)
        self.scrollArea_2.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.scrollArea_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.scrollArea_2.setStyleSheet("")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 531, 547))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout = QtGui.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.WrapLongRows)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName("formLayout")
        self._2 = QtGui.QHBoxLayout()
        self._2.setSpacing(0)
        self._2.setContentsMargins(0, -1, -1, -1)
        self._2.setObjectName("_2")
        self.u_imgs = QtGui.QWidget(self.scrollAreaWidgetContents_2)
        self.u_imgs.setObjectName("u_imgs")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.u_imgs)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.u_img1 = QtGui.QLabel(self.u_imgs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_img1.sizePolicy().hasHeightForWidth())
        self.u_img1.setSizePolicy(sizePolicy)
        self.u_img1.setMinimumSize(QtCore.QSize(150, 150))
        self.u_img1.setStyleSheet("")
        self.u_img1.setFrameShape(QtGui.QFrame.Panel)
        self.u_img1.setFrameShadow(QtGui.QFrame.Raised)
        self.u_img1.setLineWidth(3)
        self.u_img1.setMidLineWidth(2)
        self.u_img1.setText("")
        self.u_img1.setScaledContents(True)
        self.u_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.u_img1.setObjectName("u_img1")
        self.verticalLayout.addWidget(self.u_img1)
        self.u_img1_sel = QtGui.QPushButton(self.u_imgs)
        self.u_img1_sel.setObjectName("u_img1_sel")
        self.verticalLayout.addWidget(self.u_img1_sel)
        self.u_img1_set = QtGui.QPushButton(self.u_imgs)
        self.u_img1_set.setObjectName("u_img1_set")
        self.verticalLayout.addWidget(self.u_img1_set)
        self.u_img1_del = QtGui.QPushButton(self.u_imgs)
        self.u_img1_del.setObjectName("u_img1_del")
        self.verticalLayout.addWidget(self.u_img1_del)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.u_img2 = QtGui.QLabel(self.u_imgs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_img2.sizePolicy().hasHeightForWidth())
        self.u_img2.setSizePolicy(sizePolicy)
        self.u_img2.setMinimumSize(QtCore.QSize(150, 150))
        self.u_img2.setFrameShape(QtGui.QFrame.Panel)
        self.u_img2.setFrameShadow(QtGui.QFrame.Raised)
        self.u_img2.setLineWidth(3)
        self.u_img2.setMidLineWidth(2)
        self.u_img2.setText("")
        self.u_img2.setScaledContents(True)
        self.u_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.u_img2.setObjectName("u_img2")
        self.verticalLayout_3.addWidget(self.u_img2)
        self.u_img2_sel = QtGui.QPushButton(self.u_imgs)
        self.u_img2_sel.setObjectName("u_img2_sel")
        self.verticalLayout_3.addWidget(self.u_img2_sel)
        self.u_img2_set = QtGui.QPushButton(self.u_imgs)
        self.u_img2_set.setObjectName("u_img2_set")
        self.verticalLayout_3.addWidget(self.u_img2_set)
        self.u_img2_del = QtGui.QPushButton(self.u_imgs)
        self.u_img2_del.setObjectName("u_img2_del")
        self.verticalLayout_3.addWidget(self.u_img2_del)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.u_img3 = QtGui.QLabel(self.u_imgs)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_img3.sizePolicy().hasHeightForWidth())
        self.u_img3.setSizePolicy(sizePolicy)
        self.u_img3.setMinimumSize(QtCore.QSize(150, 150))
        self.u_img3.setFrameShape(QtGui.QFrame.Panel)
        self.u_img3.setFrameShadow(QtGui.QFrame.Raised)
        self.u_img3.setLineWidth(3)
        self.u_img3.setMidLineWidth(2)
        self.u_img3.setText("")
        self.u_img3.setScaledContents(True)
        self.u_img3.setAlignment(QtCore.Qt.AlignCenter)
        self.u_img3.setObjectName("u_img3")
        self.verticalLayout_4.addWidget(self.u_img3)
        self.u_img3_sel = QtGui.QPushButton(self.u_imgs)
        self.u_img3_sel.setObjectName("u_img3_sel")
        self.verticalLayout_4.addWidget(self.u_img3_sel)
        self.u_img3_set = QtGui.QPushButton(self.u_imgs)
        self.u_img3_set.setObjectName("u_img3_set")
        self.verticalLayout_4.addWidget(self.u_img3_set)
        self.u_img3_del = QtGui.QPushButton(self.u_imgs)
        self.u_img3_del.setObjectName("u_img3_del")
        self.verticalLayout_4.addWidget(self.u_img3_del)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(2, 1)
        self._2.addWidget(self.u_imgs)
        self.formLayout.setLayout(0, QtGui.QFormLayout.SpanningRole, self._2)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setCursor(QtCore.Qt.PointingHandCursor)
        self.label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label.setWordWrap(False)
        self.label.setOpenExternalLinks(True)
        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label)
        self.u_name = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_name.sizePolicy().hasHeightForWidth())
        self.u_name.setSizePolicy(sizePolicy)
        self.u_name.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_name.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_name.setStyleSheet("")
        self.u_name.setObjectName("u_name")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.u_name)
        self.label_9 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_9.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_9.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_9)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.u_ph1 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_ph1.sizePolicy().hasHeightForWidth())
        self.u_ph1.setSizePolicy(sizePolicy)
        self.u_ph1.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_ph1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_ph1.setStyleSheet("")
        self.u_ph1.setObjectName("u_ph1")
        self.horizontalLayout_3.addWidget(self.u_ph1)
        self.u_ph2 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_ph2.sizePolicy().hasHeightForWidth())
        self.u_ph2.setSizePolicy(sizePolicy)
        self.u_ph2.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_ph2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_ph2.setStyleSheet("")
        self.u_ph2.setObjectName("u_ph2")
        self.horizontalLayout_3.addWidget(self.u_ph2)
        self.u_ph3 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_ph3.sizePolicy().hasHeightForWidth())
        self.u_ph3.setSizePolicy(sizePolicy)
        self.u_ph3.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_ph3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_ph3.setStyleSheet("")
        self.u_ph3.setObjectName("u_ph3")
        self.horizontalLayout_3.addWidget(self.u_ph3)
        self.horizontalLayout_3.setStretch(1, 1)
        self.formLayout.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_2.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.u_email1 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_email1.sizePolicy().hasHeightForWidth())
        self.u_email1.setSizePolicy(sizePolicy)
        self.u_email1.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_email1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_email1.setStyleSheet("")
        self.u_email1.setObjectName("u_email1")
        self.horizontalLayout_4.addWidget(self.u_email1)
        self.u_email2 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_email2.sizePolicy().hasHeightForWidth())
        self.u_email2.setSizePolicy(sizePolicy)
        self.u_email2.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_email2.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_email2.setStyleSheet("")
        self.u_email2.setObjectName("u_email2")
        self.horizontalLayout_4.addWidget(self.u_email2)
        self.u_email3 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_email3.sizePolicy().hasHeightForWidth())
        self.u_email3.setSizePolicy(sizePolicy)
        self.u_email3.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_email3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_email3.setStyleSheet("")
        self.u_email3.setObjectName("u_email3")
        self.horizontalLayout_4.addWidget(self.u_email3)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 1)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_5 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_5.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_5.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.u_dob = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_dob.sizePolicy().hasHeightForWidth())
        self.u_dob.setSizePolicy(sizePolicy)
        self.u_dob.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_dob.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_dob.setStyleSheet("")
        self.u_dob.setObjectName("u_dob")
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.u_dob)
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_6.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_6.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setOpenExternalLinks(True)
        self.label_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.u_url1 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_url1.sizePolicy().hasHeightForWidth())
        self.u_url1.setSizePolicy(sizePolicy)
        self.u_url1.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_url1.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_url1.setStyleSheet("")
        self.u_url1.setObjectName("u_url1")
        self.horizontalLayout_12.addWidget(self.u_url1)
        self.u_url2 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_url2.sizePolicy().hasHeightForWidth())
        self.u_url2.setSizePolicy(sizePolicy)
        self.u_url2.setObjectName("u_url2")
        self.horizontalLayout_12.addWidget(self.u_url2)
        self.u_url3 = QtGui.QLineEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_url3.sizePolicy().hasHeightForWidth())
        self.u_url3.setSizePolicy(sizePolicy)
        self.u_url3.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_url3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_url3.setStyleSheet("")
        self.u_url3.setObjectName("u_url3")
        self.horizontalLayout_12.addWidget(self.u_url3)
        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 1)
        self.formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.horizontalLayout_12)
        self.label_7 = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setCursor(QtCore.Qt.PointingHandCursor)
        self.label_7.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_7.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextEditable)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_7)
        self.u_addr = QtGui.QTextEdit(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_addr.sizePolicy().hasHeightForWidth())
        self.u_addr.setSizePolicy(sizePolicy)
        self.u_addr.setMaximumSize(QtCore.QSize(16777215, 75))
        self.u_addr.setProperty("cursor", QtCore.Qt.PointingHandCursor)
        self.u_addr.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_addr.setStyleSheet("")
        self.u_addr.setFrameShape(QtGui.QFrame.Panel)
        self.u_addr.setFrameShadow(QtGui.QFrame.Raised)
        self.u_addr.setObjectName("u_addr")
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.u_addr)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.u_cancel = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_cancel.sizePolicy().hasHeightForWidth())
        self.u_cancel.setSizePolicy(sizePolicy)
        self.u_cancel.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_cancel.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_cancel.setStyleSheet("")
        self.u_cancel.setObjectName("u_cancel")
        self.horizontalLayout_7.addWidget(self.u_cancel)
        self.u_save = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.u_save.sizePolicy().hasHeightForWidth())
        self.u_save.setSizePolicy(sizePolicy)
        self.u_save.setCursor(QtCore.Qt.PointingHandCursor)
        self.u_save.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.u_save.setStyleSheet("")
        self.u_save.setObjectName("u_save")
        self.horizontalLayout_7.addWidget(self.u_save)
        self.formLayout.setLayout(9, QtGui.QFormLayout.FieldRole, self.horizontalLayout_7)
        self.u_export = QtGui.QPushButton(self.scrollAreaWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.u_export.sizePolicy().hasHeightForWidth())
        self.u_export.setSizePolicy(sizePolicy)
        self.u_export.setMinimumSize(QtCore.QSize(0, 50))
        self.u_export.setStyleSheet("")
        self.u_export.setObjectName("u_export")
        self.formLayout.setWidget(10, QtGui.QFormLayout.FieldRole, self.u_export)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.addWidget(self.scrollArea_2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_8.addWidget(self.widget)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 4)
        self.verticalLayout_5.addWidget(self.frame)
        self.frame_2 = QtGui.QFrame(self.upframe)
        self.frame_2.setFrameShape(QtGui.QFrame.Box)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(2)
        self.horizontalLayout_9.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.ui_status = QtGui.QLabel(self.frame_2)
        self.ui_status.setText("")
        self.ui_status.setObjectName("ui_status")
        self.horizontalLayout_9.addWidget(self.ui_status)
        self.label_10 = QtGui.QLabel(self.frame_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.ui_contacts = QtGui.QLabel(self.frame_2)
        self.ui_contacts.setText("")
        self.ui_contacts.setObjectName("ui_contacts")
        self.horizontalLayout_9.addWidget(self.ui_contacts)
        self.label_12 = QtGui.QLabel(self.frame_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_9.addWidget(self.label_12)
        self.ui_deleted = QtGui.QLabel(self.frame_2)
        self.ui_deleted.setText("")
        self.ui_deleted.setObjectName("ui_deleted")
        self.horizontalLayout_9.addWidget(self.ui_deleted)
        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 1)
        self.horizontalLayout_9.setStretch(3, 2)
        self.horizontalLayout_9.setStretch(4, 1)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.verticalLayout_5.setStretch(1, 17)
        self.verticalLayout_5.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.upframe)

        self.retranslateUi(VCFEditor)
        QtCore.QMetaObject.connectSlotsByName(VCFEditor)

    def retranslateUi(self, VCFEditor):
        VCFEditor.setWindowTitle(QtGui.QApplication.translate("VCFEditor", "VCFEditor", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("VCFEditor", "VCF Editor v1.0", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_help.setText(QtGui.QApplication.translate("VCFEditor", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_min.setText(QtGui.QApplication.translate("VCFEditor", "_", None, QtGui.QApplication.UnicodeUTF8))
        self.ui_exit.setText(QtGui.QApplication.translate("VCFEditor", "X", None, QtGui.QApplication.UnicodeUTF8))
        self.u_add.setText(QtGui.QApplication.translate("VCFEditor", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.u_delete.setText(QtGui.QApplication.translate("VCFEditor", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img1_sel.setText(QtGui.QApplication.translate("VCFEditor", "Select Image", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img1_set.setText(QtGui.QApplication.translate("VCFEditor", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img1_del.setText(QtGui.QApplication.translate("VCFEditor", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img2_sel.setText(QtGui.QApplication.translate("VCFEditor", "Select Image", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img2_set.setText(QtGui.QApplication.translate("VCFEditor", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img2_del.setText(QtGui.QApplication.translate("VCFEditor", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img3_sel.setText(QtGui.QApplication.translate("VCFEditor", "Select Image", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img3_set.setText(QtGui.QApplication.translate("VCFEditor", "Set Default", None, QtGui.QApplication.UnicodeUTF8))
        self.u_img3_del.setText(QtGui.QApplication.translate("VCFEditor", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VCFEditor", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("VCFEditor", "Phone", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("VCFEditor", "E-mail", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("VCFEditor", "DOB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("VCFEditor", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("VCFEditor", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.u_cancel.setText(QtGui.QApplication.translate("VCFEditor", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.u_save.setText(QtGui.QApplication.translate("VCFEditor", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.u_export.setText(QtGui.QApplication.translate("VCFEditor", "Export", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("VCFEditor", "Contacts:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("VCFEditor", "Deleted:", None, QtGui.QApplication.UnicodeUTF8))

