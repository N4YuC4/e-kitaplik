import sqlite3 as sl
import termtables
class bookshelf():
    def __init__(self,ad,yayınevi,yazar):
        self.ad=ad
        self.yevi=yayınevi
        self.yazar=yazar

    @staticmethod
    def tablo_olustur():
        with sl.connect("kitaplık.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS kitaplık(
                            ad text,
                            yayın_evi text,
                            yazar text
                        )""")
            
    @staticmethod
    def listele():
        with sl.connect("kitaplık.db") as conn:
            cursor=conn.cursor()
            cursor.execute("select count(*) from kitaplık")
            satır_sayısı=cursor.fetchone()[0]
            cursor.execute("select * from kitaplık")
            liste=[]
            başlık=["No.","Kitap İsmi","Yayın Evi","Yazar"]
            for satır,s_id in zip(cursor.fetchall(),range(1,satır_sayısı+1)):
                liste.append([s_id,satır[0],satır[1],satır[2]])
            try:
                
                termtables.print(liste,başlık)
            except ValueError:
                print("veri bulunamadı")

    @staticmethod
    def sil():
        with sl.connect("kitaplık.db") as conn:
            cursor=conn.cursor()
            bookshelf.listele()
            silinecek=input("Silinmesini istediğiniz kitabın numarasını giriniz:")
            cursor.execute("DELETE from kitaplık where rowid= ?",silinecek)

    
    def ekle(self):
        with sl.connect("kitaplık.db") as conn:
            bookshelf.tablo_olustur()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO kitaplık VALUES (?, ?, ?)", (str(self.ad).lower(), str(self.yevi).lower(), str(self.yazar).lower()))