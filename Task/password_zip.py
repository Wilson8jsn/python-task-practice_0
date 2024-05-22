import zipfile

passw = "pass123"
zfile = zipfile.ZipFile("data.zip")

with open("diccionario.txt", 'r') as file:
  
    if passw in file.read().splitlines():
        try:  
                
            zfile.extractall(pwd=passw.encode("utf-8"))
            print("Todo bien todo correcto y yo que me alegro.")
        except Exception as error:
            print(error)
    else:
        print("No sirve vete a tu casa.")
