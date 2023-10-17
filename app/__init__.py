from PyQt5.QtWidgets import (QMainWindow)
from gui import Ui_MainWindow
import decimal as dc

#set mask for output
#add release to github

def CheckCorrectString(inp_str: str) -> [bool, str]:
    if inp_str[-1] == '.':
        return False, ''
    inp_str = inp_str.replace(',', '.')
    point = len(inp_str) if inp_str.find('.') == -1 else inp_str.find('.')
    for i in range(1,4):
        if point-i>=0 and inp_str[point-i] == ' ':
            return False, ''
    inp_str = inp_str.replace(' ', '')
    return True, inp_str
    
def GetCorrectString(res):
    res = res.replace(' ', '')
    main_part, float_part = res.split('.')

    output = ''
    i = len(main_part)
    while i >= 3:
        output = main_part[i-3:i] + ' ' + output
        i -= 3
    if i > 0:
        output = main_part[:i] + ' ' + output

    output = output.strip()
    while len(float_part) != 0 and float_part[-1] == '0':
        float_part = float_part[:-1]
    if float_part:
        output += '.' + float_part
    return output

class MainWindow(QMainWindow, Ui_MainWindow):
    MAXVALUE = dc.Decimal('1000000000000.000000')
    MINVALUE = dc.Decimal('-1000000000000.000000')
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("BigNumCalc")
        Ui_MainWindow.__init__(self)

        self.setupUi(self)

        self.Plus.clicked.connect(self.PlusClickedEvent)
        self.Minus.clicked.connect(self.MinusClickedEvent)
        self.Multipl.clicked.connect(self.MultiplClickedEvent)
        self.Division.clicked.connect(self.DivisionClickedEvent)


    def GetInputs(self):
        dec = []
        for i in range(len(self.Inputs)):
            if self.Inputs[i].text() == '':
                return
            correct, inp = CheckCorrectString(self.Inputs[i].text())
            if not correct:
                self.ErrorMessage.warning(
                    self.centralwidget, 'Папярэджванне', "Некарэктна ўведзеныя дадзеныя")
                return
            dec += [dc.Decimal(inp)]
        return dec

    def ClickedEvent(self, lam):
        dec = self.GetInputs()
        if dec == None:
            return
        self.Output.clear()
        res = lam(dec[0], dec[1])
        if res >= self.MINVALUE and res <= self.MAXVALUE:
            res = res.quantize(dc.Decimal('1.000000'), dc.ROUND_HALF_UP)
            self.Output.insert(GetCorrectString(res.to_eng_string()))
        else:
            self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Рэзультат выходзіць па-за межы падтрымліваемых лічбаў")

    def PlusClickedEvent(self):
        self.ClickedEvent(lambda x, y: x+y)

    def MinusClickedEvent(self):
        self.ClickedEvent(lambda x, y: x-y)

    def MultiplClickedEvent(self):
        self.ClickedEvent(lambda x, y: x*y)

    def DivisionClickedEvent(self):
        dec = self.GetInputs()
        if dec == None:
            return
        for i in range(1, len(self.Inputs)):
            if dec[i] == 0:
                self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Дзяленне на ноль")
                return
        self.ClickedEvent(lambda x, y: x/y)
