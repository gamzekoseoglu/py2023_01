import os
class Search:
    def karsila(self):
        #folder_path = input("********URL Listeleme Alanı *****")

        klasorAdi = ('dokuman')

        pdf_dosyalari=[dosya for dosya in os.listdir(klasorAdi) if dosya.endswith('.pdf')]

        for pdf in pdf_dosyalari:
            print(pdf)
















