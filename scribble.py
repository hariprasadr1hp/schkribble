import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint with PyQt5")
        self.setGeometry(0, 0, 1920, 1080)

        # creating image object
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGB32)

        # making image color to white
        self.image.fill(QtCore.Qt.white)

        # variables
        # drawing flag
        self.drawing = False
        # default brush size
        self.brushSize = 2
        # default color
        self.brushColor = QtCore.Qt.black

        # QPoint object to tract the point
        self.lastPoint = QtCore.QPoint()

        # creating menus and its actions
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        
        saveAction = QtWidgets.QAction("Save", self)
        saveAction.setShortcut("Ctrl + S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.saveImage)

        clearAction = QtWidgets.QAction("Clear", self)
        clearAction.setShortcut("Ctrl + C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clearImage)

        brushSizeMenu = mainMenu.addMenu("Brush Size")

        pix_4 = QtWidgets.QAction("4px", self)
        brushSizeMenu.addAction(pix_4)
        pix_4.triggered.connect(lambda: setattr(self, "brushSize", 4))

        pix_7 = QtWidgets.QAction("7px", self)
        brushSizeMenu.addAction(pix_7)
        pix_7.triggered.connect(lambda: setattr(self, "brushSize", 7))

        pix_9 = QtWidgets.QAction("9px", self)
        brushSizeMenu.addAction(pix_9)
        pix_9.triggered.connect(lambda: setattr(self, "brushSize", 9))

        pix_12 = QtWidgets.QAction("12px", self)
        brushSizeMenu.addAction(pix_12)
        pix_12.triggered.connect(lambda: setattr(self, "brushSize", 12))

        brushColorMenu = mainMenu.addMenu("Brush Color")

        black = QtWidgets.QAction("black", self)
        brushColorMenu.addAction(black)
        black.triggered.connect(lambda: setattr(self, "brushColor", QtCore.Qt.black))

        white = QtWidgets.QAction("white", self)
        brushColorMenu.addAction(white)
        white.triggered.connect(lambda: setattr(self, "brushColor", QtCore.Qt.white))

        green = QtWidgets.QAction("green", self)
        brushColorMenu.addAction(green)
        green.triggered.connect(lambda: setattr(self, "brushColor", QtCore.Qt.green))

        blue = QtWidgets.QAction("blue", self)
        brushColorMenu.addAction(blue)
        blue.triggered.connect(lambda: setattr(self, "brushColor", QtCore.Qt.blue))

        red = QtWidgets.QAction("red", self)
        brushColorMenu.addAction(red)
        red.triggered.connect(lambda: setattr(self, "brushColor", QtCore.Qt.red))

    # method for checking mouse cicks
    
    def mousePressEvent(self, event):
        # if left mouse button is pressed
        if event.button() == QtCore.Qt.LeftButton:
            # make drawing flag true
            self.drawing = True
            # make last point to the point of cursor
            self.lastPoint = event.pos()

    # method for tracking mouse activity
    def mouseMoveEvent(self, event):

        # checking if left button is pressed and drawing flag is true
        if (event.buttons() & QtCore.Qt.LeftButton) & self.drawing:

            # creating painter object
            painter = QtGui.QPainter(self.image)

            # set the pen of the painter
            painter.setPen(QtGui.QPen(self.brushColor, self.brushSize,
                                QtCore.Qt.SolidLine, QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))

            # draw line from the last point of cursor to the current point
            # this will draw only one step
            painter.drawLine(self.lastPoint, event.pos())

            # change the last point
            self.lastPoint = event.pos()
            # update
            self.update()

    # method for mouse left button release
    def mouseReleaseEvent(self, event):

        if event.button() == QtCore.Qt.LeftButton:
            # make drawing flag false
            self.drawing = False

    # paint event
    def paintEvent(self, event):
        # create a canvas
        canvasPainter = QtGui.QPainter(self)

        # draw rectangle on the canvas
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    # method for saving canvas
    def saveImage(self):
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                                                  "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    # method for clearing every thing on canvas
    def clearImage(self):
        # make the whole canvas white
        self.image.fill(QtCore.Qt.white)
        # update
        self.update()



app = QtWidgets.QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
