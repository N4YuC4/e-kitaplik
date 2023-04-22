from bookshelf import * 

"""
___TO-DO___
-sqlite entegre et
"""

def tanımla():
    global book
    book=bookshelf(input("Kitap adı giriniz:"),input("Yayın evini giriniz:"),input("Yazarı giriniz:"))

def secim():
    i =input("""
    1)kitap ekle
    2)kitap çıkar
    3)listele
    işlemi seçiniz:
    """)
    match i:
        case "1":
            tanımla()
            bookshelf.ekle(book)
            secim()
        case "2":
            bookshelf.sil()
            secim()
        case "3":
            bookshelf.listele()
            secim()

secim()