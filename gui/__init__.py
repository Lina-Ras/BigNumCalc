from PyQt5 import QtCore, QtGui, QtWidgets

class Colors():
    Q_neutralLight = QtGui.QColor(240, 234, 210)
    Q_FcolorLight = QtGui.QColor(213, 223, 165)
    Q_FcolorMain = QtGui.QColor(173, 193, 120)
    Q_ScolorMain = QtGui.QColor(169, 132, 103)
    Q_ScolorDark = QtGui.QColor(60, 30, 14)

    neutralLight = f'rgb({Q_neutralLight.red()}, {Q_neutralLight.green()}, {Q_neutralLight.blue()})'
    FcolorLight = f'rgb({Q_FcolorLight.red()}, {Q_FcolorLight.green()}, {Q_FcolorLight.blue()})'
    FcolorMain = f'rgb({Q_FcolorMain.red()}, {Q_FcolorMain.green()}, {Q_FcolorMain.blue()})'
    ScolorMain = f'rgb({Q_ScolorMain.red()}, {Q_ScolorMain.green()}, {Q_ScolorMain.blue()})'
    ScolorDark = f'rgb({Q_ScolorDark.red()}, {Q_ScolorDark.green()}, {Q_ScolorDark.blue()})'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(f'background-color: {Colors.ScolorMain};')
        MainWindow.resize(800, 478)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(24)

        regex = QtCore.QRegExp(
            "[-]?([0][,.][0-9]{,6}|[1][0]{12}[.,][0]{,6}|[1-9][0-9]{,11}[,.][0-9]{,6})")
        validator = QtGui.QRegExpValidator(regex)

        borderStyleSheet = f'border:5px solid {Colors.ScolorDark};'
        bcInputStyleSheet = f'background-color: {Colors.neutralLight};'
        textStyleSheet = f'color: {Colors.ScolorDark};'
        self.Input1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Input1.setGeometry(QtCore.QRect(30, 60, 511, 71))
        self.Input1.setFont(font)
        self.Input1.setValidator(validator)
        self.Input1.setObjectName("Input1")
        self.Input1.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        self.Input2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Input2.setGeometry(QtCore.QRect(30, 160, 511, 71))
        self.Input2.setFont(font)
        self.Input2.setValidator(validator)
        self.Input2.setObjectName("Input2")
        self.Input2.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        self.Output = QtWidgets.QLineEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(30, 310, 511, 81))
        self.Output.setFont(font)
        self.Output.setReadOnly(True)
        self.Output.setValidator(validator)
        self.Output.setObjectName("Output")
        self.Output.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        self.ErrorMessage = QtWidgets.QMessageBox
        
        buttonStyleSheet = f'QPushButton{{background-color: {Colors.FcolorLight};\
                                        {borderStyleSheet + textStyleSheet}}}\
                             QPushButton::pressed{{background-color: {Colors.FcolorMain};\
                                        border: 3px solid {Colors.ScolorDark};\
                                        {textStyleSheet}}}'
        self.Plus = QtWidgets.QPushButton(self.centralwidget)
        self.Plus.setGeometry(QtCore.QRect(600, 70, 131, 51))
        self.Plus.setFont(font)
        self.Plus.setObjectName("Plus")
        self.Plus.setStyleSheet(buttonStyleSheet)
        self.Plus.setText("+")

        self.Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Minus.setGeometry(QtCore.QRect(600, 160, 131, 51))
        self.Minus.setFont(font)
        self.Minus.setObjectName("Minus")
        self.Minus.setStyleSheet(buttonStyleSheet)
        self.Minus.setText("-")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(620, 350, 171, 120))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Пашкавец\nАнгеліна\nАляксандраўна\n4к, 4гр, 2023\n")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)