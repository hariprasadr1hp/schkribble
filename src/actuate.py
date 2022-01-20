import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from src.libutil import MyColors
from src.ui_design import Ui_MainWindow


class Window(Ui_MainWindow):
    """
    Game of ....life....
    """

    def __init__(self) -> None:
        super().__init__()
        self.initialize()

    def initialize(self) -> None:
        self.initializeVariables()
        self.actuateCentralWidget()
        self.actuateMenuBar()
        self.actuateToolBar()
        self.actuateShortcuts()

    def initializeVariables(self):
        self.bg_color = MyColors.grey
        self.flag_draw = False
        self.last_point = QtCore.QPoint()
        self.pen_color = MyColors.green
        self.pen_size = 6

        # temporary variables
        self.temp_pen_color = self.pen_color
        self.temp_pen_size = self.pen_size

    def actuateCentralWidget(self) -> None:
        ...

    def actuateMenuBar(self) -> None:
        self.btn_menu_clear.triggered.connect(self.funcClearImage)
        self.btn_menu_quit.triggered.connect(self.funcQuit)
        self.btn_menu_about.triggered.connect(self.funcAbout)

    def actuateToolBar(self) -> None:
        self.btn_action_pen.triggered.connect(self.funcSetPen)
        self.btn_action_eraser.triggered.connect(self.funcSetEraser)
        self.btn_action_clear.triggered.connect(self.funcClearImage)
        self.btn_action_quit.triggered.connect(self.funcQuit)

    def funcQuit(self) -> None:
        sure_to_quit = QtWidgets.QMessageBox.question(
            self,
            "Quit Message",
            "Are you sure to quit?",
            (QtWidgets.QMessageBox.Yes or QtWidgets.QMessageBox.No),
            QtWidgets.QMessageBox.No
        )
        if sure_to_quit == QtWidgets.QMessageBox.Yes:
            QtWidgets.QApplication.quit()

    def funcAbout(self) -> None:
        info = str(self.__doc__)
        QtWidgets.QMessageBox.about(self, "automata", info)

    def funcClearImage(self) -> None:
        self.image.fill(MyColors.grey)
        self.update()

    def funcSetPenColorAndSize(self, color: QtGui.QColor, size: int) -> None:
        self.pen_color = color
        self.pen_size = size

    def funcSetPen(self):
        self.funcSetPenColorAndSize(self.temp_pen_color, self.temp_pen_size)

    def funcSetEraser(self):
        self.temp_pen_color = self.pen_color
        self.temp_pen_size = self.pen_size
        self.funcSetPenColorAndSize(self.bg_color, 72)

    def contextMenuEvent(self, event: QtGui.QContextMenuEvent) -> None:
        action = self.context_menu.exec(self.mapToGlobal(event.pos()))

        if action in [getattr(self, "btn_context_pen_color_{}".format(i)) for i in ['grey', 'green', 'yellow', 'violet', 'blue', 'pink']]:
            self.pen_color = getattr(MyColors, action.text())
        elif action in [getattr(self, "btn_context_pen_size_{}".format(i)) for i in [4, 6, 8, 10, 12, 36]]:
            self.pen_size = int(action.text())
        else:
            if action == self.btn_context_pen:
                self.funcSetPen()
            elif action == self.btn_context_eraser:
                self.funcSetEraser()
            elif action == self.btn_context_clear:
                self.funcClearImage()
            elif action == self.btn_context_help:
                self.funcAbout()
            elif action == self.btn_context_quit:
                self.funcQuit()

    def paintEvent(self, _: QtGui.QPaintEvent) -> None:
        canvas_painter = QtGui.QPainter(self)
        pen = QtGui.QPen(QtCore.Qt.blue)
        canvas_painter.setPen(pen)
        canvas_painter.drawImage(
            self.rect(),
            self.image,
            self.image.rect()
        )
        self.update()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.flag_draw = True
            self.last_point = event.pos()
            self.update()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        if (event.buttons() and QtCore.Qt.LeftButton) and self.flag_draw:
            self.statusBar().showMessage("{}, {}".format(event.x(), event.y()))
            painter = QtGui.QPainter(self.image)
            pen = QtGui.QPen(
                self.pen_color,
                self.pen_size,
                QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap,
                QtCore.Qt.RoundJoin
            )
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        if event.button() == QtCore.Qt.LeftButton:
            self.flag_draw = False
            self.update()

    def actuateShortcuts(self) -> None:
        self.btn_menu_clear.setShortcut("Ctrl+N")
        self.btn_menu_quit.setShortcut("Ctrl+W")
        self.btn_menu_about.setShortcut("Ctrl+H")
        self.btn_context_eraser.setShortcut("Ctrl+E")
        self.btn_context_clear.setShortcut("Ctrl+N")
        self.btn_context_help.setShortcut("Ctrl+H")
        self.btn_context_quit.setShortcut("Ctrl+W")


def execApp() -> None:
    app = QtWidgets.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
    

def main() -> int:
    execApp()
    sys.exit(0)

