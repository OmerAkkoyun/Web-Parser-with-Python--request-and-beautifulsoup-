import sys,os,requests

from bs4 import BeautifulSoup

from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPainter, QColor, QPen,QIcon

from PyQt5 import QtWidgets, QtGui

from PyQt5.QtWidgets import QMainWindow,QMessageBox#Uyarı vereceğimiz için gerekli modul messegebox

from PyQt5.QtWidgets import QWidget,QApplication,QTextEdit,QLabel,QPushButton,QVBoxLayout

from PyQt5.QtWidgets import QInputDialog, QLineEdit,QAction,qApp,QFileDialog,QHBoxLayout





class Pencere(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        try:
            newpath = r'C:\File'
            if not os.path.exists(newpath):  # bu kodlar  kalsör oluşturma kodudur.
                os.makedirs(newpath)

            self.setWindowIcon(QtGui.QIcon('E:/WorkSpaces/Python/furkan/icon.ico')) # İkon yeri
            self.setWindowTitle("Güncel Haber Takip") #Programın başlığı

            url = "https://finans.haberler.com/haberler/"
            response = requests.get(url)
            html_icerigi = response.content
            soup = BeautifulSoup(html_icerigi, "html.parser")
            self.bilgi = soup.find_all("div", {"class": "general w130 h100"})
            self.setGeometry(675, 300, 650, 550)

    # *********************Butonlarımız *************************
            self.yazi_alani = QTextEdit()
            self.yazi_alani.setReadOnly(True)
            self.yazi_alani.setFont(QtGui.QFont("Arial", 11, weight=QtGui.QFont.Bold))
            self.finans = QPushButton("Finans Haberleri")
            self.doviz = QPushButton("Güncel Döviz Kuru")

            self.aramayap=QLineEdit()
            self.aramayap.setPlaceholderText("Haber Ara ")
            self.aralabel=QPushButton("Ara")
            # self.nolabel=QLabel("Haber No Gir")
            self.haberno=QLineEdit()
            self.haberno.setPlaceholderText("Haber Numarası Gir")
            self.git=QPushButton("Detayı Gör")
            self.siteyegit=QPushButton("Siteye Git→")

            self.sil=QPushButton("Sayfayı Temizle")
            self.word=QPushButton("Haberi Arşivle")
            self.sayi=0

    #*********************Program üzerinde gözükecek içerikler*************************
            v_box = QVBoxLayout()
            v_box.addWidget(self.finans) # önce haberleri göster butonu
            v_box.addWidget(self.doviz)
            v_box.addWidget(self.aramayap)
            v_box.addWidget(self.aralabel)
            v_box.addWidget(self.yazi_alani) # sonra haber yazısı alanı

            self.setLayout(v_box)

            h_box=QHBoxLayout()
            # h_box.addWidget(self.nolabel)
            h_box.addWidget(self.haberno)
            h_box.addWidget(self.git)
            h_box.addWidget(self.siteyegit)
            h_box.addWidget(self.sil)
            h_box.addWidget(self.word)# altta temizle butonu
            v_box.addLayout(h_box)
    #********************************************************************************

            #********Bağlantılarımız**********************************
            self.aralabel.clicked.connect(self.araF)
            self.siteyegit.clicked.connect(self.siteF)
            self.finans.clicked.connect(self.finansF)
            self.doviz.clicked.connect(self.dovizF)
            self.sil.clicked.connect(self.supur)
            self.git.clicked.connect(self.habergetir)
            self.word.clicked.connect(self.arsivle)
            self.show()

    # ********Bağlantılarımız bitti**********************************

            # ‼renk kodları
            self.setAutoFillBackground(True)
            p = self.palette()
            p.setColor(self.backgroundRole(), Qt.gray)  # ‼renk kodları
            self.setPalette(p)

    # *********************************************************************
            # Buton Renkleri-----------------------------------------------------------------
            self.aralabel.setStyleSheet("background-color:#cdc673")
            self.yazi_alani.setStyleSheet("background-color:#ffebcd")
            self.siteyegit.setStyleSheet("background-color:white")
            self.haberno.setStyleSheet("background-color:#e0ffff")
            self.finans.setStyleSheet("background-color:white")
            self.doviz.setStyleSheet("background-color: white")
            self.sil.setStyleSheet("background-color: white")
            self.git.setStyleSheet("background-color: white")
            self.word.setStyleSheet("background-color:white")

     # *********************************************************************

            file = open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "w",
                        encoding="utf-8")  # belgeyi yeniden oluştursun.
            self.sayi = 0
            defa = 0
            for i in self.bilgi:
                while defa < 50:
                    self.sayi += 1

                    i = i.text
                    i = i.lstrip()  # sol taraftaki boşlukları sildik.Güzel görünsün diye

                    a = (self.sayi)  # TEST için. haberler aşağıda gözüksün.
                    a = str(a)  # a yı str yaptık ki metin gibi gözüksün

                    i = a + ". " + i
                    self.i=i

                    file = open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "a", encoding="utf-8")  # Yaz
                    file.write(i)
                    file.write("\n")
                    defa += 1
                    break

            with open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "r", encoding="utf-8") as file:  # Oku

                self.yazi_alani.setText(file.read())

        except:
            QMessageBox.information(self,"bilgi","İnternet Bağlantınızı kontrol edin.")

