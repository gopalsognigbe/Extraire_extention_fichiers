#Extraire les extentions (TUPPLES,LIST)

fichiers = ("notepad.exe","nom.fichier.perso.doc","note.tXt","vacance.jpeg","data.dat","planning")
definitions_extentions = (
    ("exe","Executable"),
    ("doc","Document word"),
    ("txt","Document text"),
    ("jpeg","Image JPEG")
)

#trouve les les extentions et stock le nom des fichiers dans un tableau               
def trouve(def_ext,fichiers):
    list_trouve=[]
    for i in fichiers :
        for e in range (len(def_ext)):
            for r in range (1):
                    if def_ext[e][r].lower() in i[-6:].lower().split("."):                    
                        print(f"{i} ({definitions_extentions[e][r+1]})")
                        list_trouve.append(i)
    return list_trouve                


a=trouve(definitions_extentions,fichiers)                
for i in fichiers:
     if i not in a :
            if "."  in i[-6:]:
              print(f"{i} (Aucune extention)")
            else:
                print(f"{i} (Extention non connue)")
    
          
         
            
