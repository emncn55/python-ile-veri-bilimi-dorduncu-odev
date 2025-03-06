import os
import json
import time
from datetime import datetime

def teorik_sorular():
    print("1. Dosya açma modları:\n")
    print("   - 'r': Okuma modu. Dosya yoksa hata verir.")
    print("   - 'w': Yazma modu. Dosya varsa içeriği silinir.")
    print("   - 'a': Ekleme modu. Dosyanın sonuna ekleme yapar.")
    print("   - 'x': Yeni bir dosya oluşturur. Dosya varsa hata verir.")
    print("   - 'b': İkili (binary) mod. Resim, ses gibi dosyalar için kullanılır.")
    print("   - 't': Metin modu (varsayılan). Metin dosyaları için kullanılır.\n")
    
    print("2. read(), readline() ve readlines() farkları:\n")
    print("   - read(): Tüm dosyayı string olarak okur.")
    print("   - readline(): Bir satır okur.")
    print("   - readlines(): Dosyanın tüm satırlarını liste olarak döndürür.\n")
    
    print("3. with open(...) kullanmanın avantajları:")
    print("   - Dosyanın otomatik olarak kapanmasını sağlar.\n")
    
    print("4. JSON formatı ve kullanımı:")
    print("   - JSON (JavaScript Object Notation), veri saklama ve veri alışverişi için kullanılan bir formattır.")
    print("   - Web servisleri, API’ler ve konfigürasyon dosyaları gibi durumlarda kullanılır.\n")
    
    print("5. Bir dosyanın var olup olmadığını kontrol etmek için os modülü kullanılır:")
    print("Örnek Kod:")
    print("\nif os.path.exists('dosya.txt'):\n    print('Dosya mevcut.')\nelse:\n    print('Dosya bulunamadı.')\n")

def ogrenci_dosyasi():
    with open("ogrenciler.txt", "a") as dosya:
        while True:
            isim = input("Öğrenci ismi girin (çıkmak için 'bitti' yazın): ")
            if isim.lower() == "bitti":
                break
            dosya.write(isim + "\n")

def ogrenci_listele():
    with open("ogrenciler.txt", "r") as dosya:
        print("Öğrenci Listesi:")
        print(dosya.read())

def gunluk_yaz():
    with open("gunluk.txt", "a") as dosya:
        while True:
            not_ = input("Günlük notunuzu girin ('goruntule' veya 'sil' yazabilirsiniz): ")
            if not_ == "goruntule":
                gunluk_oku()
                return
            elif not_ == "sil":
                os.remove("gunluk.txt")
                print("Günlük silindi.")
                return
            dosya.write(not_ + "\n")

def gunluk_oku():
    if os.path.exists("gunluk.txt"):
        with open("gunluk.txt", "r") as dosya:
            print("Günlük Kayıtları:")
            print(dosya.read())
    else:
        print("Günlük dosyası bulunamadı.")

def json_kullanici_ekle():
    kullanicilar = []
    if os.path.exists("kullanicilar.json"):
        with open("kullanicilar.json", "r") as dosya:
            kullanicilar = json.load(dosya)
    while True:
        ad = input("Ad: ")
        soyad = input("Soyad: ")
        yas = input("Yaş: ")
        kullanicilar.append({"ad": ad, "soyad": soyad, "yas": yas})
        with open("kullanicilar.json", "w") as dosya:
            json.dump(kullanicilar, dosya)
        if input("Başka kullanıcı eklemek ister misiniz? (e/h): ") == "h":
            break

def json_kullanicilari_listele():
    if os.path.exists("kullanicilar.json"):
        with open("kullanicilar.json", "r") as dosya:
            kullanicilar = json.load(dosya)
            for kullanici in kullanicilar:
                print(kullanici)

def telefon_rehberi():
    while True:
        komut = input("Komut girin (ekle, ara, listele, çık): ")
        if komut == "ekle":
            with open("rehber.txt", "a") as dosya:
                ad = input("İsim: ")
                numara = input("Telefon: ")
                dosya.write(f"{ad}: {numara}\n")
        elif komut == "ara":
            isim = input("Aranacak isim: ")
            with open("rehber.txt", "r") as dosya:
                for satir in dosya:
                    if isim in satir:
                        print(satir.strip())
        elif komut == "listele":
            with open("rehber.txt", "r") as dosya:
                print(dosya.read())
        elif komut == "çık":
            break

def log_sistemi():
    while True:
        with open("log.txt", "a") as dosya:
            dosya.write(f"Sistem Çalışıyor: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        time.sleep(10)

def log_goruntule():
    with open("log.txt", "r") as dosya:
        print(dosya.read())
