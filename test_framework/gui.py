import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('TL85 Capstone')

        # TODO: add dropdown to select JSON file

        self.label_start_value = QLabel(self)
        self.label_start_value.setText('Start Value')
        self.label_start_value.move(20, 100)

        self.textbox_start_value = QLineEdit(self)
        self.textbox_start_value.resize(100,30)
        self.textbox_start_value.move(200, 100)

        self.label_stop_value = QLabel(self)
        self.label_stop_value.setText('Stop Value')
        self.label_stop_value.move(20, 140)

        self.textbox_stop_value = QLineEdit(self)
        self.textbox_stop_value.resize(100,30)
        self.textbox_stop_value.move(200, 140)

        self.label_step_value = QLabel(self)
        self.label_step_value.setText('Step Value')
        self.label_step_value.move(20, 180)

        self.textbox_step_value = QLineEdit(self)
        self.textbox_step_value.resize(100,30)
        self.textbox_step_value.move(200, 180)

        self.label_step_value = QLabel(self)
        self.label_step_value.setText('Threshold')
        self.label_step_value.move(20, 220)

        self.label_step_value = QLabel(self)
        self.label_step_value.setText('0')
        self.label_step_value.move(200, 220)

        # TODO: display and highlight Fault above threshold | Fault below threshold
        # TODO: display and highlight Fault active high | Fault active low

        self.label_step_value = QLabel(self)
        self.label_step_value.setText('Test description:')
        self.label_step_value.move(20, 260)

        # TODO: description gets cut off - can you make this into a multi-line textbox

        self.label_step_value = QLabel(self)
        self.label_step_value.setText('lkjashdflkjhasdflkjhasdfkljhasdlkfjhaskldhjflkjhasdflkjhsadkljfhsadklfhjsdalkjhfklhjasdlkfjhfd')
        self.label_step_value.move(200, 260)

        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
