from difflib import SequenceMatcher

with open(r"C:\Users\user.DESKTOP-19R781R\Desktop\4014 CODE\Difflib\1.txt", encoding="UTF-8") as file1, open(r"C:\Users\user.DESKTOP-19R781R\Desktop\4014 CODE\Difflib\t2.txt", encoding="utf-8") as file2:
    fil1data=file1.read()
    file2data=file2.read()
    similarity=SequenceMatcher(None,fil1data,file2data).ratio()
    print(similarity*100)


