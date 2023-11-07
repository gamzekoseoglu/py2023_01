pip install PyPdf2
import os

import PyPDF2
pip install pdfminer.six

# PDF dosyalarını tarayacak fonksiyon
def scan_pdfs(folder_path):
    # Dizin içindeki PDF dosyalarını bulun
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

    # Her PDF dosyası için başlıkları dizinle
    for pdf_file in pdf_files:
        with open(os.path.join(folder_path, pdf_file), "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            for page_number in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_number)
                page_text = page.extractText()
                # Başlıkları belirlemek ve saklamak için uygun bir yöntem kullanın

# Kullanıcıyı yönlendiren menü fonksiyonu
def menu():
    while True:
        print("1. PDF Dosyalarını Tara")
        print("2. Dizini Görüntüle")
        print("3. Çıkış")
        choice = input("Bir seçenek seçin: ")
        if choice == "1":
            folder_path = input("PDF dosyalarını tarayacak dizini girin: ")
            scan_pdfs(folder_path)
        elif choice == "2":
            # Dizini görüntüleme işlemi
            pass
        elif choice == "3":
            break
        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    menu()
