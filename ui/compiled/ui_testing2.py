# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test2SOWkfK.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
from . import src_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(868, 593)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.img_Logo = QLabel(self.frame_2)
        self.img_Logo.setObjectName(u"img_Logo")
        self.img_Logo.setStyleSheet(u"image: url(:/icons/assets/Logo.png);")

        self.horizontalLayout_6.addWidget(self.img_Logo)

        self.widget_4 = QWidget(self.frame_2)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_2 = QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbUser = QLabel(self.widget_4)
        self.lbUser.setObjectName(u"lbUser")

        self.verticalLayout_2.addWidget(self.lbUser)

        self.lbCompany = QLabel(self.widget_4)
        self.lbCompany.setObjectName(u"lbCompany")

        self.verticalLayout_2.addWidget(self.lbCompany)


        self.horizontalLayout_6.addWidget(self.widget_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.btnProvider = QPushButton(self.widget)
        self.btnProvider.setObjectName(u"btnProvider")

        self.verticalLayout.addWidget(self.btnProvider)

        self.btnMaterial = QPushButton(self.widget)
        self.btnMaterial.setObjectName(u"btnMaterial")

        self.verticalLayout.addWidget(self.btnMaterial)

        self.btnPurchase = QPushButton(self.widget)
        self.btnPurchase.setObjectName(u"btnPurchase")

        self.verticalLayout.addWidget(self.btnPurchase)

        self.btnDistributor = QPushButton(self.widget)
        self.btnDistributor.setObjectName(u"btnDistributor")

        self.verticalLayout.addWidget(self.btnDistributor)

        self.btnSales = QPushButton(self.widget)
        self.btnSales.setObjectName(u"btnSales")

        self.verticalLayout.addWidget(self.btnSales)

        self.btnLote = QPushButton(self.widget)
        self.btnLote.setObjectName(u"btnLote")

        self.verticalLayout.addWidget(self.btnLote)

        self.btnEmployee = QPushButton(self.widget)
        self.btnEmployee.setObjectName(u"btnEmployee")

        self.verticalLayout.addWidget(self.btnEmployee)

        self.btnTitle = QPushButton(self.widget)
        self.btnTitle.setObjectName(u"btnTitle")

        self.verticalLayout.addWidget(self.btnTitle)

        self.btnDepartment = QPushButton(self.widget)
        self.btnDepartment.setObjectName(u"btnDepartment")

        self.verticalLayout.addWidget(self.btnDepartment)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.btnLogOut = QPushButton(self.widget_3)
        self.btnLogOut.setObjectName(u"btnLogOut")

        self.horizontalLayout_5.addWidget(self.btnLogOut)

        self.btnClose = QPushButton(self.widget_3)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_5.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout_2.addWidget(self.widget)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stacked1Contenido = QStackedWidget(self.frame_3)
        self.stacked1Contenido.setObjectName(u"stacked1Contenido")
        self.tbProvider = QWidget()
        self.tbProvider.setObjectName(u"tbProvider")
        self.verticalLayout_3 = QVBoxLayout(self.tbProvider)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_2 = QWidget(self.tbProvider)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget_2)

        self.tableProvider = QTableWidget(self.tbProvider)
        if (self.tableProvider.columnCount() < 5):
            self.tableProvider.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProvider.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableProvider.setObjectName(u"tableProvider")
        self.tableProvider.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.tableProvider)

        self.stacked1Contenido.addWidget(self.tbProvider)
        self.tbClient = QWidget()
        self.tbClient.setObjectName(u"tbClient")
        self.verticalLayout_5 = QVBoxLayout(self.tbClient)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_6 = QWidget(self.tbClient)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.widget_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.tableMaterial = QTableWidget(self.tbClient)
        if (self.tableMaterial.columnCount() < 6):
            self.tableMaterial.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableMaterial.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        if (self.tableMaterial.rowCount() < 1):
            self.tableMaterial.setRowCount(1)
        self.tableMaterial.setObjectName(u"tableMaterial")
        self.tableMaterial.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableMaterial.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableMaterial.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableMaterial.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableMaterial.setGridStyle(Qt.SolidLine)
        self.tableMaterial.horizontalHeader().setCascadingSectionResizes(False)
        self.tableMaterial.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableMaterial.horizontalHeader().setStretchLastSection(True)
        self.tableMaterial.verticalHeader().setCascadingSectionResizes(False)
        self.tableMaterial.verticalHeader().setProperty("showSortIndicator", False)
        self.tableMaterial.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_5.addWidget(self.tableMaterial)

        self.stacked1Contenido.addWidget(self.tbClient)
        self.tbProduct = QWidget()
        self.tbProduct.setObjectName(u"tbProduct")
        self.verticalLayout_6 = QVBoxLayout(self.tbProduct)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget_8 = QWidget(self.tbProduct)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.widget_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_3)


        self.verticalLayout_6.addWidget(self.widget_8)

        self.tablePurchase = QTableWidget(self.tbProduct)
        if (self.tablePurchase.columnCount() < 5):
            self.tablePurchase.setColumnCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tablePurchase.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tablePurchase.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tablePurchase.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tablePurchase.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tablePurchase.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        self.tablePurchase.setObjectName(u"tablePurchase")
        self.tablePurchase.setAutoFillBackground(False)
        self.tablePurchase.setAlternatingRowColors(False)
        self.tablePurchase.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tablePurchase.horizontalHeader().setProperty("showSortIndicator", False)
        self.tablePurchase.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.tablePurchase)

        self.stacked1Contenido.addWidget(self.tbProduct)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget_9 = QWidget(self.page)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_10 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.stacked1Contenido_2 = QStackedWidget(self.page)
        self.stacked1Contenido_2.setObjectName(u"stacked1Contenido_2")
        self.stacked1Contenido_2.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_3 = QWidget()
        self.tbProvider_3.setObjectName(u"tbProvider_3")
        self.verticalLayout_10 = QVBoxLayout(self.tbProvider_3)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.widget_13 = QWidget(self.tbProvider_3)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.widget_13)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.horizontalLayout_14.addWidget(self.label_7)


        self.verticalLayout_10.addWidget(self.widget_13)

        self.tableProvider_3 = QTableWidget(self.tbProvider_3)
        if (self.tableProvider_3.columnCount() < 5):
            self.tableProvider_3.setColumnCount(5)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableProvider_3.setHorizontalHeaderItem(4, __qtablewidgetitem20)
        self.tableProvider_3.setObjectName(u"tableProvider_3")
        self.tableProvider_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_3.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_10.addWidget(self.tableProvider_3)

        self.stacked1Contenido_2.addWidget(self.tbProvider_3)
        self.tbClient_3 = QWidget()
        self.tbClient_3.setObjectName(u"tbClient_3")
        self.verticalLayout_11 = QVBoxLayout(self.tbClient_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget_14 = QWidget(self.tbClient_3)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_8 = QLabel(self.widget_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_15.addWidget(self.label_8)


        self.verticalLayout_11.addWidget(self.widget_14)

        self.tableClient_3 = QTableWidget(self.tbClient_3)
        if (self.tableClient_3.columnCount() < 6):
            self.tableClient_3.setColumnCount(6)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableClient_3.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        if (self.tableClient_3.rowCount() < 1):
            self.tableClient_3.setRowCount(1)
        self.tableClient_3.setObjectName(u"tableClient_3")
        self.tableClient_3.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_3.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_3.setGridStyle(Qt.SolidLine)
        self.tableClient_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_3.horizontalHeader().setStretchLastSection(True)
        self.tableClient_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_3.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_11.addWidget(self.tableClient_3)

        self.stacked1Contenido_2.addWidget(self.tbClient_3)
        self.tbProduct_3 = QWidget()
        self.tbProduct_3.setObjectName(u"tbProduct_3")
        self.verticalLayout_12 = QVBoxLayout(self.tbProduct_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_15 = QWidget(self.tbProduct_3)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_16 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_9 = QLabel(self.widget_15)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.horizontalLayout_16.addWidget(self.label_9)


        self.verticalLayout_12.addWidget(self.widget_15)

        self.tableDistributor = QTableWidget(self.tbProduct_3)
        if (self.tableDistributor.columnCount() < 5):
            self.tableDistributor.setColumnCount(5)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableDistributor.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableDistributor.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableDistributor.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableDistributor.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableDistributor.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        self.tableDistributor.setObjectName(u"tableDistributor")
        self.tableDistributor.setAutoFillBackground(False)
        self.tableDistributor.setAlternatingRowColors(False)
        self.tableDistributor.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDistributor.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableDistributor.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_12.addWidget(self.tableDistributor)

        self.stacked1Contenido_2.addWidget(self.tbProduct_3)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.widget_16 = QWidget(self.page_3)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.stacked1Contenido_2.addWidget(self.page_3)
        self.stacked1Contenido.addWidget(self.page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stacked1Contenido_3 = QStackedWidget(self.page_4)
        self.stacked1Contenido_3.setObjectName(u"stacked1Contenido_3")
        self.stacked1Contenido_3.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_4 = QWidget()
        self.tbProvider_4.setObjectName(u"tbProvider_4")
        self.verticalLayout_13 = QVBoxLayout(self.tbProvider_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.widget_17 = QWidget(self.tbProvider_4)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_18 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_10 = QLabel(self.widget_17)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_18.addWidget(self.label_10)


        self.verticalLayout_13.addWidget(self.widget_17)

        self.tableProvider_4 = QTableWidget(self.tbProvider_4)
        if (self.tableProvider_4.columnCount() < 5):
            self.tableProvider_4.setColumnCount(5)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(1, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(2, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(3, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableProvider_4.setHorizontalHeaderItem(4, __qtablewidgetitem36)
        self.tableProvider_4.setObjectName(u"tableProvider_4")
        self.tableProvider_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_4.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_13.addWidget(self.tableProvider_4)

        self.stacked1Contenido_3.addWidget(self.tbProvider_4)
        self.tbClient_4 = QWidget()
        self.tbClient_4.setObjectName(u"tbClient_4")
        self.verticalLayout_14 = QVBoxLayout(self.tbClient_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget_18 = QWidget(self.tbClient_4)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_19 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_11 = QLabel(self.widget_18)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_19.addWidget(self.label_11)


        self.verticalLayout_14.addWidget(self.widget_18)

        self.tableClient_4 = QTableWidget(self.tbClient_4)
        if (self.tableClient_4.columnCount() < 6):
            self.tableClient_4.setColumnCount(6)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableClient_4.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        if (self.tableClient_4.rowCount() < 1):
            self.tableClient_4.setRowCount(1)
        self.tableClient_4.setObjectName(u"tableClient_4")
        self.tableClient_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_4.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_4.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_4.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_4.setGridStyle(Qt.SolidLine)
        self.tableClient_4.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_4.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_4.horizontalHeader().setStretchLastSection(True)
        self.tableClient_4.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_4.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_4.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.tableClient_4)

        self.stacked1Contenido_3.addWidget(self.tbClient_4)
        self.tbProduct_4 = QWidget()
        self.tbProduct_4.setObjectName(u"tbProduct_4")
        self.verticalLayout_15 = QVBoxLayout(self.tbProduct_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_19 = QWidget(self.tbProduct_4)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_12 = QLabel(self.widget_19)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.horizontalLayout_20.addWidget(self.label_12)


        self.verticalLayout_15.addWidget(self.widget_19)

        self.tableSales = QTableWidget(self.tbProduct_4)
        if (self.tableSales.columnCount() < 6):
            self.tableSales.setColumnCount(6)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        self.tableSales.setObjectName(u"tableSales")
        self.tableSales.setAutoFillBackground(False)
        self.tableSales.setAlternatingRowColors(False)
        self.tableSales.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSales.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableSales.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_15.addWidget(self.tableSales)

        self.stacked1Contenido_3.addWidget(self.tbProduct_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.widget_20 = QWidget(self.page_5)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_21 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.stacked1Contenido_3.addWidget(self.page_5)
        self.stacked1Contenido.addWidget(self.page_4)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.stacked1Contenido_4 = QStackedWidget(self.page_6)
        self.stacked1Contenido_4.setObjectName(u"stacked1Contenido_4")
        self.stacked1Contenido_4.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_5 = QWidget()
        self.tbProvider_5.setObjectName(u"tbProvider_5")
        self.verticalLayout_16 = QVBoxLayout(self.tbProvider_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.widget_21 = QWidget(self.tbProvider_5)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_22 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_13 = QLabel(self.widget_21)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)

        self.horizontalLayout_22.addWidget(self.label_13)


        self.verticalLayout_16.addWidget(self.widget_21)

        self.tableProvider_5 = QTableWidget(self.tbProvider_5)
        if (self.tableProvider_5.columnCount() < 5):
            self.tableProvider_5.setColumnCount(5)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableProvider_5.setHorizontalHeaderItem(4, __qtablewidgetitem53)
        self.tableProvider_5.setObjectName(u"tableProvider_5")
        self.tableProvider_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_5.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_16.addWidget(self.tableProvider_5)

        self.stacked1Contenido_4.addWidget(self.tbProvider_5)
        self.tbClient_5 = QWidget()
        self.tbClient_5.setObjectName(u"tbClient_5")
        self.verticalLayout_17 = QVBoxLayout(self.tbClient_5)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_22 = QWidget(self.tbClient_5)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_23 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_14 = QLabel(self.widget_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.horizontalLayout_23.addWidget(self.label_14)


        self.verticalLayout_17.addWidget(self.widget_22)

        self.tableClient_5 = QTableWidget(self.tbClient_5)
        if (self.tableClient_5.columnCount() < 6):
            self.tableClient_5.setColumnCount(6)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(4, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableClient_5.setHorizontalHeaderItem(5, __qtablewidgetitem59)
        if (self.tableClient_5.rowCount() < 1):
            self.tableClient_5.setRowCount(1)
        self.tableClient_5.setObjectName(u"tableClient_5")
        self.tableClient_5.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_5.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_5.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_5.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_5.setGridStyle(Qt.SolidLine)
        self.tableClient_5.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_5.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_5.horizontalHeader().setStretchLastSection(True)
        self.tableClient_5.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_5.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_5.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_17.addWidget(self.tableClient_5)

        self.stacked1Contenido_4.addWidget(self.tbClient_5)
        self.tbProduct_5 = QWidget()
        self.tbProduct_5.setObjectName(u"tbProduct_5")
        self.verticalLayout_18 = QVBoxLayout(self.tbProduct_5)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_23 = QWidget(self.tbProduct_5)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_15 = QLabel(self.widget_23)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font)

        self.horizontalLayout_24.addWidget(self.label_15)


        self.verticalLayout_18.addWidget(self.widget_23)

        self.tableLote = QTableWidget(self.tbProduct_5)
        if (self.tableLote.columnCount() < 3):
            self.tableLote.setColumnCount(3)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableLote.setHorizontalHeaderItem(0, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tableLote.setHorizontalHeaderItem(1, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableLote.setHorizontalHeaderItem(2, __qtablewidgetitem62)
        self.tableLote.setObjectName(u"tableLote")
        self.tableLote.setAutoFillBackground(False)
        self.tableLote.setAlternatingRowColors(False)
        self.tableLote.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableLote.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableLote.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_18.addWidget(self.tableLote)

        self.stacked1Contenido_4.addWidget(self.tbProduct_5)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.widget_24 = QWidget(self.page_7)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_25 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.stacked1Contenido_4.addWidget(self.page_7)
        self.stacked1Contenido.addWidget(self.page_6)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.stacked1Contenido_5 = QStackedWidget(self.page_8)
        self.stacked1Contenido_5.setObjectName(u"stacked1Contenido_5")
        self.stacked1Contenido_5.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_7 = QWidget()
        self.tbProvider_7.setObjectName(u"tbProvider_7")
        self.verticalLayout_22 = QVBoxLayout(self.tbProvider_7)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.widget_29 = QWidget(self.tbProvider_7)
        self.widget_29.setObjectName(u"widget_29")
        self.horizontalLayout_30 = QHBoxLayout(self.widget_29)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_19 = QLabel(self.widget_29)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_19)


        self.verticalLayout_22.addWidget(self.widget_29)

        self.tableProvider_7 = QTableWidget(self.tbProvider_7)
        if (self.tableProvider_7.columnCount() < 5):
            self.tableProvider_7.setColumnCount(5)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableProvider_7.setHorizontalHeaderItem(0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableProvider_7.setHorizontalHeaderItem(1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableProvider_7.setHorizontalHeaderItem(2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableProvider_7.setHorizontalHeaderItem(3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableProvider_7.setHorizontalHeaderItem(4, __qtablewidgetitem67)
        self.tableProvider_7.setObjectName(u"tableProvider_7")
        self.tableProvider_7.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_7.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_22.addWidget(self.tableProvider_7)

        self.stacked1Contenido_5.addWidget(self.tbProvider_7)
        self.tbClient_7 = QWidget()
        self.tbClient_7.setObjectName(u"tbClient_7")
        self.verticalLayout_23 = QVBoxLayout(self.tbClient_7)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_30 = QWidget(self.tbClient_7)
        self.widget_30.setObjectName(u"widget_30")
        self.horizontalLayout_31 = QHBoxLayout(self.widget_30)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_20 = QLabel(self.widget_30)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)

        self.horizontalLayout_31.addWidget(self.label_20)


        self.verticalLayout_23.addWidget(self.widget_30)

        self.tableClient_7 = QTableWidget(self.tbClient_7)
        if (self.tableClient_7.columnCount() < 6):
            self.tableClient_7.setColumnCount(6)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(0, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(1, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(2, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(3, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(4, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableClient_7.setHorizontalHeaderItem(5, __qtablewidgetitem73)
        if (self.tableClient_7.rowCount() < 1):
            self.tableClient_7.setRowCount(1)
        self.tableClient_7.setObjectName(u"tableClient_7")
        self.tableClient_7.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_7.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_7.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_7.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_7.setGridStyle(Qt.SolidLine)
        self.tableClient_7.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_7.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_7.horizontalHeader().setStretchLastSection(True)
        self.tableClient_7.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_7.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_7.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_23.addWidget(self.tableClient_7)

        self.stacked1Contenido_5.addWidget(self.tbClient_7)
        self.tbProduct_7 = QWidget()
        self.tbProduct_7.setObjectName(u"tbProduct_7")
        self.verticalLayout_24 = QVBoxLayout(self.tbProduct_7)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.widget_31 = QWidget(self.tbProduct_7)
        self.widget_31.setObjectName(u"widget_31")
        self.horizontalLayout_32 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_21 = QLabel(self.widget_31)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.horizontalLayout_32.addWidget(self.label_21)


        self.verticalLayout_24.addWidget(self.widget_31)

        self.tableEmployee = QTableWidget(self.tbProduct_7)
        if (self.tableEmployee.columnCount() < 9):
            self.tableEmployee.setColumnCount(9)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(0, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(1, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(2, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(3, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(4, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(5, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(6, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(7, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableEmployee.setHorizontalHeaderItem(8, __qtablewidgetitem82)
        self.tableEmployee.setObjectName(u"tableEmployee")
        self.tableEmployee.setAutoFillBackground(False)
        self.tableEmployee.setAlternatingRowColors(False)
        self.tableEmployee.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableEmployee.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableEmployee.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_24.addWidget(self.tableEmployee)

        self.stacked1Contenido_5.addWidget(self.tbProduct_7)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.widget_32 = QWidget(self.page_10)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_33 = QHBoxLayout(self.widget_32)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.stacked1Contenido_5.addWidget(self.page_10)
        self.stacked1Contenido.addWidget(self.page_8)
        self.page_11 = QWidget()
        self.page_11.setObjectName(u"page_11")
        self.stacked1Contenido_6 = QStackedWidget(self.page_11)
        self.stacked1Contenido_6.setObjectName(u"stacked1Contenido_6")
        self.stacked1Contenido_6.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_8 = QWidget()
        self.tbProvider_8.setObjectName(u"tbProvider_8")
        self.verticalLayout_25 = QVBoxLayout(self.tbProvider_8)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.widget_33 = QWidget(self.tbProvider_8)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_34 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_22 = QLabel(self.widget_33)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)

        self.horizontalLayout_34.addWidget(self.label_22)


        self.verticalLayout_25.addWidget(self.widget_33)

        self.tableProvider_8 = QTableWidget(self.tbProvider_8)
        if (self.tableProvider_8.columnCount() < 5):
            self.tableProvider_8.setColumnCount(5)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableProvider_8.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableProvider_8.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableProvider_8.setHorizontalHeaderItem(2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableProvider_8.setHorizontalHeaderItem(3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableProvider_8.setHorizontalHeaderItem(4, __qtablewidgetitem87)
        self.tableProvider_8.setObjectName(u"tableProvider_8")
        self.tableProvider_8.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_8.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_25.addWidget(self.tableProvider_8)

        self.stacked1Contenido_6.addWidget(self.tbProvider_8)
        self.tbClient_8 = QWidget()
        self.tbClient_8.setObjectName(u"tbClient_8")
        self.verticalLayout_26 = QVBoxLayout(self.tbClient_8)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.widget_34 = QWidget(self.tbClient_8)
        self.widget_34.setObjectName(u"widget_34")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_23 = QLabel(self.widget_34)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.horizontalLayout_35.addWidget(self.label_23)


        self.verticalLayout_26.addWidget(self.widget_34)

        self.tableClient_8 = QTableWidget(self.tbClient_8)
        if (self.tableClient_8.columnCount() < 6):
            self.tableClient_8.setColumnCount(6)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(3, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(4, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableClient_8.setHorizontalHeaderItem(5, __qtablewidgetitem93)
        if (self.tableClient_8.rowCount() < 1):
            self.tableClient_8.setRowCount(1)
        self.tableClient_8.setObjectName(u"tableClient_8")
        self.tableClient_8.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_8.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_8.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_8.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_8.setGridStyle(Qt.SolidLine)
        self.tableClient_8.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_8.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_8.horizontalHeader().setStretchLastSection(True)
        self.tableClient_8.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_8.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_8.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_26.addWidget(self.tableClient_8)

        self.stacked1Contenido_6.addWidget(self.tbClient_8)
        self.tbProduct_8 = QWidget()
        self.tbProduct_8.setObjectName(u"tbProduct_8")
        self.verticalLayout_27 = QVBoxLayout(self.tbProduct_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.widget_35 = QWidget(self.tbProduct_8)
        self.widget_35.setObjectName(u"widget_35")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_35)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_24 = QLabel(self.widget_35)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)

        self.horizontalLayout_36.addWidget(self.label_24)


        self.verticalLayout_27.addWidget(self.widget_35)

        self.tableTitle = QTableWidget(self.tbProduct_8)
        if (self.tableTitle.columnCount() < 6):
            self.tableTitle.setColumnCount(6)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(0, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(1, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(2, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(3, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(4, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableTitle.setHorizontalHeaderItem(5, __qtablewidgetitem99)
        self.tableTitle.setObjectName(u"tableTitle")
        self.tableTitle.setAutoFillBackground(False)
        self.tableTitle.setAlternatingRowColors(False)
        self.tableTitle.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableTitle.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableTitle.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_27.addWidget(self.tableTitle)

        self.stacked1Contenido_6.addWidget(self.tbProduct_8)
        self.page_12 = QWidget()
        self.page_12.setObjectName(u"page_12")
        self.widget_36 = QWidget(self.page_12)
        self.widget_36.setObjectName(u"widget_36")
        self.widget_36.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_37 = QHBoxLayout(self.widget_36)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.stacked1Contenido_6.addWidget(self.page_12)
        self.stacked1Contenido.addWidget(self.page_11)
        self.page_13 = QWidget()
        self.page_13.setObjectName(u"page_13")
        self.stacked1Contenido_7 = QStackedWidget(self.page_13)
        self.stacked1Contenido_7.setObjectName(u"stacked1Contenido_7")
        self.stacked1Contenido_7.setGeometry(QRect(0, 0, 612, 487))
        self.tbProvider_9 = QWidget()
        self.tbProvider_9.setObjectName(u"tbProvider_9")
        self.verticalLayout_28 = QVBoxLayout(self.tbProvider_9)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.widget_37 = QWidget(self.tbProvider_9)
        self.widget_37.setObjectName(u"widget_37")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_37)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_25 = QLabel(self.widget_37)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.horizontalLayout_38.addWidget(self.label_25)


        self.verticalLayout_28.addWidget(self.widget_37)

        self.tableProvider_9 = QTableWidget(self.tbProvider_9)
        if (self.tableProvider_9.columnCount() < 5):
            self.tableProvider_9.setColumnCount(5)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableProvider_9.setHorizontalHeaderItem(0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableProvider_9.setHorizontalHeaderItem(1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableProvider_9.setHorizontalHeaderItem(2, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableProvider_9.setHorizontalHeaderItem(3, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableProvider_9.setHorizontalHeaderItem(4, __qtablewidgetitem104)
        self.tableProvider_9.setObjectName(u"tableProvider_9")
        self.tableProvider_9.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProvider_9.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_28.addWidget(self.tableProvider_9)

        self.stacked1Contenido_7.addWidget(self.tbProvider_9)
        self.tbClient_9 = QWidget()
        self.tbClient_9.setObjectName(u"tbClient_9")
        self.verticalLayout_29 = QVBoxLayout(self.tbClient_9)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.widget_38 = QWidget(self.tbClient_9)
        self.widget_38.setObjectName(u"widget_38")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_38)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_26 = QLabel(self.widget_38)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.horizontalLayout_39.addWidget(self.label_26)


        self.verticalLayout_29.addWidget(self.widget_38)

        self.tableClient_9 = QTableWidget(self.tbClient_9)
        if (self.tableClient_9.columnCount() < 6):
            self.tableClient_9.setColumnCount(6)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableClient_9.setHorizontalHeaderItem(5, __qtablewidgetitem110)
        if (self.tableClient_9.rowCount() < 1):
            self.tableClient_9.setRowCount(1)
        self.tableClient_9.setObjectName(u"tableClient_9")
        self.tableClient_9.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableClient_9.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableClient_9.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableClient_9.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tableClient_9.setGridStyle(Qt.SolidLine)
        self.tableClient_9.horizontalHeader().setCascadingSectionResizes(False)
        self.tableClient_9.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableClient_9.horizontalHeader().setStretchLastSection(True)
        self.tableClient_9.verticalHeader().setCascadingSectionResizes(False)
        self.tableClient_9.verticalHeader().setProperty("showSortIndicator", False)
        self.tableClient_9.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_29.addWidget(self.tableClient_9)

        self.stacked1Contenido_7.addWidget(self.tbClient_9)
        self.tbProduct_9 = QWidget()
        self.tbProduct_9.setObjectName(u"tbProduct_9")
        self.verticalLayout_30 = QVBoxLayout(self.tbProduct_9)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.widget_39 = QWidget(self.tbProduct_9)
        self.widget_39.setObjectName(u"widget_39")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_27 = QLabel(self.widget_39)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font)

        self.horizontalLayout_40.addWidget(self.label_27)


        self.verticalLayout_30.addWidget(self.widget_39)

        self.tableDepartment = QTableWidget(self.tbProduct_9)
        if (self.tableDepartment.columnCount() < 4):
            self.tableDepartment.setColumnCount(4)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableDepartment.setHorizontalHeaderItem(0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableDepartment.setHorizontalHeaderItem(1, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableDepartment.setHorizontalHeaderItem(2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableDepartment.setHorizontalHeaderItem(3, __qtablewidgetitem114)
        self.tableDepartment.setObjectName(u"tableDepartment")
        self.tableDepartment.setAutoFillBackground(False)
        self.tableDepartment.setAlternatingRowColors(False)
        self.tableDepartment.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableDepartment.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableDepartment.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_30.addWidget(self.tableDepartment)

        self.stacked1Contenido_7.addWidget(self.tbProduct_9)
        self.page_14 = QWidget()
        self.page_14.setObjectName(u"page_14")
        self.widget_40 = QWidget(self.page_14)
        self.widget_40.setObjectName(u"widget_40")
        self.widget_40.setGeometry(QRect(0, 40, 594, 40))
        self.horizontalLayout_41 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.stacked1Contenido_7.addWidget(self.page_14)
        self.stacked1Contenido.addWidget(self.page_13)

        self.verticalLayout_4.addWidget(self.stacked1Contenido)

        self.widget_5 = QWidget(self.frame_3)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.btnDeleteRow = QPushButton(self.widget_5)
        self.btnDeleteRow.setObjectName(u"btnDeleteRow")

        self.horizontalLayout_3.addWidget(self.btnDeleteRow)

        self.btnUpdateRow = QPushButton(self.widget_5)
        self.btnUpdateRow.setObjectName(u"btnUpdateRow")

        self.horizontalLayout_3.addWidget(self.btnUpdateRow)

        self.btnAdd = QPushButton(self.widget_5)
        self.btnAdd.setObjectName(u"btnAdd")

        self.horizontalLayout_3.addWidget(self.btnAdd)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addWidget(self.widget_5)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stacked1Contenido.setCurrentIndex(8)
        self.stacked1Contenido_2.setCurrentIndex(2)
        self.stacked1Contenido_3.setCurrentIndex(2)
        self.stacked1Contenido_4.setCurrentIndex(2)
        self.stacked1Contenido_5.setCurrentIndex(2)
        self.stacked1Contenido_6.setCurrentIndex(2)
        self.stacked1Contenido_7.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_Logo.setText("")
        self.lbUser.setText("")
        self.lbCompany.setText("")
        self.btnProvider.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.btnMaterial.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        self.btnPurchase.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        self.btnDistributor.setText(QCoreApplication.translate("MainWindow", u"Distribuidores", None))
        self.btnSales.setText(QCoreApplication.translate("MainWindow", u"Venta", None))
        self.btnLote.setText(QCoreApplication.translate("MainWindow", u"Lote", None))
        self.btnEmployee.setText(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.btnTitle.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        self.btnDepartment.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.btnLogOut.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem = self.tableProvider.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableProvider.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem2 = self.tableProvider.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem3 = self.tableProvider.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem4 = self.tableProvider.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem5 = self.tableMaterial.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tableMaterial.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem7 = self.tableMaterial.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Existencia", None));
        ___qtablewidgetitem8 = self.tableMaterial.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem9 = self.tableMaterial.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        ___qtablewidgetitem10 = self.tableMaterial.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        ___qtablewidgetitem11 = self.tablePurchase.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem12 = self.tablePurchase.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem13 = self.tablePurchase.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem14 = self.tablePurchase.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Costo", None));
        ___qtablewidgetitem15 = self.tablePurchase.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem16 = self.tableProvider_3.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem17 = self.tableProvider_3.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem18 = self.tableProvider_3.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem19 = self.tableProvider_3.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem20 = self.tableProvider_3.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem21 = self.tableClient_3.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem22 = self.tableClient_3.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem23 = self.tableClient_3.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem24 = self.tableClient_3.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem25 = self.tableClient_3.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem26 = self.tableClient_3.horizontalHeaderItem(5)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Distribuidores", None))
        ___qtablewidgetitem27 = self.tableDistributor.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem28 = self.tableDistributor.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Venta", None));
        ___qtablewidgetitem29 = self.tableDistributor.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Cliente desde", None));
        ___qtablewidgetitem30 = self.tableDistributor.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem31 = self.tableDistributor.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Numero de Telefono", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem32 = self.tableProvider_4.horizontalHeaderItem(0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem33 = self.tableProvider_4.horizontalHeaderItem(1)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem34 = self.tableProvider_4.horizontalHeaderItem(2)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem35 = self.tableProvider_4.horizontalHeaderItem(3)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem36 = self.tableProvider_4.horizontalHeaderItem(4)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem37 = self.tableClient_4.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem38 = self.tableClient_4.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem39 = self.tableClient_4.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem40 = self.tableClient_4.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem41 = self.tableClient_4.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem42 = self.tableClient_4.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Venta", None))
        ___qtablewidgetitem43 = self.tableSales.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem44 = self.tableSales.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem45 = self.tableSales.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem46 = self.tableSales.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Costo", None));
        ___qtablewidgetitem47 = self.tableSales.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Vendido en", None));
        ___qtablewidgetitem48 = self.tableSales.horizontalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Lote", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem49 = self.tableProvider_5.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem50 = self.tableProvider_5.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem51 = self.tableProvider_5.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem52 = self.tableProvider_5.horizontalHeaderItem(3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem53 = self.tableProvider_5.horizontalHeaderItem(4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem54 = self.tableClient_5.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem55 = self.tableClient_5.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem56 = self.tableClient_5.horizontalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem57 = self.tableClient_5.horizontalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem58 = self.tableClient_5.horizontalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem59 = self.tableClient_5.horizontalHeaderItem(5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Lote", None))
        ___qtablewidgetitem60 = self.tableLote.horizontalHeaderItem(0)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem61 = self.tableLote.horizontalHeaderItem(1)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None));
        ___qtablewidgetitem62 = self.tableLote.horizontalHeaderItem(2)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem63 = self.tableProvider_7.horizontalHeaderItem(0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem64 = self.tableProvider_7.horizontalHeaderItem(1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem65 = self.tableProvider_7.horizontalHeaderItem(2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem66 = self.tableProvider_7.horizontalHeaderItem(3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem67 = self.tableProvider_7.horizontalHeaderItem(4)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem68 = self.tableClient_7.horizontalHeaderItem(0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem69 = self.tableClient_7.horizontalHeaderItem(1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem70 = self.tableClient_7.horizontalHeaderItem(2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem71 = self.tableClient_7.horizontalHeaderItem(3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem72 = self.tableClient_7.horizontalHeaderItem(4)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem73 = self.tableClient_7.horizontalHeaderItem(5)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Empleado", None))
        ___qtablewidgetitem74 = self.tableEmployee.horizontalHeaderItem(0)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem75 = self.tableEmployee.horizontalHeaderItem(1)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Nombre(s)", None));
        ___qtablewidgetitem76 = self.tableEmployee.horizontalHeaderItem(2)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Apellidos", None));
        ___qtablewidgetitem77 = self.tableEmployee.horizontalHeaderItem(3)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Numero de Telefono", None));
        ___qtablewidgetitem78 = self.tableEmployee.horizontalHeaderItem(4)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Puesto", None));
        ___qtablewidgetitem79 = self.tableEmployee.horizontalHeaderItem(5)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Departamento", None));
        ___qtablewidgetitem80 = self.tableEmployee.horizontalHeaderItem(6)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Empleado por", None));
        ___qtablewidgetitem81 = self.tableEmployee.horizontalHeaderItem(7)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Sueldo", None));
        ___qtablewidgetitem82 = self.tableEmployee.horizontalHeaderItem(8)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem83 = self.tableProvider_8.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem84 = self.tableProvider_8.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem85 = self.tableProvider_8.horizontalHeaderItem(2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem86 = self.tableProvider_8.horizontalHeaderItem(3)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem87 = self.tableProvider_8.horizontalHeaderItem(4)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem88 = self.tableClient_8.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem89 = self.tableClient_8.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem90 = self.tableClient_8.horizontalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem91 = self.tableClient_8.horizontalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem92 = self.tableClient_8.horizontalHeaderItem(4)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem93 = self.tableClient_8.horizontalHeaderItem(5)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Cargo", None))
        ___qtablewidgetitem94 = self.tableTitle.horizontalHeaderItem(0)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem95 = self.tableTitle.horizontalHeaderItem(1)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem96 = self.tableTitle.horizontalHeaderItem(2)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u" Nombre", None));
        ___qtablewidgetitem97 = self.tableTitle.horizontalHeaderItem(3)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Sueldo Base", None));
        ___qtablewidgetitem98 = self.tableTitle.horizontalHeaderItem(4)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Hora de entrada", None));
        ___qtablewidgetitem99 = self.tableTitle.horizontalHeaderItem(5)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Hora de Salida", None));
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        ___qtablewidgetitem100 = self.tableProvider_9.horizontalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem101 = self.tableProvider_9.horizontalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem102 = self.tableProvider_9.horizontalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Material", None));
        ___qtablewidgetitem103 = self.tableProvider_9.horizontalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Telefono", None));
        ___qtablewidgetitem104 = self.tableProvider_9.horizontalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Materiales", None))
        ___qtablewidgetitem105 = self.tableClient_9.horizontalHeaderItem(0)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem106 = self.tableClient_9.horizontalHeaderItem(1)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem107 = self.tableClient_9.horizontalHeaderItem(2)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem108 = self.tableClient_9.horizontalHeaderItem(3)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Historial combinaciones", None));
        ___qtablewidgetitem109 = self.tableClient_9.horizontalHeaderItem(4)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Pzs/Lote", None));
        ___qtablewidgetitem110 = self.tableClient_9.horizontalHeaderItem(5)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Ultima Compra", None));
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        ___qtablewidgetitem111 = self.tableDepartment.horizontalHeaderItem(0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem112 = self.tableDepartment.horizontalHeaderItem(1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Gerente", None));
        ___qtablewidgetitem113 = self.tableDepartment.horizontalHeaderItem(2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem114 = self.tableDepartment.horizontalHeaderItem(3)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        self.btnDeleteRow.setText(QCoreApplication.translate("MainWindow", u"Borrar", None))
        self.btnUpdateRow.setText(QCoreApplication.translate("MainWindow", u"Actualizar", None))
        self.btnAdd.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
    # retranslateUi

