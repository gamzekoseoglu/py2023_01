from fileSearch import fileSearch
print("-: Mini Örümceğe hoş geldiniz! :-")
print("|------------------------------|")
print("")
useDataSearch = fileSearch()
while True:
    print("Menü: 0)Çıkış 1)URL Listele 2)URL Ekle 3)Örümcek Gönder 4)Sonuçları Listele")
    menuSecim = int(input("Tercihiniz: "))
    if menuSecim == 0:
        print("Mini Örümcek kapatılıyor...")
        break
    elif menuSecim == 1:
        useDataSearch.karsila()
        break
    elif menuSecim == 2:
        break
    elif menuSecim == 3:
        break
    elif menuSecim == 4:
        break