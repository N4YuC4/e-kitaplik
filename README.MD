# E-Kitaplık 📚

E-Kitaplık, kişisel kütüphanenizi dijital ortamda yönetmenizi sağlayan, Python ile geliştirilmiş terminal tabanlı bir uygulamadır. Kitaplarınızı veritabanına kaydedebilir, detaylı listeleyebilir ve dilediğiniz zaman silebilirsiniz.

## 🚀 Özellikler

* **Kitap Ekleme:** Kitap adı, yayınevi ve yazar bilgileriyle yeni kayıt oluşturma.
* **Listeleme:** Kayıtlı kitapları `termtables` kullanarak düzenli bir tablo formatında görüntüleme.
* **Kitap Silme:** Listeden seçilen kitabı ID numarasına göre veritabanından kaldırma.
* **Kalıcı Veritabanı:** SQLite (`kitaplık.db`) kullanımı sayesinde verileriniz program kapansa bile saklanır.

## 🛠️ Gereksinimler

Bu projeyi çalıştırabilmek için bilgisayarınızda Python 3'ün yüklü olması gerekir. Ayrıca görsel tablolar oluşturmak için harici bir kütüphane kullanılmaktadır:

* Python 3.x
* `termtables` kütüphanesi

## 📥 Kurulum

Projeyi bilgisayarınıza indirdikten sonra, gerekli olan `termtables` kütüphanesini kurmak için terminalde şu komutu çalıştırın:

```bash
pip install termtables
````

## ▶️ Kullanım

Uygulamayı başlatmak için proje dizininde terminali açın ve `main.py` dosyasını çalıştırın:

```bash
python main.py
```

### Menü Seçenekleri:

1.  **Kitap Ekle:** Sizden sırasıyla "Kitap Adı", "Yayınevi" ve "Yazar" ismini girmenizi ister ve veritabanına kaydeder.
2.  **Kitap Çıkar:** Mevcut kitapları listeler ve silmek istediğiniz kitabın numarasını (ID) girmenizi bekler.
3.  **Listele:** Kütüphanenizdeki tüm kitapları No, Kitap İsmi, Yayın Evi ve Yazar sütunlarıyla tablo halinde gösterir.

## 📂 Proje Yapısı

  * `main.py`: Uygulamanın ana dosyasıdır. Kullanıcı menüsü (ekleme, silme, listeleme seçimleri) burada yönetilir.
  * `bookshelf.py`: Veritabanı bağlantısı, tablo oluşturma (CREATE), veri ekleme (INSERT), silme (DELETE) ve listeleme (SELECT) gibi arka plan işlemlerini yapan `bookshelf` sınıfını içerir.
  * `kitaplık.db`: Program ilk kez çalıştırıldığında otomatik oluşturulan SQLite veritabanı dosyasıdır.

## 📝 Yapılacaklar (To-Do)

Gelecek sürümlerde eklenmesi planlanan özellikler:

  - [ ] Grafiksel Kullanıcı Arayüzü (GUI) eklenmesi.
  - [ ] ISBN numarası ile otomatik kitap tarama ve bilgi çekme.
  - [ ] Yazar veya kitap adına göre arama filtresi.

## 🤝 Katkıda Bulunma

1.  Bu projeyi forklayın.
2.  Yeni bir özellik dalı (feature branch) oluşturun (`git checkout -b yeni-ozellik`).
3.  Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`).
4.  Dalınızı pushlayın (`git push origin yeni-ozellik`).
5.  Bir Pull Request oluşturun.

-----

*Bu proje açık kaynaklıdır ve geliştirilmeye açıktır.*