# --------------------------------------------------------------------------------------------------------------------------------------------

    def finansF(self):

        file = open(os.path.join(os.path.expanduser("C:/File/haber.txt")), "w",
                    encoding="utf-8")  # belgeyi yeniden oluştursun.
        self.sayi = 0
        defa = 0
        for i in self.bilgi:
            while defa < 50:
                self.sayi += 1

                i = i.text
                i = i.lstrip()  # sol taraftaki boşlukları sildik.Güzel görünsün diye

                a = (self.sayi)
                a = str(a)  # a yı str yaptık ki metin gibi gözüksün

                i = a + ". " + i

                file = open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "a", encoding="utf-8")  # Yaz
                file.write(i)
                file.write("\n")
                defa += 1
                break
        with open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "r", encoding="utf-8") as file:  # Oku

            self.yazi_alani.setText(file.read())

        #***************************Link oluştursun aynı zamanda **********************************************
        url = "https://finans.haberler.com/haberler/"
        response = requests.get(url)
        html_icerigi = response.content
        soup = BeautifulSoup(html_icerigi, "html.parser")
        bilgi = soup.find_all("a", {"class": "haber_list"})
        # -----------------------------------------------------------------------
        # -----------------------------------------------------------------------
        file = open(os.path.expanduser("C:/File/links.txt"), "w", encoding="utf-8")  # belgeyi yeniden oluştursun.

        kez = 0
        for i in bilgi:
            linklistesi = []
            while kez < 50:

                i = str(i)
                i = i.replace('class="haber_list"', "")
                i = i.replace('href="', '')
                i = i.replace('<a', '')
                i = i.replace('</a>', '')
                i = i.replace('">', '')
                i = i.replace('"', '')
                a = 0
                for j in range(50):
                    a = str(a)

                    i = i.replace(('id=ContentPlaceHolder1_rptHaberler_linkHaberMetin_' + a), "")
                    a = int(a)
                    a += 1

                linklistesi.append(i.split("/"))  # parçaladık.

                file = open(os.path.expanduser("C:/File/links.txt"), "a",
                            encoding="utf-8")  # belgeyi yeniden oluştursun.
                file.write("/".join(
                    linklistesi[0][0:4]).strip())  # hem / birleştirsin ,hemde baştaki sondaki boşluklar gitsin.
                file.write("\n")

                a = ("/".join(linklistesi[0][0:4]))
                a = a.strip()

                kez += 1
                break

#*****************************************************************************************************************
    def dovizF(self):
        file = open(os.path.expanduser("C:/File/doviz.txt"), "w", encoding="utf-8")  # belgeyi yeniden oluştursun.
        try:
            self.yazi_alani.setAlignment(Qt.AlignCenter)
            url = "https://www.doviz.com/"  # url yi çektik
            response = requests.get(url)  # url yi inceledik parçalamak için
            html_icerigi = response.content  # div class gibi yerlieri görmemizi sağladı
            parcala = BeautifulSoup(html_icerigi, "html.parser")
            bilgi = parcala.find_all("div", {"class": "column2-row2"})
            sayi = 0
            listem = []
            for i in bilgi:
                i = i.text
                listem.append(i)
            isimler = ["Dolar Alış                     :", "Dolar Satış                  :", "Euro Alış                      :",
                       "Euro Satış                   :", "İng Sterlin Alış            :", "İng Sterlin Satış         :",
                       "İsviçre Frangı Alış      :", "İsviçre Frangı Satış   :"]
            a = 0
            b = 2
            for s in range(8):
                file = open(os.path.expanduser("C:/File/doviz.txt"), "a", encoding="utf-8")
                son = (str((isimler[a], listem[b])))
                son = son.replace("'", "")
                 # burda çektiğimiz veriyi budama işlemi yaptık temizledik.
                son = son.replace("(", "")
                son = son.replace(")", "")

                file.write(son)
                file.write("\n")
                a += 1
                b += 1
            with open(os.path.expanduser(os.path.expanduser("C:/File/doviz.txt")), "r",encoding="utf-8") as file:  # Oku
                self.yazi_alani.setText(file.read())
        except:
            self.yazi_alani.setText("Beklenmeyen bir hata oluştu !")
            self.yazi_alani.setAlignment(Qt.AlignCenter) # ortaya aldık metni

