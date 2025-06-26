from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, Slot, Signal,
    QSize, QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QResizeEvent,
    QImage, QKeySequence, QLinearGradient, QStandardItemModel, QStandardItem,
    QPalette, QPixmap, QRadialGradient, QTransform, Qt)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QTextBrowser, QVBoxLayout,
    QWidget, QFileDialog)


class TLabel(QLabel):
    def __init__(self):
        super().__init__()
        super().setStyleSheet("background-color: rgb(255, 255, 255)")
        super().setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        super().setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().setPixmap(self.__pixmap.scaled(event.size(), Qt.AspectRatioMode.KeepAspectRatio))
        super().resizeEvent(event)

    def setPixmap(self, arg__1) -> None:
        assert(isinstance(arg__1, QPixmap) or isinstance(arg__1, QImage) or isinstance(arg__1, str))
        self.__pixmap = arg__1 if isinstance(arg__1, QPixmap) else QPixmap(arg__1)
        x,y = super().width(), super().height()
        super().resize(x + 1, y + 1)
        super().resize(x, y)