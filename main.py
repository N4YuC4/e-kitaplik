"""
___TO-DO___
-sqlite entegre et
"""

import sqlite3 as sl
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

    def ekle(self):
        with sl.connect("kitaplık.db") as conn:
            bookshelf.tablo_olustur()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO kitaplık VALUES (?, ?, ?)", (self.ad, self.yevi, self.yazar))

book=bookshelf(input("Kitap adı giriniz:"),input("Yayın evini giriniz:"),input("Yazarı giriniz:"))

bookshelf.ekle(book)