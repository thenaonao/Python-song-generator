import string #pour les notes
import random #pour les randoms
import time #pour le temps
from math import ceil #pour l'arrondi superieur
from math import floor #pour l'arrondi inferieur
debut = time.time() #debut temps
liste = []
#nbr = 1 #degre d'evolution
timing = 790000 #90000 est bien pour les tests
aigu = 40 #le plus aigu
grave = 200 #le plus grave
tempo = 60 #Plus le tempo est grand plus il y aura de rythme
flow = (aigu + grave)/2 * (aigu + grave)/tempo #calcul longueur note
loop = timing/flow #calcul notes avec le temps et la longueur note
d = flow/1.5 #decalage de la longeur
mini = flow - d #longueur minimum
maxi = flow + d #longueur maximum
fichier = open("Song.txt", "w")
def song(mini,maxi,l):
    #ajuste maximum avec grave
    b = (l/grave) * (maxi - mini)
    big = maxi - b
    return random.randint(mini,big)
s = string.letters
liste = s
dataevent = int(ceil(timing/100000)) #calcul pour frequence affichage pourcentage
for i in range(loop):
    r = random.choice(liste)
#    for u in range(nbr):
#        liste.append(r)
    b = random.randint(aigu,grave)
    for y in range(song(mini,maxi,b)):
        fichier.write(r)
        fichier.write(' ' * b)
    if(i%(loop/dataevent) == 0):
        print ''.join([repr((i*100)/loop),'%'])
fichier.close()
fin = time.time()
print fin - debut
