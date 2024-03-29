# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(769, 593)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(639, 530, 121, 21))
        self.exitButton.setObjectName("exitButton")
        self.directoryPath = QtWidgets.QLineEdit(self.centralwidget)
        self.directoryPath.setGeometry(QtCore.QRect(190, 10, 571, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.directoryPath.setFont(font)
        self.directoryPath.setObjectName("directoryPath")
        self.upButton = QtWidgets.QPushButton(self.centralwidget)
        self.upButton.setGeometry(QtCore.QRect(10, 10, 41, 21))
        self.upButton.setObjectName("upButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 111, 16))
        self.label.setObjectName("label")
        self.directory = QtWidgets.QListWidget(self.centralwidget)
        self.directory.setGeometry(QtCore.QRect(190, 40, 571, 481))
        self.directory.setObjectName("directory")
        self.directoryTree = QtWidgets.QTreeWidget(self.centralwidget)
        self.directoryTree.setGeometry(QtCore.QRect(10, 40, 171, 481))
        self.directoryTree.setObjectName("directoryTree")
        self.directoryTree.headerItem().setText(0, "1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 769, 17))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.upButton, self.directoryPath)
        MainWindow.setTabOrder(self.directoryPath, self.exitButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.exitButton.setText(_translate("MainWindow", "Выход"))
        self.upButton.setText(_translate("MainWindow", "⬆️"))
        self.label.setText(_translate("MainWindow", "Путь к папке :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
