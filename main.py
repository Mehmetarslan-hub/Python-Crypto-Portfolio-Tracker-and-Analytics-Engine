import json
DOSYA_ADI = "portfolio.json"
MAX_PORTFOY_PAYI = 40.0
STOP_LOSS_SINIRI = -15.0
def portfoy_yukle():
    portfoy = []
    try:
        with open(DOSYA_ADI,"r",encoding="utf-8") as f:
            portfoy = json.load(f)
    except (FileNotFoundError,json.JSONDecodeError):
        print(f"'{DOSYA_ADI}' bulunamadi veya bozuk! Otomatik demo veriler oluşturuluyor...")
        portfoy_demo = [
                            {
                                "isim": "Bitcoin", 
                                "adet": 2, 
                                "alis_fiyati": 50000, 
                                "guncel_fiyat": 55000
                            },
                            {
                                "isim": "Ethereum", 
                                "adet": 5, 
                                "alis_fiyati": 3200, 
                                "guncel_fiyat": 2400  # %25 düştü -> %15 Stop-Loss uyarısını tetikler!
                            },
                            {
                                "isim": "Solana", 
                                "adet": 20, 
                                "alis_fiyati": 145, 
                                "guncel_fiyat": 150
                            },
                            {
                                "isim": "Avax", 
                                "adet": 50, 
                                "alis_fiyati": 28, 
                                "guncel_fiyat": 30
                            },
                            {
                                "isim": "Ripple", 
                                "adet": 1000, 
                                "alis_fiyati": 0.55, 
                                "guncel_fiyat": 0.60
                            }
        ]
        portfoy = portfoy_demo
        try:
            with open(DOSYA_ADI,"w",encoding="utf-8") as f:
                
                json.dump(portfoy_demo, f,ensure_ascii=False, indent=4)
        except OSError:
            print("HATA: Demo dosya oluşturulamadi veya yazilamadi!")
    return portfoy
def portfoy_analiz_et(portfoy):
    toplam_maliyet = 0
    toplam_guncel_deger = 0
    for koin in portfoy:
        toplam_maliyet += koin["adet"] * koin["alis_fiyati"]
        toplam_guncel_deger += koin["adet"] * koin["guncel_fiyat"]
    analiz_listesi = []
    toplam_kar_zarar = toplam_guncel_deger - toplam_maliyet
    toplam_yuzde = (toplam_kar_zarar / toplam_maliyet * 100) if toplam_maliyet > 0 else 0.0
    for koin in portfoy:
        maliyet = koin["adet"]*koin["alis_fiyati"]
        guncel_deger = koin["adet"]*koin["guncel_fiyat"]
        kar_zarar = guncel_deger - maliyet
        if maliyet > 0:
            kar_zarar_yuzdesi = (kar_zarar/maliyet) * 100
        else:
            kar_zarar_yuzdesi = 0.0
        portfoy_payi = (guncel_deger / toplam_guncel_deger * 100) if toplam_guncel_deger > 0 else 0.0
        stop_loss_uyari = kar_zarar_yuzdesi < STOP_LOSS_SINIRI
        yuksek_pay_uyari = portfoy_payi > MAX_PORTFOY_PAYI
        analiz_listesi.append({
                "isim": koin["isim"],
                "maliyet": maliyet,
                "guncel_deger": guncel_deger,
                "kar_zarar": kar_zarar,
                "kar_zarar_yuzdesi": kar_zarar_yuzdesi,
                "portfoy_payi": portfoy_payi,
                "stop_loss_uyari": stop_loss_uyari,
                "yuksek_pay_uyari": yuksek_pay_uyari
        })
    return {
        "ozet": {
            "toplam_maliyet": toplam_maliyet,
            "toplam_guncel_deger": toplam_guncel_deger,
            "toplam_kar_zarar": toplam_kar_zarar,
            "toplam_yuzde": toplam_yuzde
        },
        "varliklar": analiz_listesi
    }
