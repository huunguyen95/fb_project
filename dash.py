# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dashboard_window(object):
    def setupUi(self, dashboard_window):
        dashboard_window.setObjectName("dashboard_window")
        dashboard_window.resize(1341, 651)
        self.centralwidget = QtWidgets.QWidget(dashboard_window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 40, 1321, 561))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label.setObjectName("label")
        dashboard_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(dashboard_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1341, 21))
        self.menubar.setObjectName("menubar")
        dashboard_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(dashboard_window)
        self.statusbar.setObjectName("statusbar")
        dashboard_window.setStatusBar(self.statusbar)

        self.retranslateUi(dashboard_window)
        QtCore.QMetaObject.connectSlotsByName(dashboard_window)

    def retranslateUi(self, dashboard_window):
        _translate = QtCore.QCoreApplication.translate
        dashboard_window.setWindowTitle(_translate("dashboard_window", "dashboard_window"))
        self.label.setText(_translate("dashboard_window", "Info list"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dashboard_window = QtWidgets.QMainWindow()
    ui = Ui_dashboard_window()
    ui.setupUi(dashboard_window)
    dashboard_window.show()
    sys.exit(app.exec_())
