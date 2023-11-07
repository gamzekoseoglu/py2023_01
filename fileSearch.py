class fileSearch:
       def karsila(self):
           folder_path = input("********URL Listeleme Alanı *****")
           dataOpen = open(self.dataFile, 'r')
           for dataShow in dataOpen:
               print(dataShow)
           dataOpen.close()


