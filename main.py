import sys
from Mywindow import Mywindow
from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Mywindow()
    mywindow.show()
    sys.exit(app.exec())