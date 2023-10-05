from PyQt5.QtWidgets import (QMainWindow)
from gui import Ui_MainWindow
import decimal as dc

#set mask for output
#add release to github

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

    def PlusClickedEvent(self):
        if self.Input1.text()!='' and self.Input2.text()!='':
            finp = dc.Decimal(self.Input1.text().replace(',', '.'))
            sinp = dc.Decimal(self.Input2.text().replace(',', '.'))
            self.Output.clear()
            if finp+sinp <= self.MAXVALUE:
                self.Output.insert((finp+sinp).to_eng_string())
            else:
                self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Рэзультат выходзіць па-за межы падтрымліваемыз лічбаў")

    def MinusClickedEvent(self):
        if self.Input1.text() != '' and self.Input2.text() != '':
            finp = dc.Decimal(self.Input1.text().replace(',', '.'))
            sinp = dc.Decimal(self.Input2.text().replace(',', '.'))
            self.Output.clear()
            if finp-sinp >= self.MINVALUE:
                self.Output.insert((finp-sinp).to_eng_string())
            else:
                self.ErrorMessage.warning(self.centralwidget, 'Папярэджванне', "Рэзультат выходзіць па-за межы падтрымліваемыз лічбаў")
