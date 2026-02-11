#simülasyon oyunu
import random
print("Adada hayatta kalma simülatörüne hoş geldiniz!")
print("Vereceğiniz her karar ada halkının kaderini etkileyecek.")
print("Başlayalım!")
#Başlangıç Değerleri
nufus_gecmisi=[]
gida_kaydi=[100]
günlük_kazanclar=[]
gün=0
nüfus=100
gıda=100
ada_sağlığı=100
teknoloji=0
#Oyun Döngüsü
while nüfus>0 and ada_sağlığı>0:
    kazanç=0
    gün+=1
    print(f"\n {gün}. gün başlıyor.")
    print(f"GÜNCEL DURUM: Nüfus: {nüfus}, Gıda: {gıda}, Ada Sağlığı: {ada_sağlığı}, Teknoloji: {teknoloji}")
    #Seçim Noktası
    print("Bugün ne yapmak istersiniz?")
    print("1- Avlan \n 2- Araştırma yap  \n 3- Dinlen")
    seçim1=input("Seçiminiz (1/2/3): ")
    if seçim1=="1":
        if random.randint(0, 100) < 20:  # %20 ihtimalle vahşi hayvan saldırısı
            print("Avlanırken vahşi hayvan saldırısına uğradınız! Ada sağlığı 20, nüfus 5 azaldı.")
            nüfus = max(0, nüfus - 5)
            ada_sağlığı = max(0, ada_sağlığı - 20)
        kazanç=random.randint(0,30)
        gıda+=kazanç
        ada_sağlığı = max(0, ada_sağlığı - 10)
        if(kazanç==0):
            print("Avlanma başarısız, gıda artmadı. Avlanırken yoruldun, ada sağlığı 10 azaldı.")
        else:
            print(f"Av başarılı! Gıda {kazanç} arttı. Avlanırken yoruldun, ada sağlığı 10 azaldı.")
    elif seçim1=="2":
        if random.randint(0, 100) < 10:  # %10 ihtimalle kaza
            print("Araştırma yaparken bir kaza geçirdiniz! Nüfus 3 azaldı.")
            nüfus = max(0, nüfus - 3)
        if random.randint(0, 100) < 15:  # %15 ihtimalle buluş
            teknoloji=max(0, teknoloji + 5)
            gıda=max(0, gıda - 15)
            print("Büyük bir buluş yaptınız! Teknoloji 5 arttı. Gıda 15 azaldı.")
        else:
            teknoloji=max(0, teknoloji + 1)
            gıda=max(0, gıda - 15)
            print("Araştırma yaptınız. Teknoloji 1 arttı, gıda 15 azaldı.")
    elif seçim1=="3":
        ada_sağlığı = max(0, min(100, ada_sağlığı + 20))
        gıda = max(0, gıda - 15)
        print("Dinlendiniz. Ada sağlığı 20 arttı, gıda 15 azaldı.")
    else:
        gıda=max(0, gıda - 10)
        print("Geçersiz seçim yaptın, gün boşa geçti ada halkı gıda kaybetti.")
    #Rastgele Olaylar
    print("Gün devam ediyor... Acaba neler olacak?")
    olay_ihtimali = 0.6  # %60 ihtimalle rastgele bir olay
    if random.random() < olay_ihtimali:
        olay=random.choice(["Fırtına", "Hastalık Salgını", "Yeni Göçmenler", "Hazine Keşfi", "Doğum" , "Hiçbir Şey"])
        if olay=="Fırtına":
            random_event=random.randint(0,100)
            if random_event<60:
                ada_sağlığı=max(0, ada_sağlığı - 15)
                print("Şiddetli bir fırtına çıktı! Ada sağlığı 15 azaldı.1- Yaralıları tedavi et \n 2- Hasarı onar \n 3- Hiçbir şey yapma")
                seçim2=input("Seçiminiz (1/2/3): ")
                if seçim2=="1":
                    ada_sağlığı=max(0, min(100, ada_sağlığı + 20))
                    gıda=max(0, gıda - 10)
                    print("Yaralıları tedavi ettiniz. Ada sağlığı 5 arttı, gıda 10 azaldı.")
                elif seçim2=="2":
                    gıda=max(0, gıda - 10)
                    teknoloji=max(0, teknoloji + 4)
                    print("Hasarı onardınız. Gıda 10 azaldı, teknoloji 4 arttı.")
                else:
                    ada_sağlığı=max(0, ada_sağlığı - 2)
                    teknoloji=max(0, teknoloji - 2)
                    print("Hiçbir şey yapmadınız. Durum kötüleşiyor.")
            else:
                ada_sağlığı=max(0, ada_sağlığı - 5)
                print("Fırtına çıktı ama çok zarar vermedi. Ada sağlığı 5 azaldı.")
        elif olay=="Hastalık Salgını":
            random_event=random.randint(0,100)
            if random_event<30:
                nüfus=max(0, nüfus - 15)
                ada_sağlığı=max(0, ada_sağlığı - 10)
                gıda=max(0, gıda - 15)
                print("Ciddi bir hastalık salgını yayıldı! Nüfus 15, ada sağlığı 10 azaldı. Karantinada gıda 15 azaldı.")
            else:
                nüfus=max(0, nüfus - 5)
                print("Hafif bir hastalık yayıldı. Nüfus 5 azaldı.")
        elif olay=="Yeni Göçmenler":
            yeni_göçmen=random.randint(5,15)
            nüfus+=yeni_göçmen
            gıda=max(0, gıda - yeni_göçmen//2)
            print(f"Yeni göçmenler adaya geldi! Nüfus {yeni_göçmen} arttı, gıda {yeni_göçmen//2} azaldı.")
            random_event=random.randint(0,100)
            if random_event<50:
                teknoloji=max(0, teknoloji + 3)
                print("Göçmenler beraberinde yeni bilgiler getirdi! Teknoloji 3 arttı.")
            elif random_event<40:
                nüfus=max(0, nüfus - 10)
                print("Göçmenler ve ada halkı arasında anlaşmazlık çıktı! Nüfus 10 azaldı.")
        elif olay=="Hazine Keşfi":
            hazine=random.randint(20,50)
            gıda+=hazine
            print(f"Adada gizli bir hazine buldunuz! Gıda {hazine} arttı.")
            random_event=random.randint(0,100)
            if random_event<50:
                teknoloji=max(0, teknoloji + 5)
                print("Hazine içinde eski teknolojik aletler buldunuz! Teknoloji 5 arttı.")
            elif random_event<30:
                ada_sağlığı=max(0, ada_sağlığı - 10)
                print("Hazineyi koruyan tuzaklar vardı! Ada sağlığı 10 azaldı.")
            elif random_event<20:
                nüfus=max(0, nüfus - 10)
                print("Adalılar arasında hazine yüzünden kavga çıktı! Nüfus 10 azaldı.")
        elif olay=="Doğum":
            doğum_sayısı=random.randint(1,5)
            nüfus=max(0, nüfus + doğum_sayısı)
            print(f"Adada yeni doğumlar oldu! Nüfus {doğum_sayısı} arttı.")
        else:
            print("Adada sıradan bir gün devam ediyor.")
    print("Neredeyse akşam olmak üzere...")
    random_event=random.randint(0,100)
    if random_event<30:
        print("Adalılar bir mağara keşfettiler! 1- Mağarayı araştır \n 2- Hiçbir şey yapma")
        seçim3=input("Seçiminiz (1/2): ")
        if seçim3=="1":
            mağara_olayı=random.randint(0,100)
            if mağara_olayı<50:
                teknoloji=max(0, teknoloji + 7)
                gıda=max(0, gıda + 5)
                ada_sağlığı=max(0, ada_sağlığı - 10)
                print("Mağarada hazine buldunuz! Teknoloji 7 arttı, gıda 5 arttı, ada sağlığı 10 azaldı.")
            elif mağara_olayı<20:
                ada_sağlığı=max(0, ada_sağlığı - 15)
                nüfus=max(0, nüfus - 5)
                print("Mağarada çöküntü oldu! Ada sağlığı 15, nüfus 5 azaldı.")
            else:
                print("Mağarada pek bir şey bulamadınız.")
    elif random_event<50:
        print("Adalılar yeni bir tarım tekniği keşfettiler! Gıda üretimi artacak.")
        gıda=max(0, gıda + 20)
    elif random_event<60:
        print("Adalılar günün yorgunluğunu atmak için bir festival düzenlediler. Ada sağlığı 10 arttı.")
        ada_sağlığı=max(0, min(100, ada_sağlığı + 10))
    #Gün Sonu
    gıda = max(0, gıda - nüfus // 10)  # Her gün nüfusun %10'u kadar gıda tüketilir
    print(f"Adada {gün}. sona erdi. Bir durum değerlendirmesi yapalım.")
    if gıda==0:
        nüfus=max(0, nüfus - 10)
        ada_sağlığı=max(0, ada_sağlığı - 10)
        print(f"Gıda stokları tükendi! Açlıktan dolayı nüfus 10, ada sağlığı 10 azaldı.")
    if ada_sağlığı<50:
        nüfus=max(0, nüfus - 2)
        print(f"Ada sağlığı azalıyor! Nüfus 2 azaldı.")
    if ada_sağlığı<30:
        nüfus=max(0, nüfus - 5)
        print(f"Ada sağlığı kritik durumda! Nüfus 5 azaldı.")
    if ada_sağlığı<10:
        nüfus=max(0, nüfus - 10)
        print(f"Ada sağlığı çok kötü durumda! Nüfus 10 azaldı.")
    if teknoloji>10:
        ada_sağlığı=max(0, min(100, ada_sağlığı + 10))
        print(f"Yüksek teknoloji sayesinde ada sağlığı iyileşti! Ada sağlığı 10 arttı.")
    #GÜN SONU DEĞERLENDİRMESİ
    print(f"GÜN SONU DURUMU: Nüfus: {nüfus}, Gıda: {gıda}, Ada Sağlığı: {ada_sağlığı}, Teknoloji: {teknoloji}")
    nufus_gecmisi.append(nüfus)
    net_kazanc = gıda - gida_kaydi[-1] 
    günlük_kazanclar.append(net_kazanc)
    gida_kaydi.append(gıda)
#Oyun Sonu
print(f"\n Adada toplam {gün} gün geçirdiniz.")
if nüfus<=0:
    print("Tüm ada halkı hayatını kaybetti. Oyun bitti.")
elif ada_sağlığı<=0:
    print("Ada sağlığı tamamen tükendi. Ada yaşanmaz hale geldi. Oyun bitti.")
print(f"Maksimum ulaştığınız nüfus: {max(nufus_gecmisi)}")
print(f"Ortalama ulaşılan nüfus: {sum(nufus_gecmisi) / len(nufus_gecmisi):.2f}") 
if günlük_kazanclar:
    en_yuksek_kazanc = max(günlük_kazanclar)
    en_basarili_gun = günlük_kazanclar.index(en_yuksek_kazanc) + 1
    print(f"En Başarılı (Net Kazancın En Yüksek Olduğu) Gün: {en_basarili_gun}. gün (Kazanç: {en_yuksek_kazanc})")

    
    