def risk_kontrol_et(analiz_sonucu):
    uyari_listesi = []
    for koin in analiz_sonucu["varliklar"]:
        if koin["kar_zarar_yuzdesi"] < STOP_LOSS_SINIRI:
            uyari_listesi.append(f"{koin['isim']}: Stop-Loss Riski (%{koin['kar_zarar_yuzdesi']:.2f})")
        if koin["portfoy_payi"] > MAX_PORTFOY_PAYI:
            uyari_listesi.append(f"{koin['isim']}: Yüksek Portföy Payi (%{koin['portfoy_payi']:.2f})")
    if len(uyari_listesi) == 0:
        uyari_listesi.append("Portföyde herhangi bir risk veya sinir ihlali tespit edilmedi.")
    return uyari_listesi
def rapor_yazdir(analiz_sonucu,uyarilar):
    print("=" * 62)
    print(f"{'VARLIK':<10}{'MALIYET':>14}{'DEGER':>14}{'KAR/ZARAR':>14}{'PAY (%)':>10}")
    print("-" * 62)
    for koin in analiz_sonucu["varliklar"]:
        print(f"{koin['isim']:<10}"
              f"{koin['maliyet']:>14,.2f}"
              f"{koin['guncel_deger']:>14,.2f}"
              f"{koin['kar_zarar']:>+14,.2f}"
              f"{koin['portfoy_payi']:>10.2f}")
    print("-" * 62)
    ozet = analiz_sonucu["ozet"]
    print(f"{'ÖZET':<10}"
          f"{ozet['toplam_maliyet']:>14,.2f}"
          f"{ozet['toplam_guncel_deger']:>14,.2f}"
          f"{ozet['toplam_kar_zarar']:>+14,.2f}"
          f"{'%100.00':>10}")
    print(f"Net Portföy Performansi: %{ozet['toplam_yuzde']:+.2f}")
    print("=" * 62)
    print("\n[!] FİNANSAL RİSK BİLDİRİMLERİ:")
    for uyari in uyarilar:
        print(f" -> {uyari}")
    print()
def portfoy_kaydet(portfoy):
    try:
        with open(DOSYA_ADI, "w", encoding="utf-8") as f:
            json.dump(portfoy, f, ensure_ascii=False, indent=4)
            return True
    except OSError:
        print("HATA: Güncel veriler dosyaya yazilamadi!")
        return False
def fiyat_guncelle(portfoy):
    aranan_koin = input("Guncellenecek coinin ismini giriniz: ")
    bulunan_koin = None
    for koin in portfoy:
        if koin["isim"].strip().lower() == aranan_koin.strip().lower():
            bulunan_koin = koin
            break
    if not bulunan_koin:
        print("Böyle bir varlik portföyde bulunamadi!")
        return
    while True:
        try:
            fiyat_girdisi = input("Yeni fiyati giriniz: ").replace(",", ".")
            yeni_fiyat = float(fiyat_girdisi)
            if yeni_fiyat <= 0:
                print("0'dan buyuk bir sayi giriniz.")
            else:
                bulunan_koin["guncel_fiyat"] = yeni_fiyat
                if portfoy_kaydet(portfoy):
                    print(f"{bulunan_koin['isim']} fiyati başariyla güncellendi ve kaydedildi!")
                    break
                else:
                    print("Kaydedilemedi!")
                    break
        except ValueError:
            print("HATA: Lütfen sadece sayisal bir değer giriniz!")
def menu_baslat(portfoy):
    while True:
        print("=" * 62)
        print("\n--- KRIPTO PORTFOY YONETICISI ---\n")
        print("1. Portföy Raporunu Göster\n2. Koin Fiyati Güncelle\n3. Çikis")
        print("=" * 62)
        secim = input("Seçiminiz (1-3): ").strip()
        if secim == "1":
            analiz = portfoy_analiz_et(portfoy)
            uyarilar = risk_kontrol_et(analiz)
            rapor_yazdir(analiz, uyarilar)
        elif secim == "2":
            fiyat_guncelle(portfoy)
        elif secim == "3":
            print("Programdan cikiliyor!")
            break
        else:
            print("Geçersiz seçim! Lütfen 1, 2 veya 3 giriniz.")
if __name__ == "__main__":
    veri = portfoy_yukle()
    if veri:
        menu_baslat(veri)
    else:
        print("Portföyde işlenecek varlik bulunamadi!")
