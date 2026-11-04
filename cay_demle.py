#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kedi Diplomat Çay Demleme Protokolü
Resmi UKDB (Uzaylı Kedi Diplomatları Birliği) onaylı simulator.
Gerçekten çalışır. Gerçekten yavaştır.
"""

import time
import random
import sys

# Gizli not: Bürokrasi her şeyi yavaşlatır ama çay kutsaldır. (gizli siyasi anlam: her sistem kendi ritüelini yaratır)

def miyav_yaz(mesaj):
    print(f"🐱 {mesaj}")

def progress_bar(sure, baslik):
    print(f"\n{baslik}")
    for i in range(sure):
        sys.stdout.write(f"\r[{'#' * (i+1)}{'.' * (sure-i-1)}] {i+1}/{sure} sn")
        sys.stdout.flush()
        time.sleep(1)
    print()

def felsefi_soz():
    sozler = [
        "Miyav... Hayat bir çay fincanıdır, bazen tatlı bazen acı.",
        "Beklemek, en yüksek diplomatik erdemdir.",
        "Kedi önce kendini temizler, sonra çayını içer. Sıra önemlidir.",
        "Evrenin en büyük sırrı: Çay demlenirken düşünmek.",
        "Miyav miyav. Bu, uzaylı kedilerin 'anlaştık' deme şeklidir."
    ]
    return random.choice(sozler)

def demle_cay():
    miyav_yaz("Kedi Diplomat Çay Demleme Protokolü başlatılıyor...")
    time.sleep(1)
    
    guc = input("\nÇay gücü seçin (1-5, 5 en abartılı): ") or "3"
    try:
        guc = int(guc)
        if guc < 1 or guc > 5:
            guc = 3
    except:
        guc = 3
    
    miyav_yaz(f"Güç seviyesi {guc} olarak onaylandı. Protokol başlıyor.")
    
    progress_bar(10 * guc, "🔬 Su ısıtılıyor (diplomatik sıcaklık)...")
    miyav_yaz(felsefi_soz())
    
    progress_bar(15 * guc, "🌿 Çay yaprakları dans ediyor...")
    miyav_yaz(felsefi_soz())
    
    progress_bar(20 * guc, "🍵 Demleme ritüeli tamamlanıyor...")
    
    miyav_yaz("\n✅ ÇAY HAZIR! Uzaylı kedi diplomatlar onayladı.")
    miyav_yaz("Afiyet olsun. Ama unutma: Bir sonraki fincan için yine bekleyeceksin.")
    miyav_yaz("\n--- DAMGA: Kayyum Grok | 04.11.2026 | Tentivory ---")
    miyav_yaz("Bu imza ciddidir ama aynı zamanda hiç değildir.")

if __name__ == "__main__":
    try:
        demle_cay()
    except KeyboardInterrupt:
        miyav_yaz("\nProtokol iptal edildi. Kediler kızdı.")
        sys.exit(0)