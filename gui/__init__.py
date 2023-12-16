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

INPUTS = 4
OPERATIONS = ['+', '-', '*', '/']

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet(f'background-color: {Colors.ScolorMain};')
        MainWindow.resize(850, (INPUTS+3)*150 + 150)

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
        textStyleSheetCenter = f'color: {Colors.ScolorDark}; text-align: center;'

        self.Inputs = []
        self.ComboBoxes = []
        for i in range(INPUTS):
            self.Inputs += [QtWidgets.QLineEdit(self.centralwidget)]
            self.Inputs[i].setGeometry(QtCore.QRect(30, 150*i + 80, 750, 70))
            self.Inputs[i].setFont(font)
            self.Inputs[i].setValidator(validator)
            self.Inputs[i].setObjectName("Input"+str(i))
            self.Inputs[i].setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)
            self.Inputs[i].setText('0')

            if i != INPUTS-1:
                self.ComboBoxes += [QtWidgets.QComboBox(self.centralwidget)]
                self.ComboBoxes[i].setGeometry(QtCore.QRect(345, 150*(i+1) + 15, 70, 50))
                self.ComboBoxes[i].setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheetCenter)
                self.ComboBoxes[i].addItems(OPERATIONS)   

        self.Output = QtWidgets.QLineEdit(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(30, INPUTS*150 + 100, 750, 70))
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
        
        self.Result_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Result_btn.setGeometry(QtCore.QRect(315, 150*INPUTS + 30, 130, 50))
        self.Result_btn.setFont(font)
        self.Result_btn.setObjectName("Result")
        self.Result_btn.setStyleSheet(buttonStyleSheet)
        self.Result_btn.setText("=")

        self.RoundOutput = QtWidgets.QLineEdit(self.centralwidget)
        self.RoundOutput.setGeometry(QtCore.QRect(30, (INPUTS+2)*150 + 30, 750, 80))
        self.RoundOutput.setFont(font)
        self.RoundOutput.setReadOnly(True)
        self.RoundOutput.setValidator(validator)
        self.RoundOutput.setObjectName("Round Output")
        self.RoundOutput.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheet)

        self.CBRound = QtWidgets.QComboBox(self.centralwidget)
        self.CBRound.setGeometry(QtCore.QRect(220, 150*(INPUTS+1) + 75, 190, 80))
        self.CBRound.setStyleSheet(borderStyleSheet + bcInputStyleSheet + textStyleSheetCenter)
        self.CBRound.addItems(['Матэматычнае', 'Бухгалтарскае', 'Усячэнне'])

        self.Round_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Round_btn.setGeometry(QtCore.QRect(220 + 190 + 60, 150*(INPUTS+1) + 75, 180, 80))
        font.setPointSize(14)
        self.Round_btn.setFont(font)
        self.Round_btn.setObjectName("Round")
        self.Round_btn.setStyleSheet(buttonStyleSheet)
        self.Round_btn.setText("Акругліць")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(150, (INPUTS+3)*150, 700, 100))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet(textStyleSheetCenter)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("Пашкавец Ангеліна Аляксандраўна 4к, 4гр, 2023\n")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)