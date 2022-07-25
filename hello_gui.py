from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
import sys

class example(QMainWindow):
    def __init__(self):
        super().__init__()
        btn = QPushButton("Hello world!",self)
        btn.move(50,75)
        self.setGeometry(100,100,200,150)
        self.setWindowTitle('PyQt Window')
        self.show()

if __name__=='__main__':

    app=QApplication(sys.argv)
    ex=example()
    sys.exit(app.exec_())
