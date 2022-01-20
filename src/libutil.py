from typing import NamedTuple
from PyQt5 import QtGui, QtWidgets


class MyColors(NamedTuple):
    grey = QtGui.QColor("#243238")
    green = QtGui.QColor("#afff87")
    yellow = QtGui.QColor("#ffe300")
    violet = QtGui.QColor("#8787ff")
    blue = QtGui.QColor("#87d7ff")
    pink = QtGui.QColor("#d75fff")


def stylizeColor(widget: QtWidgets.QWidget, attr: str, color: QtGui.QColor):
    widget.setStyleSheet("{}: {}".format(attr, color.name()))


