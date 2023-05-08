import os
import sys
import time
import random
import pprint
import datetime
import traceback
# from PyQt5.QtCore import Qt
import Qt
from Qt import QtCore, QtWidgets

#import ui with inheritance
from ui.timelogs_form import Ui_Form as timeLogs_form

class TimeLogs (QtWidgets.QWidget):
    update_overview = QtCore.Signal(QtWidgets.QWidget, float)
    finish_process = QtCore.Signal(QtWidgets.QWidget)

    #change variables to the ones from toolkit (ex. projectName, user, task)
    def __init__(self, project, user, task):
        super(TimeLogs, self).__init__()

        self.ui = timeLogs_form()
        self.ui.setupUi(self)

      
    