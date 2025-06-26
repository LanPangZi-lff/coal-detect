# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setPointSize(6)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	\n"
"	background-color: rgb(221, 221, 221);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.detectButton_1 = QPushButton(self.centralwidget)
        self.detectButton_1.setObjectName(u"detectButton_1")
        self.detectButton_1.setMinimumSize(QSize(150, 30))
        self.detectButton_1.setMaximumSize(QSize(150, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.detectButton_1.setFont(font1)
        self.detectButton_1.setLayoutDirection(Qt.LeftToRight)
        self.detectButton_1.setAutoFillBackground(False)
        self.detectButton_1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(214, 214, 214);\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(85, 255, 255);\n"
"	border:none;\n"
"	border-radius:8px\n"
"}")

        self.verticalLayout.addWidget(self.detectButton_1, 0, Qt.AlignHCenter)

        self.detectButton_2 = QPushButton(self.centralwidget)
        self.detectButton_2.setObjectName(u"detectButton_2")
        self.detectButton_2.setMinimumSize(QSize(150, 30))
        self.detectButton_2.setMaximumSize(QSize(150, 16777215))
        self.detectButton_2.setFont(font1)
        self.detectButton_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(214, 214, 214);\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(85, 255, 255);\n"
"	border:none;\n"
"	border-radius:8px\n"
"}")

        self.verticalLayout.addWidget(self.detectButton_2, 0, Qt.AlignHCenter)

        self.detectButton_3 = QPushButton(self.centralwidget)
        self.detectButton_3.setObjectName(u"detectButton_3")
        self.detectButton_3.setMinimumSize(QSize(150, 30))
        self.detectButton_3.setMaximumSize(QSize(150, 16777215))
        self.detectButton_3.setFont(font1)
        self.detectButton_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(214, 214, 214);\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(85, 255, 255);\n"
"	border:none;\n"
"	border-radius:8px\n"
"}")

        self.verticalLayout.addWidget(self.detectButton_3, 0, Qt.AlignHCenter)

        self.detectButton_4 = QPushButton(self.centralwidget)
        self.detectButton_4.setObjectName(u"detectButton_4")
        self.detectButton_4.setMinimumSize(QSize(150, 30))
        self.detectButton_4.setMaximumSize(QSize(150, 16777215))
        self.detectButton_4.setFont(font1)
        self.detectButton_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	\n"
"	background-color: rgb(214, 214, 214);\n"
"	border:none;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(85, 255, 255);\n"
"	border:none;\n"
"	border-radius:8px\n"
"}")
        self.detectButton_4.setFlat(False)

        self.verticalLayout.addWidget(self.detectButton_4, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 120, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        font2 = QFont()
        font2.setPointSize(12)
        self.tableView.setFont(font2)
        self.tableView.setStyleSheet(u"background:rgb(255,255,255)")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setTextElideMode(Qt.ElideNone)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setVisible(False)
        self.tableView.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tableView)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 20))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.detectButton_1.clicked.connect(MainWindow.detect_single)
        self.detectButton_2.clicked.connect(MainWindow.result_save)
        self.detectButton_3.clicked.connect(MainWindow.detect_folder)
        self.detectButton_4.clicked.connect(MainWindow.modify_path)
        self.tableView.clicked.connect(MainWindow.show_result)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Detector", None))
#if QT_CONFIG(tooltip)
        self.detectButton_1.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.detectButton_1.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.detectButton_1.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.detectButton_1.setText(QCoreApplication.translate("MainWindow", u"Detect Single Image", None))
        self.detectButton_2.setText(QCoreApplication.translate("MainWindow", u"Save Single Image", None))
        self.detectButton_3.setText(QCoreApplication.translate("MainWindow", u"Detect Folder", None))
        self.detectButton_4.setText(QCoreApplication.translate("MainWindow", u"Modify Path", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Detection Result Information", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Original Image", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Detection Result Image", None))
    # retranslateUi

