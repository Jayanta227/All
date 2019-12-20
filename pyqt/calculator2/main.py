import sys

from PySide2.QtWidgets import *
import cal2, untitled


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
        if e.key() == 16777220:
            self.process_str()
        elif e.key() in [48, 46, 49, 50, 51, 52, 53, 54, 55, 56, 57, 43, 47, 42, 45]:
            self.syntax += e.text()
            self.ui.panel.setText(self.syntax)

    def process_str(self):
        self.ui.lcd.display(eval(self.ui.panel.text()))
        wd = QWidget()
        self.ui2 = untitled.Ui_Form()
        self.ui2.setupUi(wd)
        self.setCentralWidget(wd)
        self.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.UI()
    sys.exit(app.exec_())
