"""
___TO-DO___
-sqlite entegre et
"""

import sqlite3 as sl
class bookshelf():
    def __init__(self,ad,yayınevi,yazar) -> None:
        self.ad=ad
        self.yevi=yayınevi
        self.yazar=yazar

    def tablo_olustur():
        db= sl.connect("kitaplık.db")
        crsr=db.cursor()    
        crsr.execute("""CREATE TABLE IF NOT EXISTS KİTAPLIK(
                    AD text,
                    YAYIN_EVİ text,
                 YAZAR text
        )""")
        db.commit()
        db.close()

    def ekle(kitap):
        db= sl.connect("kitaplık.db")
        crsr=db.cursor()
        bookshelf.tablo_olustur()
        crsr.execute("INSERT INTO KİTAPLIK VALUES (?,?,?)",(kitap))
        db.commit()
        db.close()

book=bookshelf("drga","tgatha","hath")
kitap=(book.ad,book.yazar,book.yevi)
print(kitap)

bookshelf.ekle(kitap)