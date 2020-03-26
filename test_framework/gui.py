import sys
import random
import matplotlib

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure

from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QComboBox, QVBoxLayout, QWidget, QSizePolicy
from PyQt5.QtCore import QTimer

class MplCanvas(FigureCanvas):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Graphing(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()
        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def init_UI(self):

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        self.setCentralWidget(self.canvas)

        n_data = 50
        self.xdata = list(range(n_data))
        self.ydata = [random.randint(0, 10) for i in range(n_data)]
        self.update_plot()

        self.showMaximized()

    def update_plot(self):
        # Drop off the first y element, append a new one.
        self.ydata = self.ydata[1:] + [random.randint(0, 10)]
        self.canvas.axes.cla()  # Clear the canvas.
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')
        # Trigger the canvas to update and redraw.
        self.canvas.draw()

class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('TL85 Capstone')

        self.dropdown_json = QComboBox(self)
        self.dropdown_json.move(20, 50)
        self.dropdown_json.addItem('abc')
        self.dropdown_json.addItem('def')
        self.dropdown_json.addItem('ghi')
        self.dropdown_json.addItem('jkl')

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

        self.label_threshold  = QLabel(self)
        self.label_threshold.setText('Threshold')
        self.label_threshold.move(20, 220)

        self.label_threshold_value = QLabel(self)
        self.label_threshold_value.setText('0')
        self.label_threshold_value.move(200, 220)

        self.label_test_description = QLabel(self)
        self.label_test_description.setText('Test description:')
        self.label_test_description.move(20, 260)
        self.label_test_description.adjustSize()

        self.label_test_description_value = QLabel(self)
        self.label_test_description_value.setText('the quick brown fox jumps over the lazy dog')
        self.label_test_description_value.move(200, 260)
        self.label_test_description_value.setWordWrap(True)
        self.label_test_description_value.adjustSize()

        self.label_fault_active_state = QLabel(self)
        self.label_fault_active_state.setText('Fault active state')
        self.label_fault_active_state.move(20, 300)
        self.label_fault_active_state.adjustSize()

        self.label_fault_active_state_value = QLabel(self)
        self.label_fault_active_state_value.setText('HIGH')
        self.label_fault_active_state_value.move(200, 300)
        self.label_fault_active_state_value.adjustSize()

        self.label_fault_threshold = QLabel(self)
        self.label_fault_threshold.setText('Fault occurs _______ threshold')
        self.label_fault_threshold.move(20, 340)
        self.label_fault_threshold.adjustSize()

        self.label_fault_threshold_value = QLabel(self)
        self.label_fault_threshold_value.setText('ABOVE')
        self.label_fault_threshold_value.move(105, 340)
        self.label_fault_threshold_value.adjustSize()

        self.showMaximized()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    first = Main()
    second = Graphing()
    sys.exit(app.exec_())
