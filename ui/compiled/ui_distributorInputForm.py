# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'productInputFormCcNnqY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(393, 640)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_4 = QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.textId = QPlainTextEdit(self.frame_4)
        self.textId.setObjectName(u"textId")

        self.verticalLayout_2.addWidget(self.textId)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.textSale = QPlainTextEdit(self.frame_4)
        self.textSale.setObjectName(u"textSale")

        self.verticalLayout_2.addWidget(self.textSale)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.textDate = QDateEdit(self.frame_4)
        self.textDate.setObjectName(u"textDate")

        self.verticalLayout_2.addWidget(self.textDate)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.textNombre = QPlainTextEdit(self.frame_4)
        self.textNombre.setObjectName(u"textNombre")

        self.verticalLayout_2.addWidget(self.textNombre)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.textTel = QPlainTextEdit(self.frame_4)
        self.textTel.setObjectName(u"textTel")

        self.verticalLayout_2.addWidget(self.textTel)


        self.verticalLayout_3.addWidget(self.frame_4)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btnCancel = QPushButton(self.widget_2)
        self.btnCancel.setObjectName(u"btnCancel")

        self.horizontalLayout.addWidget(self.btnCancel)

        self.btnOk = QPushButton(self.widget_2)
        self.btnOk.setObjectName(u"btnOk")

        self.horizontalLayout.addWidget(self.btnOk)


        self.verticalLayout.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Id", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Venta", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Cliente desde", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Numero Telefonico", None))
        self.btnCancel.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.btnOk.setText(QCoreApplication.translate("Form", u"OK", None))
    # retranslateUi
