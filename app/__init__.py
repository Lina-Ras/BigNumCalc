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
    if res.find('.') > -1:
        main_part, float_part = res.split('.')
    else:
        main_part, float_part = res, '0'

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

        self.Result_btn.clicked.connect(self.Calculate)
        self.Round_btn.clicked.connect(self.Round)


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

# ['Матэматычнае', 'Бухгалтарскае', 'Усячэнне']
    def Round(self):
        self.RoundOutput.clear()
        out = dc.Decimal(self.Output.text())
        round_method = self.CBRound.currentIndex()
        if round_method == 0:
            out = out.quantize(dc.Decimal('1'), dc.ROUND_HALF_UP)
        elif round_method == 1:
            out = out.quantize(dc.Decimal('1'))
        elif round_method == 2:
            out = out // 1
        self.RoundOutput.insert(GetCorrectString(out.to_eng_string()))

    def Calculate(self):
        self.Output.clear()
        self.RoundOutput.clear()
        inps = self.GetInputs()
        ops = [combx.currentText() for combx in self.ComboBoxes]
        res = self.Operation(ops[1], inps[1], inps[2])
        if res != None:
            if (ops[2] == '*' or ops[2] == '/') and (ops[0] == '+' or ops[0] == '-'):
                res = self.Operation(ops[2], res, inps[3])
                if res != None:
                    res = self.Operation(ops[0], inps[0], res)
            else:
                res = self.Operation(ops[0], inps[0], res)
                if res != None:
                    res = self.Operation(ops[2], res, inps[3])
            if res != None:
                res = res.quantize(dc.Decimal('1.000000'), dc.ROUND_HALF_UP)
                self.Output.insert(GetCorrectString(res.to_eng_string()))

    def Operation(self, op, x, y):
        if op == '+':
            def lam(x, y): return x+y
        elif op == '-':
            def lam(x, y): return x-y
        elif op == '*':
            def lam(x, y): return x*y
        elif op == '/':
            if y == 0:
                self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Дзяленне на ноль")
                return
            def lam(x, y): return x/y
        res = lam(x, y)
        if res >= self.MINVALUE and res <= self.MAXVALUE:
            return res.quantize(dc.Decimal('1.0000000000'), dc.ROUND_HALF_UP)  
        else:
            self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Рэзультат выходзіць па-за межы падтрымліваемых лічбаў")
            return None