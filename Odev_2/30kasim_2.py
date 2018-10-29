from PyQt4.QtGui import*
from PyQt4.QtCore import* #SIGNAL ı kullanmak için
class ortCls(QDialog): #ekranın en dış kısmı
    def __init__(self,ebeveyn=None):
        super(ortCls,self).__init__(ebeveyn)

        grid=QGridLayout()


        grid.addWidget(QLabel("Dönem Başı Çalışan Sayısı"),0,0)
        self.calisanS=QLineEdit()
        grid.addWidget(self.calisanS,0,1)

        grid.addWidget(QLabel("Dönem Sonu Çalışan Sayısı"),1,0)
        self.calisanSon=QLineEdit()
        grid.addWidget(self.calisanSon,1,1)

        
        grid.addWidget(QLabel("PERSONEL DEVİR HIZI"),2,0)
        self.ortalamaC=QLabel("")
        grid.addWidget(self.ortalamaC,2,1)

        hesapla1=QPushButton("Hesapla")
        self.connect(hesapla1,SIGNAL("pressed()"),self.islem1)
        self.setLayout(grid)
        grid.addWidget(hesapla1,3,0)
        

    def islem1(self):
        a1=int(self.calisanS.text())
        a2=int(self.calisanSon.text())
        
        global sonuc1
        sonuc1=((a1-a2)/a2)
        self.ortalamaC.setText(('<font color="blue"><b>%0.1f</b></font>'%sonuc1))







uygulama=QApplication([])
pencere=ortCls() #çağırdık
pencere.show()

