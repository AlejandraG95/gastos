# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gastos_final.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDateEdit,
    QDateTimeEdit, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(420, 547)
        Form.setStyleSheet(u"QPushButton{\n"
"background-color: #57b1e6;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(34, 110, 172);\n"
"	\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(Form)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"QFrame{\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.background_frame.setFrameShape(QFrame.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        font = QFont()
        font.setPointSize(13)
        self.content_frame.setFont(font)
        self.content_frame.setFrameShape(QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.img_pushButton = QPushButton(self.content_frame)
        self.img_pushButton.setObjectName(u"img_pushButton")
        self.img_pushButton.setStyleSheet(u"background-color: transparent")
        icon = QIcon()
        icon.addFile(u":/iconos/assets/iconos/ambienteslogo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.img_pushButton.setIcon(icon)
        self.img_pushButton.setIconSize(QSize(135, 135))

        self.verticalLayout_3.addWidget(self.img_pushButton)

        self.titulo_label = QLabel(self.content_frame)
        self.titulo_label.setObjectName(u"titulo_label")
        font1 = QFont()
        font1.setFamilies([u"Myanmar Text 12"])
        font1.setPointSize(27)
        font1.setBold(False)
        font1.setItalic(False)
        self.titulo_label.setFont(font1)
        self.titulo_label.setLayoutDirection(Qt.LeftToRight)
        self.titulo_label.setStyleSheet(u"font:  27pt \"Myanmar Text\" bold;\n"
"color: #00003d;")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setMargin(-3)
        self.titulo_label.setIndent(-1)

        self.verticalLayout_3.addWidget(self.titulo_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fecha_i_dateEdit = QDateEdit(self.content_frame)
        self.fecha_i_dateEdit.setObjectName(u"fecha_i_dateEdit")
        font2 = QFont()
        font2.setPointSize(12)
        self.fecha_i_dateEdit.setFont(font2)
        self.fecha_i_dateEdit.setWrapping(False)
        self.fecha_i_dateEdit.setFrame(True)
        self.fecha_i_dateEdit.setCalendarPopup(True)
        self.fecha_i_dateEdit.setTimeSpec(Qt.LocalTime)
        self.fecha_i_dateEdit.setDate(QDate(2024, 1, 1))

        self.horizontalLayout.addWidget(self.fecha_i_dateEdit)

        self.fecha_f_dateEdit = QDateEdit(self.content_frame)
        self.fecha_f_dateEdit.setObjectName(u"fecha_f_dateEdit")
        self.fecha_f_dateEdit.setFont(font2)
        self.fecha_f_dateEdit.setStyleSheet(u"")
        self.fecha_f_dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.fecha_f_dateEdit.setCalendarPopup(True)
        self.fecha_f_dateEdit.setDate(QDate(2024, 12, 31))

        self.horizontalLayout.addWidget(self.fecha_f_dateEdit)

        self.buscar_pushButton = QPushButton(self.content_frame)
        self.buscar_pushButton.setObjectName(u"buscar_pushButton")
        self.buscar_pushButton.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u":/iconos/assets/iconos/lupa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.buscar_pushButton.setIcon(icon1)
        self.buscar_pushButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.buscar_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.registro_gastos_tableWidget = QTableWidget(self.content_frame)
        if (self.registro_gastos_tableWidget.columnCount() < 7):
            self.registro_gastos_tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.registro_gastos_tableWidget.rowCount() < 3):
            self.registro_gastos_tableWidget.setRowCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(0, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(0, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(0, 3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(1, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(2, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(2, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(2, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.registro_gastos_tableWidget.setItem(2, 3, __qtablewidgetitem21)
        self.registro_gastos_tableWidget.setObjectName(u"registro_gastos_tableWidget")
        self.registro_gastos_tableWidget.setAutoFillBackground(False)
        self.registro_gastos_tableWidget.setStyleSheet(u"header:\n"
"(background-color: rgb(50, 156, 248);)")
        self.registro_gastos_tableWidget.setFrameShape(QFrame.StyledPanel)
        self.registro_gastos_tableWidget.setFrameShadow(QFrame.Sunken)
        self.registro_gastos_tableWidget.setLineWidth(4)
        self.registro_gastos_tableWidget.setMidLineWidth(2)
        self.registro_gastos_tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.registro_gastos_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.registro_gastos_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.registro_gastos_tableWidget.setAutoScroll(True)
        self.registro_gastos_tableWidget.setTabKeyNavigation(True)
        self.registro_gastos_tableWidget.setDragEnabled(True)
        self.registro_gastos_tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.registro_gastos_tableWidget.setAlternatingRowColors(True)
        self.registro_gastos_tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.registro_gastos_tableWidget.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.registro_gastos_tableWidget.setTextElideMode(Qt.ElideRight)
        self.registro_gastos_tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.registro_gastos_tableWidget.setGridStyle(Qt.DashLine)
        self.registro_gastos_tableWidget.setSortingEnabled(False)
        self.registro_gastos_tableWidget.setCornerButtonEnabled(True)
        self.registro_gastos_tableWidget.horizontalHeader().setVisible(True)
        self.registro_gastos_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.registro_gastos_tableWidget.horizontalHeader().setMinimumSectionSize(36)
        self.registro_gastos_tableWidget.horizontalHeader().setDefaultSectionSize(121)
        self.registro_gastos_tableWidget.horizontalHeader().setHighlightSections(True)
        self.registro_gastos_tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.registro_gastos_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.registro_gastos_tableWidget.verticalHeader().setVisible(False)
        self.registro_gastos_tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.registro_gastos_tableWidget.verticalHeader().setHighlightSections(True)
        self.registro_gastos_tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.registro_gastos_tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.registro_gastos_tableWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 6, 3, 6)
        self.txt_label = QLabel(self.content_frame)
        self.txt_label.setObjectName(u"txt_label")
        self.txt_label.setStyleSheet(u"font:  12pt \"Myanmar Text\" bold;\n"
"color: #00003d;")

        self.horizontalLayout_3.addWidget(self.txt_label)

        self.resultado_label = QLabel(self.content_frame)
        self.resultado_label.setObjectName(u"resultado_label")
        font3 = QFont()
        font3.setPointSize(11)
        self.resultado_label.setFont(font3)
        self.resultado_label.setLayoutDirection(Qt.LeftToRight)
        self.resultado_label.setAutoFillBackground(False)
        self.resultado_label.setStyleSheet(u"QLabel{\n"
"background-color: transparent;\n"
"color:black;\n"
"border: 1px solid  rgb(34, 110, 172); \n"
"border-radius: 5px;\n"
"	background-color: rgb(255, 255, 255)\n"
"}\n"
"")
        self.resultado_label.setScaledContents(False)
        self.resultado_label.setAlignment(Qt.AlignCenter)
        self.resultado_label.setWordWrap(False)
        self.resultado_label.setMargin(0)
        self.resultado_label.setIndent(-1)
        self.resultado_label.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.resultado_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.calcular_pushButton = QPushButton(self.content_frame)
        self.calcular_pushButton.setObjectName(u"calcular_pushButton")
        self.calcular_pushButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/iconos/assets/iconos/ok.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calcular_pushButton.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.calcular_pushButton)

        self.imprimir_pushButton = QPushButton(self.content_frame)
        self.imprimir_pushButton.setObjectName(u"imprimir_pushButton")
        self.imprimir_pushButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/iconos/assets/iconos/printer_15827856.png", QSize(), QIcon.Normal, QIcon.Off)
        self.imprimir_pushButton.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.imprimir_pushButton)

        self.cancelar_pushButton = QPushButton(self.content_frame)
        self.cancelar_pushButton.setObjectName(u"cancelar_pushButton")
        self.cancelar_pushButton.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u":/iconos/assets/iconos/cancelar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelar_pushButton.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.cancelar_pushButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.content_frame)


        self.verticalLayout.addWidget(self.background_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.img_pushButton.setText("")
        self.titulo_label.setText(QCoreApplication.translate("Form", u"GASTOS", None))
        self.fecha_i_dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.fecha_f_dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"dd/MM/yyyy", None))
        self.buscar_pushButton.setText(QCoreApplication.translate("Form", u"Buscar", None))
        ___qtablewidgetitem = self.registro_gastos_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.registro_gastos_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"fecha", None));
        ___qtablewidgetitem2 = self.registro_gastos_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"cajero", None));
        ___qtablewidgetitem3 = self.registro_gastos_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"concepto", None));
        ___qtablewidgetitem4 = self.registro_gastos_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"valor", None));
        ___qtablewidgetitem5 = self.registro_gastos_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"tipo", None));
        ___qtablewidgetitem6 = self.registro_gastos_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"liquidacion", None));

        __sortingEnabled = self.registro_gastos_tableWidget.isSortingEnabled()
        self.registro_gastos_tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem7 = self.registro_gastos_tableWidget.item(0, 0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"1", None));
        ___qtablewidgetitem8 = self.registro_gastos_tableWidget.item(0, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"andrea", None));
        ___qtablewidgetitem9 = self.registro_gastos_tableWidget.item(0, 3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"bbb", None));
        ___qtablewidgetitem10 = self.registro_gastos_tableWidget.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"2", None));
        ___qtablewidgetitem11 = self.registro_gastos_tableWidget.item(1, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"maria", None));
        ___qtablewidgetitem12 = self.registro_gastos_tableWidget.item(1, 3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"bvbv", None));
        ___qtablewidgetitem13 = self.registro_gastos_tableWidget.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"3", None));
        ___qtablewidgetitem14 = self.registro_gastos_tableWidget.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"juan", None));
        ___qtablewidgetitem15 = self.registro_gastos_tableWidget.item(2, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"df", None));
        self.registro_gastos_tableWidget.setSortingEnabled(__sortingEnabled)

        self.txt_label.setText(QCoreApplication.translate("Form", u"Total de Gastos:", None))
        self.resultado_label.setText(QCoreApplication.translate("Form", u"0", None))
        self.calcular_pushButton.setText(QCoreApplication.translate("Form", u"CALCULAR", None))
        self.imprimir_pushButton.setText(QCoreApplication.translate("Form", u"IMPRMIR", None))
        self.cancelar_pushButton.setText(QCoreApplication.translate("Form", u"CANCELAR", None))
    # retranslateUi

