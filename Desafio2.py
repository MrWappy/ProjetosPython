import os
import re


dir = os.listdir("../")


for file in dir:
    if ".jpg" in file:
        novo_nome = re.sub(r'[0-9]+', '', file)
        os.rename("../" + file,"../" + novo_nome)
print("Os Ficheiros Foram Alterados!")
print(dir)