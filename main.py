import os
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background: #2c2c2c;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.convert())
        self.convertButton.setGeometry(QtCore.QRect(30, 150, 151, 38))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.convertButton.setFont(font)
        self.convertButton.setStyleSheet("QPushButton {\n"
" background: rgb(0, 255, 255);\n"
"color: rgb(52, 52, 52);\n"
" border: 2px solid rgb(0, 255, 255);\n"
"border-radius: 19px;\n"
"padding-bottom: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(0, 255, 255);\n"
"background: rgb(52, 52, 52);\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.convertButton.setObjectName("convertButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(30, 30, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 255, 255);")
        self.title.setObjectName("title")
        self.selected_files_list = QtWidgets.QListWidget(self.centralwidget)
        self.selected_files_list.setGeometry(QtCore.QRect(310, 70, 261, 261))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.selected_files_list.setFont(font)
        self.selected_files_list.setStyleSheet("border: 2px solid rgb(0, 255, 255);\n"
"color: rgb(0, 255, 255);\n"
"border-radius: 30;\n"
"padding-top: 26;\n"
"padding-bottom: 22;")
        self.selected_files_list.setObjectName("selected_files_list")
        self.configure = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.openFileDialog())
        self.configure.setGeometry(QtCore.QRect(370, 340, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.configure.setFont(font)
        self.configure.setStyleSheet("QPushButton {\n"
" background: rgb(0, 255, 255);\n"
"color: rgb(52, 52, 52);\n"
" border: 2px solid rgb(0, 255, 255);\n"
"border-radius: 15px;\n"
"padding-bottom: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(0, 255, 255);\n"
"background: rgb(52, 52, 52);\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.configure.setObjectName("configure")
        self.label_converTo = QtWidgets.QLabel(self.centralwidget)
        self.label_converTo.setGeometry(QtCore.QRect(30, 110, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_converTo.setFont(font)
        self.label_converTo.setStyleSheet("color: rgb(0, 255, 255);")
        self.label_converTo.setObjectName("label_converTo")
        self.selected_files_list_label = QtWidgets.QLabel(self.centralwidget)
        self.selected_files_list_label.setGeometry(QtCore.QRect(370, 78, 150, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.selected_files_list_label.setFont(font)
        self.selected_files_list_label.setStyleSheet("color: rgb(0, 255, 255);")
        self.selected_files_list_label.setObjectName("selected_files_list_label")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(180, 110, 71, 22))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.type.setFont(font)
        self.type.setStyleSheet("border: 2px solid rgb(0, 255, 255);\n"
"color: rgb(0, 255, 255);\n"
"border-radius: 4;\n"
"padding-left: 8;")
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.type.addItem("")
        self.languageSwitch = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.lang())
        self.languageSwitch.setGeometry(QtCore.QRect(30, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.languageSwitch.setFont(font)
        self.languageSwitch.setStyleSheet("QPushButton {\n"
" background: rgb(0, 255, 255);\n"
"color: rgb(52, 52, 52);\n"
" border: 2px solid rgb(0, 255, 255);\n"
"border-radius: 15px;\n"
"padding-bottom: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"color: rgb(0, 255, 255);\n"
"background: rgb(52, 52, 52);\n"
"border: 2px solid rgb(0, 255, 255);\n"
"}")
        self.languageSwitch.setObjectName("languageSwitch")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.language = "eng"
        self.images_list = []

    def convert(self):
        for filename in self.images_list:
            img = Image.open(filename)
            image_dir = os.path.dirname(filename)

            output_folder = os.path.join(image_dir, "converted files")

            os.makedirs(output_folder, exist_ok=True)

            new_filename = os.path.join(output_folder, os.path.basename(filename))

            base_name = os.path.splitext(new_filename)[0]
            try:
                if(self.type.currentText() == ".png"):
                    new_filename = base_name + ".png"
                    img.save(new_filename, "PNG")
                    if (self.language == "eng"):
                        print("converted image:", new_filename)
                    elif (self.language == "ukr"):
                        print("конвертовано зображення:", new_filename)

                elif(self.type.currentText() == ".jpg"):
                    new_filename = base_name + ".jpg"
                    img.save(new_filename, "JPG")
                    if (self.language == "eng"):
                        print("converted image:", new_filename)
                    elif (self.language == "ukr"):
                        print("конвертовано зображення:", new_filename)

                elif(self.type.currentText() == ".jpeg"):
                    new_filename = base_name + ".jpeg"
                    img.save(new_filename, "JPEG")
                    if (self.language == "eng"):
                        print("converted image:", new_filename)
                    elif (self.language == "ukr"):
                        print("конвертовано зображення:", new_filename)
            except Exception as e:
                if (self.language == "eng"):
                    print("error when saving an image:", e)
                elif (self.language == "ukr"):
                    print("помилка при збереженнi зображення:", e)

    def openFileDialog(self):
        self.selected_files_list.clear()
        self.images_list = []
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFiles)
        if (self.language == "eng"):
            file_dialog.setNameFilter("images (*.png *.jpg *.jpeg)")
        elif (self.language == "ukr"):
            file_dialog.setNameFilter("зображення (*.png *.jpg *.jpeg)")

        if file_dialog.exec_():
            filenames = file_dialog.selectedFiles()
            self.images_list = filenames
            for filename in filenames:
                if(self.language == "eng"):
                    print("selected file:", filename)
                elif(self.language == "ukr"):
                    print("вибраний файл:", filename)
                self.selected_files_list.addItem(filename)

    def lang(self):
        if(self.language == "eng"):
            self.language = "ukr"
        elif(self.language == "ukr"):
            self.language = "eng"
        if(self.language == "eng"):
            self.label_converTo.setText("convert to:")
            self.convertButton.setText("convert")
            self.selected_files_list_label.setText("selected files:")
            self.configure.setText("select files...")
            self.languageSwitch.setText("мова")
            print(f"language has been changed to {self.language}")
        elif(self.language == "ukr"):
            self.label_converTo.setText("конвертувати в:")
            self.convertButton.setText("конвертувати")
            self.selected_files_list_label.setText("вибранi файли:")
            self.configure.setText("вибрати файли...")
            self.languageSwitch.setText("language")
            print(f"language has been changed to {self.language}")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ez converter"))
        self.convertButton.setText(_translate("MainWindow", "convert"))
        self.title.setText(_translate("MainWindow", "ez converter"))
        self.configure.setText(_translate("MainWindow", "select files..."))
        self.label_converTo.setText(_translate("MainWindow", "convert to:"))
        self.selected_files_list_label.setText(_translate("MainWindow", "selected files:"))
        self.type.setItemText(0, _translate("MainWindow", ".png"))
        self.type.setItemText(1, _translate("MainWindow", ".jpg"))
        self.type.setItemText(2, _translate("MainWindow", ".jpeg"))
        self.languageSwitch.setText(_translate("MainWindow", "мова"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
