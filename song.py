import string #pour les notes
import random #pour les randoms
import time #pour le temps
from math import ceil #pour l'arrondi superieur
from math import floor #pour l'arrondi inferieur
debut = time.time() #debut temps
liste = []
#nbr = 1 #degre d'evolution
timing = 90000 #90000 est bien pour les tests
aigu = 50 #le plus aigu
grave = 400 #le plus grave
tempo = 92 #Plus le tempo est grand plus il y aura de rythme 82 max
flow = int(ceil((aigu + grave)/2 * (aigu + grave)/tempo)) #calcul longueur note
loop = int(ceil(timing/flow)) #calcul notes avec le temps et la longueur note
d = flow/1.5 #decalage de la longeur
mini = flow - d #longueur minimum
maxi = flow + (d*6) #longueur maximum
change = 75 #pourcentage de changement
percent_sensibility = 1.5 #1.5 est bien
fichier = open("Song.txt", "w")
def song(mini,maxi,l):
    #ajuste maximum avec grave
    b = (l/grave) * (maxi - mini)
    big = maxi - b
    mini = int(mini)
    big = int(big)
    return random.randint(mini,big)
def modify(a,d):
    z = (a*0.9)/d * (change/100)
    mini_v = (aigu - b)
    mini_v = int(floor(mini_v * z))
    maxi_v = grave - b
    maxi_v = floor(maxi_v * z)
    v = random.randint(mini_v,maxi_v)
    p = v/a
    return p
s = string.letters
liste = s
time_percent = 100000 * percent_sensibility
dataevent = int(ceil(timing/time_percent)) #calcul pour frequence affichage pourcentage
for i in range(loop):
    r = random.choice(liste)
#    for u in range(nbr):
#        liste.append(r)
    b = random.randint(aigu,grave)
    len_song = song(mini,maxi,b)
    v = 0
    p = 0
    if(random.randint(0,100) > 50):
        p = modify(len_song,maxi)
    for y in range(len_song):
        b = b + p
        fichier.write(r)
        fichier.write(' ' * b)
    if(i%(loop/dataevent) == 0):
        print ''.join([repr((i*100)/loop),'%'])
fichier.close()
fin = time.time()
print fin - debut
