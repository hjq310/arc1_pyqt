####################################

# (c) Radu Berdan
# ArC Instruments Ltd.

# This code is licensed under GNU v3 license (see LICENSE.txt for details)

####################################

import sys
import os
import importlib
from PyQt5 import QtGui, QtCore, QtWidgets

import Globals.GlobalStyles as s
import Globals.GlobalVars as g

sys.path.append(os.path.abspath(os.getcwd()+'/ProgPanels/'))


class prog_panel(QtWidgets.QWidget):
    
    def __init__(self):
        super(prog_panel, self).__init__()
        self.initUI()
        
    def initUI(self):   
        mainLayout=QtWidgets.QVBoxLayout()

        hbox_1=QtWidgets.QHBoxLayout()

        label_panels = QtWidgets.QLabel('Panels:')
        label_panels.setMaximumWidth(40)

        self.prog_panelList = QtWidgets.QComboBox()
        self.prog_panelList.setStyleSheet(s.comboStyle)
        self.prog_panelList.setMinimumWidth(150*g.scaling_factor)

        files = [f for f in os.listdir('ProgPanels') if f.endswith(".py")]  # populate prog panel dropbox
        for f in files:
            if (f[:-3]!="CT_LIVE"):
                self.prog_panelList.addItem(f[:-3])

        boldFont=QtGui.QFont("FontFamily")
        boldFont.setBold(True)
        self.prog_panelList.setItemData(self.prog_panelList.findText("SuperMode"), boldFont, QtCore.Qt.FontRole)

        self.push_add=QtWidgets.QPushButton('Add')
        self.push_add.setStyleSheet(s.btnStyle2)
        self.push_add.clicked.connect(self.addPanel)

        self.push_remove=QtWidgets.QPushButton('Remove')
        self.push_remove.setStyleSheet(s.btnStyle2)
        self.push_remove.clicked.connect(self.removePanel)

        self.tabFrame=QtWidgets.QTabWidget()

        hbox_1.addWidget(label_panels)
        hbox_1.addWidget(self.prog_panelList)
        hbox_1.addWidget(self.push_add)
        hbox_1.addWidget(self.push_remove)
        
        mainLayout.addLayout(hbox_1)
        mainLayout.addWidget(self.tabFrame)

        mainLayout.setContentsMargins(10,10,10,0)   # no margin on the bottom

        self.setContentsMargins(0,0,0,0)

        #self.mainPanel = QtWidgets.QGroupBox('')
        #self.mainPanel.setStyleSheet(s.groupStyleProg)
        #self.mainPanel.setLayout(mainLayout)

        #container=QtWidgets.QVBoxLayout()
        #container.addWidget(self.mainPanel)   
        #container.setContentsMargins(0,0,0,0)    

        self.setLayout(mainLayout)

        #self.setLayout(mainLayout)

        #self.show()

    def addPanel(self):

        moduleName=str(self.prog_panelList.currentText())   # format module name from drop down
        thisPanel = importlib.import_module(moduleName)     # import the module
        panel_class = getattr(thisPanel, moduleName)        # get it's main class    
        widg=panel_class()                    
        self.tabFrame.addTab(widg,moduleName) # instantiate it and add to tabWidget

        self.tabFrame.setCurrentWidget(widg)

    def setEnabled(self, state):
        for child in range(self.tabFrame.count()):
            self.tabFrame.widget(child).setEnabled(state)

    def removePanel(self):
        self.tabFrame.removeTab(self.tabFrame.currentIndex())

    def populatePanels(self):
        pass

