import chardet
# with open("fichier.text","a") as f:
#     f.write("un contenu")
#
# #
# with open("fichier_latin1.txt","r") as f:
#     content = f.read()
#
# print(content)
#
#
# with open("fichier_unicode.txt","r", encoding='utf-8') as f:
#     content = f.read()
#
# print(content)
#
#
# with open("fichier_unicode.txt","rb") as f:
#     print(chardet.detect(f.read()))
#     encoding = chardet.detect(f.read())['encoding'] #recuperation de l'encodage
#
# with open("fichier_unicode.txt","r", encoding=encoding) as f:
#     content = f.read() #utilisation de l'encoding recuperer par chardet



with open ("fichier_unicode.txt","rb") as f:
    encoding = chardet.detect(f.read())['encoding']
    f.seek(0)
    content = f.read().decode(encoding)
    print(content)


with open('fichier.text',"r+") as f: #ici on est en read+write
    print(f.tell()) #donne la position du curseur
    content = f.read()
    f.seek(0) #bouge le curseur a la postion voulue
    f.write(content[:4] + '-fred-' + content[4:])
    f.seek(0)
    print(f.read())


with open('fichier.text',"a") as f: #ici on est en append
    f.write("contenu")


with open("fichier.text",'a', newline='\n') as f:
    f.write("contenu")



from os.path import exists


if not exists('exist_as.txt'):
    print('creation du fichier')
    with open('existe_pas.txt','w') as f:
        f.write('contenu')
else:
    print('fichier deja existant')


#################################################################################################

#serialisation

import pickle

animaux = ['lion','elephant','tigre']

pickle.dump(animaux,open('animaux.txt','wb'))

animaux = pickle.load(open('animaux.txt','rb'))

print(animaux)



################################################################################################

animaux = ['chat', 'chien', 'pingouin']
fruits = ['pomme', 'poire', 'banane']
monuments = ['Tour Eiffel','Mont Saint-Michel','Machu Pichu']

# Déchargement
f = open("test.p", 'wb')
pickle.dump(animaux, f)
pickle.dump(fruits, f)
pickle.dump(monuments, f)

# Chargement
f = open('test.p', 'rb')
animaux = pickle.load(f)
fruits = pickle.load(f)
monuments = pickle.load(f)


#################################################################################

#json

import json

data = [
    {
        "pk":1,
        "label":"test",
    },{
        "pk":2,
        "label":"test2",

    }
]


serialized = json.dump(data)


print(serialized)
print(type(serialized))

deserialized = json.loads(serialized)

print(deserialized)
print(type(deserialized))



################################################################################