from PyQt5.QtWidgets import (QMainWindow)
from gui import Ui_MainWindow
import decimal as dc

#set mask for output
#add release to github

def GetCorrectInputString(inp_str: str):
    inp_str = inp_str.replace(',', '.')
    inp_str = inp_str.replace(' ', '')
    return inp_str
    
def GetCorrectOutputString(res_dec: dc.Decimal): 
    numbers = res_dec.to_eng_string().split('.')
    main_part = numbers[0]
    float_part = numbers[1] if len(numbers) == 2 else ''

    output = ''
    i = len(main_part)
    while i >= 3:
        output = main_part[i-3:i] + ' ' + output
        i -= 3
    if i > 0:
        output = main_part[:i] + ' ' + output

    output = output.strip()
    if float_part:
        while float_part[-1] == '0':
            float_part = float_part[:-1]
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

    def ClickedEvent(self, lam):
        if self.Input1.text()!='' and self.Input2.text()!='':
            finp = dc.Decimal(GetCorrectInputString(self.Input1.text()))
            sinp = dc.Decimal(GetCorrectInputString(self.Input2.text()))
            self.Output.clear()
            res = lam(finp, sinp)
            if res >= self.MINVALUE and res <= self.MAXVALUE:
                res = res.quantize(dc.Decimal('1.000000'), dc.ROUND_HALF_UP)
                self.Output.insert(GetCorrectOutputString(res))
            else:
                self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Рэзультат выходзіць па-за межы падтрымліваемыз лічбаў")

    def PlusClickedEvent(self):
        self.ClickedEvent(lambda x, y: x+y)

    def MinusClickedEvent(self):
        self.ClickedEvent(lambda x, y: x-y)

    def MultiplClickedEvent(self):
        self.ClickedEvent(lambda x, y: x*y)

    def DivisionClickedEvent(self):
        inp2 = dc.Decimal(self.Input2.text().replace(',', '.'))
        if inp2 == 0:
            self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Дзяленне на ноль")
            return
        self.ClickedEvent(lambda x, y: x/y)
