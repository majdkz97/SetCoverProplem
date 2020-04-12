# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MAJDKZ\Desktop\view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import random
import Chromosome
import Functions
import Universe
import Set
import Generation
import Main
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 529)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button_Solve = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Solve.setGeometry(QtCore.QRect(10, 420, 221, 81))
        self.Button_Solve.setObjectName("Button_Solve")
        self.Clear_Output = QtWidgets.QPushButton(self.centralwidget)
        self.Clear_Output.setGeometry(QtCore.QRect(750, 230, 100, 30))
        self.Clear_Output.setObjectName("Clear_Output")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(250, 10, 601, 211))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_7.addWidget(self.label_7)
        self.Input_Sets = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_7)
        self.Input_Sets.setObjectName("Input_Sets")
        self.verticalLayout_7.addWidget(self.Input_Sets)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(250, 250, 601, 251))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.Output_Solution = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_8)
        self.Output_Solution.setObjectName("Output_Solution")
        self.verticalLayout_8.addWidget(self.Output_Solution)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 221, 401))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Number_Of_Chromosomes = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Number_Of_Chromosomes.setFont(font)
        self.Number_Of_Chromosomes.setObjectName("Number_Of_Chromosomes")
        self.verticalLayout.addWidget(self.Number_Of_Chromosomes)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.Size_Of_Universe = QtWidgets.QTextEdit(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Size_Of_Universe.setFont(font)
        self.Size_Of_Universe.setObjectName("Size_Of_Universe")
        self.verticalLayout_4.addWidget(self.Size_Of_Universe)
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.Number_Of_Generation = QtWidgets.QTextEdit(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Number_Of_Generation.setFont(font)
        self.Number_Of_Generation.setObjectName("Number_Of_Generation")
        self.verticalLayout_5.addWidget(self.Number_Of_Generation)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.Crossover_Rate = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Crossover_Rate.setFont(font)
        self.Crossover_Rate.setObjectName("Crossover_Rate")
        self.verticalLayout_2.addWidget(self.Crossover_Rate)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.Crossover_Type = QtWidgets.QComboBox(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Crossover_Type.setFont(font)
        self.Crossover_Type.setObjectName("Crossover_Type")
        self.Crossover_Type.addItem("")
        self.Crossover_Type.addItem("")
        self.verticalLayout_6.addWidget(self.Crossover_Type)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.Mutation_Rate = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.Mutation_Rate.setFont(font)
        self.Mutation_Rate.setObjectName("Mutation_Rate")
        self.verticalLayout_3.addWidget(self.Mutation_Rate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Genetic Algorithm"))
        self.Button_Solve.setText(_translate("MainWindow", "Solve it "))
        self.Clear_Output.setText(_translate("MainWindow", "Clear Output"))
        self.label_7.setText(_translate("MainWindow", "Input Sets"))
        self.label_8.setText(_translate("MainWindow", "OUTPUT SOLUTION"))
        self.label.setText(_translate("MainWindow", "Population Size"))
        self.label_2.setText(_translate("MainWindow", "Size of Universe"))
        self.label_6.setText(_translate("MainWindow", "Number of Generations"))
        self.label_4.setText(_translate("MainWindow", " Crossover Rate "))
        self.label_3.setText(_translate("MainWindow", "Type of Crossover"))
        self.Crossover_Type.setItemText(0, _translate("MainWindow", "one point"))
        self.Crossover_Type.setItemText(1, _translate("MainWindow", "two point"))
        self.label_5.setText(_translate("MainWindow", "Mutation Rate"))
        #ربط الزر بتابع الحل
        self.Button_Solve.clicked.connect(self.Solve)
        self.Clear_Output.clicked.connect(self.Clear_Output_Function)
        

    def Solve(self):

        universe_Input = Universe.Universe()
        #تحديد حجم الفضاء
        universe_Input.universe_Size = int(self.Size_Of_Universe.toPlainText())

        #توليد عناصر الفضاء
        universe_Input.list_Universe_Items = []
        for i in range(0,universe_Input.universe_Size):
            universe_Input.list_Universe_Items.append(i)
        
        
        
        #توليد مجموعات الدخل
        input_Text = self.Input_Sets.toPlainText()
        lines = []
        lines = input_Text.splitlines()
        #تحديد عدد المجموعات
        universe_Input.set_Count = int(len(lines)/2)

        #توليد المجموعات
        universe_Input.list_Sets = []
        for i in range(0,len(lines),2):
            Input_Set = Set.Set()
            Input_Set.list_set = list(map(int, lines[i].split()))
            Input_Set.set_Cost = float(lines[i+1])
            universe_Input.list_Sets.append(Input_Set)
        
        #تحديد عدد الكروموسومات
        universe_Input.chromosome_Count = int(self.Number_Of_Chromosomes.toPlainText())
        
        #تحديد عدد الأجيال
        universe_Input.generations_Count = int(self.Number_Of_Generation.toPlainText())
        list_Genereations = []

        #تحديد معدل التصالب
        
        universe_Input.crossover_Rate = float(self.Crossover_Rate.toPlainText())
        
        #تحديد معدل الطفران
        
        universe_Input.mutation_Rate = float(self.Mutation_Rate.toPlainText())
        
        #استدعاء تابع الحل
        Main.Main_Solve(universe_Input,list_Genereations,self.Crossover_Type.currentText())
        
        newlist_Sorted = sorted(list_Genereations, key=lambda x: x.best_Chromosome.Fitness, reverse=True).copy()
        out = newlist_Sorted[0]
        
        #تجهيز الخرج
        str1=''
        str1 +='List_Genes Of Best Chromosomes: '
        str1 += ' - '.join(str(e) for e in out.best_Chromosome.List_Genes)    
        str1 += '\n'
        str1 +='Fitness Of Best Chromosomes: '
        str1 += str(out.best_Chromosome.Fitness)
        str1 += '\n'
        str1 +='Sum_Costs Of Best Chromosomes: '
        str1 += str(out.best_Chromosome.sum_Costs)
        str1 += '\n'
        index =0
        str1 += 'Solution Sets: '
        str1 += '\n'
        for s in out.best_Chromosome.List_Genes:
            if s==1:
                str1+= 'Set ({}): '.format(index+1)
                str1 += ' - '.join(str(e) for e in universe_Input.list_Sets[index].list_set)
                str1+='\n'
            index+=1
        self.Output_Solution.appendPlainText(str1)
        list_Genereations.clear()

    def Clear_Output_Function(self):
        self.Output_Solution.clear()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

