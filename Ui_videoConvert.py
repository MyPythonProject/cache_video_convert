# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\UserData\Personal\GitHub\Python\cache_viddeo_convert\videoConvert.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(984, 675)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        Form.setFont(font)
        Form.setStyleSheet("color: rgba(255, 85, 128);\n"
"font: 75 11pt \"微软雅黑\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop:0.1 rgba(255, 255, 255, 255), stop:0.2 rgba(255, 176, 176, 167), stop:0.3 rgba(255, 151, 151, 92), stop:0.4 rgba(255, 125, 125, 51), stop:0.5 rgba(255, 76, 76, 205), stop:0.52 rgba(255, 76, 76, 205), stop:0.6 rgba(255, 180, 180, 84), stop:1 rgba(255, 255, 255, 0));")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_choice_load = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choice_load.sizePolicy().hasHeightForWidth())
        self.btn_choice_load.setSizePolicy(sizePolicy)
        self.btn_choice_load.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_choice_load.setAutoFillBackground(False)
        self.btn_choice_load.setObjectName("btn_choice_load")
        self.gridLayout.addWidget(self.btn_choice_load, 0, 0, 1, 1)
        self.label_dir_load = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dir_load.sizePolicy().hasHeightForWidth())
        self.label_dir_load.setSizePolicy(sizePolicy)
        self.label_dir_load.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_dir_load.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dir_load.setObjectName("label_dir_load")
        self.gridLayout.addWidget(self.label_dir_load, 0, 1, 1, 1)
        self.btn_choice_out = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_choice_out.sizePolicy().hasHeightForWidth())
        self.btn_choice_out.setSizePolicy(sizePolicy)
        self.btn_choice_out.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btn_choice_out.setAutoFillBackground(False)
        self.btn_choice_out.setObjectName("btn_choice_out")
        self.gridLayout.addWidget(self.btn_choice_out, 1, 0, 1, 1)
        self.label_dir_out = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_dir_out.sizePolicy().hasHeightForWidth())
        self.label_dir_out.setSizePolicy(sizePolicy)
        self.label_dir_out.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_dir_out.setAlignment(QtCore.Qt.AlignCenter)
        self.label_dir_out.setObjectName("label_dir_out")
        self.gridLayout.addWidget(self.label_dir_out, 1, 1, 1, 1)
        self.chk_delete_source = QtWidgets.QCheckBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chk_delete_source.sizePolicy().hasHeightForWidth())
        self.chk_delete_source.setSizePolicy(sizePolicy)
        self.chk_delete_source.setObjectName("chk_delete_source")
        self.gridLayout.addWidget(self.chk_delete_source, 2, 0, 1, 2)
        self.list_file = QtWidgets.QListView(Form)
        self.list_file.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.list_file.setStyleSheet("background-color: qconicalgradient(cx:1, cy:1, angle:0, stop:0 rgba(0, 0, 0, 127), stop:1 rgba(255, 255, 255, 127));")
        self.list_file.setObjectName("list_file")
        self.gridLayout.addWidget(self.list_file, 3, 0, 1, 2)
        self.progress_convert = QtWidgets.QProgressBar(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress_convert.sizePolicy().hasHeightForWidth())
        self.progress_convert.setSizePolicy(sizePolicy)
        self.progress_convert.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.progress_convert.setProperty("value", 100)
        self.progress_convert.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_convert.setObjectName("progress_convert")
        self.gridLayout.addWidget(self.progress_convert, 4, 0, 1, 2)
        self.btn_go = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_go.sizePolicy().hasHeightForWidth())
        self.btn_go.setSizePolicy(sizePolicy)
        self.btn_go.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        font.setStrikeOut(False)
        self.btn_go.setFont(font)
        self.btn_go.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.btn_go.setObjectName("btn_go")
        self.gridLayout.addWidget(self.btn_go, 5, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "缓存视频转换"))
        self.btn_choice_load.setToolTip(_translate("Form", "选择要转码的视频文件目录"))
        self.btn_choice_load.setText(_translate("Form", "加载转换目录"))
        self.label_dir_load.setText(_translate("Form", "加载目录"))
        self.btn_choice_out.setToolTip(_translate("Form", "选择要转码的视频文件目录"))
        self.btn_choice_out.setText(_translate("Form", "选择输出目录"))
        self.label_dir_out.setText(_translate("Form", "输出目录"))
        self.chk_delete_source.setText(_translate("Form", "转换完成后删除源文件"))
        self.btn_go.setText(_translate("Form", "开始转换"))
