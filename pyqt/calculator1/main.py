import sys

from PySide2.QtWidgets import *
from decimal import  Decimal
import cal2

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.syntax = ""

    def UI(self):
        self.ui = cal2.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        for i in self.ui.centralwidget.findChildren(type(QPushButton())):
            i.clicked.connect(self.buttonClicked)

    def calculate(self):
        pass

    def buttonClicked(self):
        sender = self.sender()
        if sender.text() == 'clr':
            self.syntax = ""
            self.ui.panel.setText('')
        elif sender.text() == 'btn_eql':
            self.calculate()
        elif sender.text() == '=':
            self.process_str()
        elif sender.text() == 'Back':
            self.syntax = self.syntax[0:-1]
            self.ui.panel.setText(self.syntax)
        else:
            self.syntax += sender.text()
            self.ui.panel.setText(self.syntax)



    def keyPressEvent(self, e):
        if e.key() in [16777220, 16777221]:
            self.process_str()
        elif e.key() in [48, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47, 42, 45]:
            self.syntax += e.text()
            self.ui.panel.setText(self.syntax)
        elif e.key() == 16777219:
            self.syntax = self.syntax[0:-1]
            self.ui.panel.setText(self.syntax)
        else:
            print(e.key())

    def process_str(self):
        try:
            # eval function does the string parsing and calculation
            res = eval(self.ui.panel.text())

            # if the length of the number is too large then it is printed in scientific format
            if len(str(res)) > 15:
                res = '%E' % Decimal(res)
            self.ui.label.setText(str(res))
        except:
            print(sys.exc_info())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.UI()
    sys.exit(app.exec_())
