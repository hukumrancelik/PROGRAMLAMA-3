import sys
from PyQt4.QtGui import *

metin = "<center>tükeilen yakıt tutarı</center>"
 
grid = QGridLayout()
baslik = QLabel(metin)
yol = QLabel('gideceğiniz yol')
yakıt = QLabel('yakıt fiyatı ')

km = QLabel('100 km de tüketilen yakıt ')
yoldeger = QLineEdit()
yakıtdeger = QLineEdit()
kmDeger = QLineEdit()

sonuc = QLabel('toplam tutar ')
sonucDeger = QLabel('0.00')
hesapla = QPushButton('Hesapla')
 

grid.addWidget(baslik)
grid.addWidget(yol)
grid.addWidget(yoldeger)
grid.addWidget(yakıt)
grid.addWidget(yakıtdeger)
grid.addWidget(km)
grid.addWidget(kmDeger)
grid.addWidget(sonuc)
grid.addWidget(sonucDeger)
grid.addWidget(hesapla)                                                                                                                                                                                                                                                                                                                                 
 

setLayout(self.grid)
setWindowTitle("akaryakıt hesaplama")
 
 
uyg = QApplication([])
pencere=yakıtHesapla()
pencere.show()
grid.show()
