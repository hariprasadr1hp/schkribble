from PyQt5 import QtGui, QtWidgets

# from src.libutil import MyColors, stylizeColor

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.uiInitialize()

    def uiInitialize(self) -> None:
        self.uiSettings()
        self.uiIcons()
        self.uiCentralWidget()
        self.uiMenuBar()
        self.uiContextMenu()
        self.uiStatusBar()
        self.uiToolBar()

    def uiSettings(self) -> None:
        self.setGeometry(0,0,1919, 1015)
        self.setWindowTitle("Schkribble")
        self.image = QtGui.QImage(
                self.size(),
                QtGui.QImage.Format_RGB32
        )
        self.image.fill(MyColors.grey)
        
    def uiIcons(self) -> None:
        # icons
        self.icon_pen = QtGui.QIcon("assets/icon_pen.jpg")
        self.icon_eraser = QtGui.QIcon("assets/icon_eraser.jpg")
        self.icon_clear = QtGui.QIcon("assets/icon_clear.jpg")
        self.icon_quit = QtGui.QIcon("assets/icon_quit.jpg")

    def uiToolBar(self):
        self.toolbar = QtWidgets.QToolBar()
        self.addToolBar(self.toolbar)
        self.btn_action_pen = QtWidgets.QAction(self.icon_pen, "pen")
        self.btn_action_eraser = QtWidgets.QAction(self.icon_eraser, "eraser")
        self.btn_action_clear = QtWidgets.QAction(self.icon_clear, "clear")
        self.btn_action_quit = QtWidgets.QAction(self.icon_quit, "quit")

        self.toolbar.addAction(self.btn_action_pen)
        self.toolbar.addAction(self.btn_action_eraser)
        self.toolbar.addAction(self.btn_action_clear)
        self.toolbar.addAction(self.btn_action_quit)

    def uiCentralWidget(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.setCentralWidget(self.central_widget)

    def uiMenuBar(self) -> None:
        # initializing main menu
        self.menu_main = QtWidgets.QMenuBar()
        self.setMenuBar(self.menu_main)

        # setting up file menu
        self.menu_file = QtWidgets.QMenu("File")
        self.menu_main.addMenu(self.menu_file)
        self.btn_menu_clear = QtWidgets.QAction('clear')
        self.menu_file.addAction(self.btn_menu_clear)
        self.btn_menu_quit = QtWidgets.QAction('quit')
        self.menu_file.addAction(self.btn_menu_quit)

        # setting up help menu
        self.menu_help = QtWidgets.QMenu("Help")
        self.menu_main.addMenu(self.menu_help)
        self.btn_menu_about = QtWidgets.QAction("About")
        self.menu_help.addAction(self.btn_menu_about)
    
    def uiContextMenu(self):
        self.context_menu = QtWidgets.QMenu()

        self.btn_context_pen_color = self.context_menu.addMenu('color')
        self.btn_context_pen_color_grey = self.btn_context_pen_color.addAction('grey')
        self.btn_context_pen_color_green = self.btn_context_pen_color.addAction('green')
        self.btn_context_pen_color_yellow = self.btn_context_pen_color.addAction('yellow')
        self.btn_context_pen_color_violet = self.btn_context_pen_color.addAction('violet')
        self.btn_context_pen_color_blue = self.btn_context_pen_color.addAction('blue')
        self.btn_context_pen_color_pink = self.btn_context_pen_color.addAction('pink')
        self.btn_context_pen_size = self.context_menu.addMenu('size')
        self.btn_context_pen_size_4 = self.btn_context_pen_size.addAction('4')
        self.btn_context_pen_size_6 = self.btn_context_pen_size.addAction('6')
        self.btn_context_pen_size_8 = self.btn_context_pen_size.addAction('8')
        self.btn_context_pen_size_10 = self.btn_context_pen_size.addAction('10')
        self.btn_context_pen_size_12 = self.btn_context_pen_size.addAction('12')
        self.btn_context_pen_size_36 = self.btn_context_pen_size.addAction('36')
        self.btn_context_pen = self.context_menu.addAction('pen')
        self.btn_context_eraser = self.context_menu.addAction('eraser')
        self.btn_context_clear = self.context_menu.addAction('clear')
        self.btn_context_help = self.context_menu.addAction('help')
        self.btn_context_quit = self.context_menu.addAction('quit')


    def uiStatusBar(self):
        stylizeColor(self.statusBar(), "color", MyColors.grey)
        stylizeColor(self.statusBar(), "background", MyColors.green)


if __name__ == "__main__":
    from libutil import MyColors, stylizeColor
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec()

else:
    from src.libutil import MyColors, stylizeColor