# *****************************************************************************************************************
    def araF(self):
        try:

            aramayap = self.aramayap.text()
            aramayapbuyuk=(self.aramayap.text()).capitalize() #Kelimelerin ilk harfini büyüttük.Arama işlemi için.
            buyukharf=(self.aramayap.text()).upper()
            ac = open(os.path.expanduser(os.path.expanduser("C:/File/aranan.txt")), "w", encoding="utf-8")  # belgeyi yeniden oluştursun.
            ac.close()
            sayisi=[]
            dosya=open(os.path.expanduser(os.path.expanduser("C:/File/haber.txt")), "r",encoding="utf-8") # Oku
            for i in dosya:
                if aramayap in i or aramayapbuyuk in i or buyukharf in i:
                    sayisi.append(i)
                    file = open(os.path.expanduser(os.path.expanduser("C:/File/aranan.txt")), "a",encoding="utf-8")  # belgeyi yeniden oluştursun.
                    file.write(i)
                    file.close()

            with open(os.path.expanduser(os.path.expanduser("C:/File/aranan.txt")), "r",encoding="utf-8") as file:  # Oku
                self.yazi_alani.setText(file.read())


            if len(sayisi)<1: # Eğer hiç haber yoksa kelime ile ilgili haber yok uyarısı versin..
                self.yazi_alani.setText("Böyle bir haber bulunamadı.")


        except:
            self.yazi_alani.setText("Beklenmedik Hata !")




# *****************************************************************************************************************
    def supur(self):
        self.yazi_alani.clear()
        self.haberno.clear()
# *****************************************************************************************************************
    def habergetir(self):
        QMessageBox.about(self, "Haber", "Haber Getirilirken Lütfen Bekleyin!")  # mesaj
        try:
            habernumara = self.haberno.text()
            habernumara=int(habernumara)
            if habernumara <1 or habernumara >50:
                self.yazi_alani.setText("Yanlış haber numarası girdiniz... \nLütfen kontrol ederek tekrar deneyin!")
            else:
                habernumara = int(habernumara)
                getir = open(os.path.expanduser("C:/File/links.txt"), "r", encoding="utf-8")
                b = 0
                self.sonlink=[]
                while b < habernumara:
                    for a in getir:
                        a=a.strip()
                        self.sonlink.append(a)
                        b += 1
                        break
                url =(str(self.sonlink[-1]))
                print((self.sonlink[-1]))#☺test için 
				
                response = requests.get(url)
                html_icerigi = response.content
                soup = BeautifulSoup(html_icerigi, "html.parser")
                bilgi = soup.find_all("div", {"class": "haber_metni mb20 detay-v3_3 anou"})
                sayi = 0
                for i in bilgi:
                    sayi += 1
                    i = i.text
                    i = i.replace(
                            '$(window).load(function () { var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = 1; s.src = "//cdn2.admatic.com.tr/showad/showad.js"; el.parentNode.insertBefore(s, el); });',
                            '')
                    i = i.lstrip()  # sol taraftaki boşlukları sildik.Güzel görünsün diye
                    a = (sayi)  # TEST için. haberler aşağıda gözüksün.
                    a = str(a)  # a yı str yaptık ki metin gibi gözüksün
                    i = a + ". " + i
                    file = open(os.path.expanduser("C:/File/detay.txt"), "w",
                                    encoding="utf-8")  # belgeyi yeniden oluştursun.
                    file.write(i)
                    break
                with open(os.path.expanduser(os.path.expanduser("C:/File/detay.txt")), "r",encoding="utf-8") as file:  # Oku
                    self.yazi_alani.setText(file.read())
        except:
            self.yazi_alani.setText("Lütfen Önce Haber Numarası Girin !")
            self.yazi_alani.setAlignment(Qt.AlignCenter)  # metni ortaya aldık
# *****************************************************************************************************************
    def siteF(self):
        import webbrowser
        try:

            habernumara = self.haberno.text()
            habernumara = int(habernumara)

            if habernumara < 1 or habernumara > 50:
                self.yazi_alani.setText("Yanlış haber numarası girdiniz... \nLütfen kontrol ederek tekrar deneyin!")

            else:

                habernumara = int(habernumara)
                getir = open(os.path.expanduser("C:/File/links.txt"), "r", encoding="utf-8")
                b = 0
                self.sonlink = []
                while b < habernumara:
                    for a in getir:
                        a = a.strip()
                        self.sonlink.append(a)
                        b += 1
                        break
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(self.sonlink[-1])

        except:
            self.yazi_alani.setText("Lütfen Önce Haber Numarası Girin !")
            self.yazi_alani.setAlignment(Qt.AlignCenter)  # metni ortaya aldık

# *****************************************************************************************************************
    def arsivle(self):

        open(os.path.expanduser(os.path.expanduser("~/Desktop/Haber.txt")), "w", encoding="utf-8")  # Yaz
        QMessageBox.about(self, "Haber", "Haber Başarıyla Arşivlendi.\nKaydedilen Konum: Masaüstü")  # mesaj
        kayit = open(os.path.expanduser("C:/File/detay.txt"), "r", encoding="utf-8")
        for al in kayit:
            yeni = open(os.path.expanduser(os.path.expanduser("~/Desktop/Haber.txt")), "a", encoding="utf-8")  # Yaz
            yeni.write(al)
            yeni.close()
# *****************************************************************************************************************
app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())