import sys
import time


from pypresence import Presence
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

# details = 2nd line
# state = 3rd line
# large_image = large img
# small_image = small img
# buttons = buttons


def pypresence(client_id, details, state, first_button, first_button_url, second_button, second_button_url):

    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()

    print("Connected to Discord")

    RPC.update(state=state, details=details, large_image="piximg", small_image="piximg", start=2, buttons=[
               {"label": first_button, "url": first_button_url}, {"label": second_button, "url": second_button_url}])  # Set the presence
    print(
        client_id,
        details,
        state,
        first_button,
        first_button_url,
        second_button,
        second_button_url,
    )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyPresence GUI")

        layout = QVBoxLayout()

        client_id_input = QLineEdit()
        client_id_input.setPlaceholderText("Client ID")

        details_input = QLineEdit()
        details_input.setPlaceholderText("Details")

        state_input = QLineEdit()
        state_input.setPlaceholderText("State")

        first_button = QLineEdit()
        first_button.setPlaceholderText("First Button")

        first_button_url = QLineEdit()
        first_button_url.setPlaceholderText("First Button URL")

        second_button = QLineEdit()
        second_button.setPlaceholderText("Second Button")

        second_button_url = QLineEdit()
        second_button_url.setPlaceholderText("Second Button URL")

        button = QPushButton("Update Rich Presence")

        widgets = [
            client_id_input,
            details_input,
            state_input,
            first_button,
            first_button_url,
            second_button,
            second_button_url,
            button,
        ]

        self.setFixedSize(QSize(400, 400))

        for w in widgets:
            layout.addWidget(w)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

        button.clicked.connect(lambda: pypresence(
            client_id_input.text(),
            details_input.text(),
            state_input.text(),
            first_button.text(),
            first_button_url.text(),
            second_button.text(),
            second_button_url.text(),
        ))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
