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

INPUTS = 2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(f'background-color: {Colors.ScolorMain};')
        MainWindow.resize(1000, (INPUTS+1)*120 + 120)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(24)

        regex_str = "[-]?([0][,.][0-9]{,6}|"
        regex_str+="[1]([\s]?[0]{3}){3}[.,][0]{0,6}|"
        regex_str+="[1-9][0-9]{,2}([\s]?[0-9]{3}){,3}[,.][0-9]{0,6})"
        regex = QtCore.QRegExp(regex_str)
        validator = QtGui.QRegExpValidator(regex)

        borderStyleSheet = f'border:5px solid {Colors.ScolorDark};'
        bcInputStyleSheet = f'background-color: {Colors.neutralLight};'
        textStyleSheet = f'color: {Colors.ScolorDark};'

        self.Inputs = []
        for i in range(INPUTS):
            self.Inputs += [QtWidgets.QLineEdit(self.centralwidget)]
            self.Inputs[i].setGeometry(QtCore.QRect(30, 120*i + 60, 700, 71))
            self.Inputs[i].setFont(font)
            self.Inputs[i].setValidator(validator)
            self.Inputs[i].setObjectName("Input"+str(i))
            self.Inputs[i].setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        # self.Input2 = QtWidgets.QLineEdit(self.centralwidget)
        # self.Input2.setGeometry(QtCore.QRect(30, 160, 700, 71))
        # self.Input2.setFont(font)
        # self.Input2.setValidator(validator)
        # self.Input2.setObjectName("Input2")
        # self.Input2.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        self.Output = QtWidgets.QLineEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(30, INPUTS*120 + 100, 700, 81))
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
        self.Plus.setGeometry(QtCore.QRect(800, 70, 131, 51))
        self.Plus.setFont(font)
        self.Plus.setObjectName("Plus")
        self.Plus.setStyleSheet(buttonStyleSheet)
        self.Plus.setText("+")

        self.Minus = QtWidgets.QPushButton(self.centralwidget)
        self.Minus.setGeometry(QtCore.QRect(800, 130, 131, 51))
        self.Minus.setFont(font)
        self.Minus.setObjectName("Minus")
        self.Minus.setStyleSheet(buttonStyleSheet)
        self.Minus.setText("-")

        self.Multipl = QtWidgets.QPushButton(self.centralwidget)
        self.Multipl.setGeometry(QtCore.QRect(800, 190, 131, 51))
        self.Multipl.setFont(font)
        self.Multipl.setObjectName("Multipl")
        self.Multipl.setStyleSheet(buttonStyleSheet)
        self.Multipl.setText("*")

        self.Division = QtWidgets.QPushButton(self.centralwidget)
        self.Division.setGeometry(QtCore.QRect(800, 250, 131, 51))
        self.Division.setFont(font)
        self.Division.setObjectName("Division")
        self.Division.setStyleSheet(buttonStyleSheet)
        self.Division.setText("/")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(800, 350, 171, 120))
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