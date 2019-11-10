from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit,QInputDialog, QApplication,QMessageBox
from PyQt5.QtGui import *
from password_generator import *
import random
import os
import datetime

class Ui_Form(object):

    def hepsini_kaydet(self):
        try:
            path = os.path.expanduser('~')
            path = path + "\Desktop"
            istikamet = path + "\Parolalar"
            try:
                os.mkdir(istikamet)
            except:
                print("var olan dosya")
            dosya_yolu = istikamet + "\Kayıtlı Parolalar.txt"
            dosya = open(dosya_yolu, "a")
            an = datetime.datetime.today()
            toplam = "{}/{}/{} | {}:{} | Parolalar: ".format(an.year, an.month, an.day, an.hour, an.minute)
            yazi = toplam + str(self.sifreler) + "\n"
            dosya.write(yazi)
        except:
            print("hata")

    def miktar_hata(self):
        buttonReply = QMessageBox.critical(None, "Miktar hatası", "Lütfen 8 veya daha büyük sayı giriniz.",
                                           QMessageBox.Ok)

    def fonk_kaydet(self):
        try:
            for item in self.liste.selectedItems():
                print(item.text())
                try:
                    path = os.path.expanduser('~')
                    path = path + "\Desktop"
                    istikamet = path + "\Parolalar"
                    try:
                        os.mkdir(istikamet)
                    except:
                        print("var olan dosya")
                    d, okbabba=QInputDialog.getText(None,"Ne Şifresi ?","Lütfen ne şifresi olduğunu giriniz.")
                    if d != "":
                        dosya_yolu = istikamet + "\Kayıtlı Parolalar.txt"
                        dosya = open(dosya_yolu, "a")
                        an = datetime.datetime.today()
                        toplam = "{}/{}/{} | {}:{} | {} parolası: ".format(an.year, an.month, an.day, an.hour, an.minute,d)
                        yazi = toplam + str(item.text()) + "\n"
                        dosya.write(yazi)

                    else:
                        QMessageBox.critical(None, "HATA", "Lütfen ne şifresi olduğunu giriniz. ",
                                             QMessageBox.Ok)
                except:
                    print("hata")
        except:
            print("hata")

    def olustur(self):
        if self.radioButton.isChecked() ==True:
            try:
                if int(self.aralik.text()) < 8:
                    self.miktar_hata()
                    return
                pwo = PasswordGenerator()
                pwo.minlen = int(self.aralik.text())
                pwo.maxlen = int(self.aralik.text())
                guclu_parola = pwo.generate()
                self.sifreler.append(guclu_parola)
                print(self.sifreler)
                self.liste.addItem(guclu_parola)
            except:
                print("hata-Güçü")
                self.miktar_hata()
                return

        elif self.radioButton_2.isChecked() ==True:

            try:
                if int(self.aralik.text()) < 8:
                    self.miktar_hata()
                    return
                y = ''.join(random.choice(self.medium_sifreler))
                self.sifreler.append(y)
                self.liste.addItem(y)
                print(self.sifreler)
            except:
                print("haataaaa -Orta")
                self.miktar_hata()
                return

        elif self.radioButton_3.isChecked() ==True:
           try:
               if int(self.aralik.text()) < 8:
                   self.miktar_hata()
                   return
               zayif_parola = int(''.join([str(random.randint(0,10)) for _ in range(int(self.aralik.text()))]))
               self.sifreler.append(zayif_parola)
               self.liste.addItem(str(zayif_parola))

               print(self.sifreler)
           except:
               print("hata - zayıf")
               self.miktar_hata()
               return
        else:
            QMessageBox.critical(None, "Hata", "Lütfen parolanın ne kadar güçlü olacağını seçin",
                                               QMessageBox.Ok)

    def setupUi(self, Form):
        Form.setWindowIcon(QtGui.QIcon('logo_son.png'))
        Form.setObjectName("Güçlü Şifre Oluşturucu")
        Form.resize(299, 259)
        Form.setFixedSize(299, 259)
        self.medium_sifreler = ['RzW6F0Xm', 'qmjiVOFh', '83dPuKrk', 'q2ZrIt4j', 'uScj8Zct', 'QSvpz0Y4', '3TDiIslR',
                                '19lRJCi4', 's22yi7pW', 'CDaJWfpW', 'USkBMe2R', 'iwbAIKRW', 'Vu60LRBJ', 'y4c72lZS',
                                'TEgK06gp', 'EqDjUyy2', '3VZD8O1p', 'dlSm50Bc', '1yy0WvhK', '7H2keW3Q', 'U14QiZyj',
                                'FyEmW0f4', 'DIpsU149', 'hnBqUA96', 'aQnPDiy8', '86KcWWJH', 'SDtit1Nt', 'dQw5uxGb',
                                'Wa4JTdE4', 'MmvQWVeo', 'qHUP4jkD', '700jj8OQ', '0TcrxpTZ', 'Kro4McZH', '6SRAGpun',
                                'h9faYk4M', 'KynRUmdB', 'GnE6kIps', 'vJsZ8ctr', 'RqQukycw', 'u3fS61NY', 'SWeTGbQX',
                                'OOIcoYn5', 'UhyTXLrF', 'ftxpGcxg', 'LJbn0Tez', 'PmTAiVdl', 'uzVl3Wi5', 'dJHjrJj7',
                                'KDaLti7a', 'k8giLrBt', 'auef3i07', 'Vi5sIcbf', 'ttC92Gvu', '1KIIdadK', '7LyuX0WT',
                                'YMFKhpTx', 'VkYEjJPC', '2ii8XGPR', 'HANKNQVe', 'UsUD7Hpx', 'qZ56MK7f', 'PAKSve1r',
                                '52PBOMRN', 'UKi90MEO', 'p0bpajM7', 'YaROF7ww', 'wfvxbTzR', 'ckJ7jfrk', 'piZ4jciu',
                                'sasThACV', '8wod5jH3', 'FlUafFs7', '9jaHFGPn', 'VBEUrDhL', 'VfmYG7gX', 'ylxoRikV',
                                'HwmWOJ1C', 'sAmgcQfa', 'cS2SINUw', '1cuzrGHH', 'VzPHYyXR', 'uDf6a799', 'pr7IVdV7',
                                'jCa3LMU1', 'izwweawH', 'hBoopHCk', 'fV5J3kGZ', 'k9naJQTf', 'Zsirxk5z', 'X5inu90U',
                                'AoKk5AWe', 'AeBxjuuN', '6s1Wdcfh', 'nijZrViF', 'TYTu7RKB', 'Ymd0t4FS', 'UnwScLpe',
                                '2yS655ZI', 'tRMeD0pL', 'dm4QlVXH', '902iqftp', 'iQ5bbYcT', '3eAaP73d', 'oAPOTHZn',
                                'IPEwjyiR', 'svbR7yqD', 'dyhz6jHO', 'qKt7p4KJ', '0Uf0EBv6', 'IQK8e9fz', 'I0DJKZED',
                                'DxNpD2rV', 'M21sOq00', 'KoCzjIhr']
        self.guc = ""
        self.guclu_sifre = ""
        self.orta_sifre = ""
        self.zayif_sifre = ""
        self.sifreler = []


        self.liste = QtWidgets.QListWidget(Form)
        self.liste.setGeometry(QtCore.QRect(10, 100, 171, 151))
        self.liste.setObjectName("liste")

        self.soru_label = QtWidgets.QLabel(Form)
        self.soru_label.setGeometry(QtCore.QRect(90, 10, 200, 16))
        self.soru_label.setObjectName("soru_label")

        self.Olustur = QtWidgets.QPushButton(Form)
        self.Olustur.setGeometry(QtCore.QRect(110, 50, 161, 23))
        self.Olustur.clicked.connect(self.olustur)
        self.Olustur.setObjectName("Olustur")

        self.kaydet = QtWidgets.QPushButton(Form)
        self.kaydet.setGeometry(QtCore.QRect(190, 99, 95, 23))
        self.kaydet.clicked.connect(self.fonk_kaydet)
        self.kaydet.setObjectName("kaydet")

        self.allkaydet = QtWidgets.QPushButton(Form)
        self.allkaydet.setGeometry(QtCore.QRect(190, 125, 95, 23))
        self.allkaydet.clicked.connect(self.hepsini_kaydet)
        self.allkaydet.setObjectName("allkaydet")

        self.aralik = QtWidgets.QLineEdit(Form)
        self.aralik.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.aralik.setObjectName("aralik")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.colorCount()
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")

        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Güçlü Şifre Oluşturucu"))
        self.soru_label.setText(_translate("Form", "Şifreniz kaç karakterli olsun? (8-1000)"))
        self.Olustur.setText(_translate("Form", "OLUŞTUR"))
        self.kaydet.setText(_translate("Form", "KAYDET"))
        self.allkaydet.setText(_translate("Form","HEPSİNİ KAYDET"))
        self.radioButton.setText(_translate("Form", "Güçlü"))
        self.radioButton_2.setText(_translate("Form", "Orta"))
        self.radioButton_3.setText(_translate("Form", "Zayıf"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

