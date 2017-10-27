import string #pour les notes
import random #pour les randoms
import time #pour le temps
debut = time.time() #debut temps
liste = []
#nbr = 1 #degre d'evolution
timing = 760000 #90000 21 sec pour telecharger
aigu = 80 #le plus aigu
grave = 200 #le plus grave
tempo = 74 #Plus le tempo est grand plus il y aura de rythme
flow = (aigu + grave)/2 * (aigu + grave)/tempo #calcul longueur note
loop = timing/flow #calcul notes avec le temps et la longueur note
d = flow/2 #decalage de la longeuur
mini = flow - d #longueur minimum
maxi = flow + d #longueur maximum
fichier = open("Song.txt", "w")
def Random_str(cnt):
    return random.choice(cnt)
def RndIn(a,b):
    return random.randint(a,b)
def song(mini,maxi,l):
    #ajuste maximum avec grave
    b = (l/grave) * (maxi - mini)
    big = maxi - b
    return random.randint(mini,big)
#s = string.letters[0:52]
s = string.letters
#s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#s = '06agATZ'
for k in s:
    liste.append(k)
for i in range(loop):
    r = Random_str(liste)
#    for u in range(nbr):
#        liste.append(r)
    b = RndIn(aigu,grave)
    for y in range(song(mini,maxi,b)):
        fichier.write(r)
        for t in range(b):
            fichier.write(' ')
    if(i%(loop/(loop/100)) == 0):
        print ''.join([repr((i*100)/loop),'%'])
fichier.close()
fin = time.time()
print fin - debut
