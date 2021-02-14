import string 
from random import randint
import time 
from math import ceil 
from math import floor
from math import sin
from math import cos
from math import sqrt

#I use french names, do= C; la=A
do = 32.70320 
re = 36.70810  
mi = 41.20344 
fa = 43.65353 
sol = 48.99943
la = 55.00000 
si = 61.73541
doSharp=34.6479
reSharp=38.8909
faSharp=46.2493
solSharp=51.9130
laSharp=58.2705 

PI = 3.141592

def abs(a):
    if a<0:
        return -a
    return a

def track_fusion(track1,track2):
    if len(track1)!=len(track2):
        print("Error")
        print("Track1")
        print(len(track1))
        print("Track2")
        print(len(track2))

    else:
        print("Ok")
        ret=[]
        for i in range(len(track1)):
            n1=track1[i]-127
            n2=track2[i]-127
            element=int((n1+n2)/2)+127
            ret.append(element)
        return ret
        
def note_do(length,octave):
    do_array=[]
    for i in range(length):
        note = int( sin(2*PI*do*pow(2,octave)*i/44100)*127*((length*3-i)/(length*3))+127)
        do_array.append(note)
    return do_array

def note_re(length,octave):
    re_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*re*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        re_array.append(note)
    return re_array

def note_mi(length,octave):
    mi_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*mi*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        mi_array.append(note)
    return mi_array

def note_fa(length,octave):
    fa_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*fa*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        fa_array.append(note)
    return fa_array

def note_sol(length,octave):
    sol_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*sol*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        sol_array.append(note)
    return sol_array

def note_la(length,octave):
    la_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*la*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        la_array.append(note)
    return la_array

def note_si(length,octave):
    si_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*si*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        si_array.append(note)
    return si_array

#44100 = 1 Sec; 44 = 1 ms
def chute(time):
    chute_array=[]
    for k in range(0,time):
        chute_array.append(127)
    return chute_array

def choose_note():
    r=randint(0,6)
    if r==0:
        return la
    elif r==1:
        return si
    elif r==2:
        return do
    elif r==3:
        return re
    elif r==4:
        return mi
    elif r==5:
        return fa
    else:
        return sol

#generate one note
def gen_note(length, freq,octave):
    note_array=[]
    for i in range(length):
        note = int( sin(i*2*PI*freq*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        #note = int( sin(i*2*PI*freq*pow(2,octave)/44100)*127*(1/sqrt(i+1))+127) #New way of attenuation, very primitive. . .
        note_array.append(note)
    print(length/44100)
    return note_array

#generate the whole music
def gen_notes_track(howmany):
    notes_track_array=[]
    #Hard coded test with sharps notes
    notes_track_array+=gen_note(int(214*44*2),reSharp,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),re,5)
    notes_track_array+=gen_note(int(214*44*2),reSharp,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),sol,5)
    notes_track_array+=gen_note(int(214*44),fa,5)
    notes_track_array+=gen_note(int(214*44),reSharp,5)
    notes_track_array+=gen_note(int(214*44),fa,5)
    notes_track_array+=gen_note(int(214*44*2),reSharp,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),re,5)
    notes_track_array+=gen_note(int(214*44*2),reSharp,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),sol,5)
    notes_track_array+=gen_note(int(214*44),fa,5)
    notes_track_array+=gen_note(int(214*44),reSharp,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)

    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44*2),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),do,5)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),laSharp,4)
    notes_track_array+=gen_note(int(214*44*4),do,5)
    notes_track_array+=chute(int(214*44*2))
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    
    #for i in range(howmany):
    #    notes_track_array+=gen_note(randint(440,44100),choose_note())
    return notes_track_array

def gen_note_trackGauche1():
    notes_track_array=[]
    notes_track_array+=chute(int(214*44*32))
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=gen_note(int(214*44*2),sol,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=gen_note(int(214*44*4),sol,4)
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=chute(int(214*44))
   
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),do,4)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*3),solSharp,4)
    notes_track_array+=gen_note(int(214*44),solSharp,4)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=gen_note(int(214*44),reSharp,4)
    notes_track_array+=gen_note(int(214*44*4),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,4)
    notes_track_array+=chute(int(214*44))
    return notes_track_array

def gen_note_trackGauche2():
    notes_track_array=[]
    notes_track_array+=chute(int(214*44*32))
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=gen_note(int(214*44*2),sol,3)
    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=gen_note(int(214*44*4),sol,3)
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=gen_note(int(214*44),sol,4)
    notes_track_array+=chute(int(214*44))

    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),do,3)
    notes_track_array+=gen_note(int(214*44),do,4)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*3),solSharp,3)
    notes_track_array+=gen_note(int(214*44),solSharp,3)
    notes_track_array+=chute(int(214*44))
    
    notes_track_array+=gen_note(int(214*44),sol,3)
    notes_track_array+=gen_note(int(214*44),reSharp,3)
    notes_track_array+=gen_note(int(214*44*4),do,3)
    notes_track_array+=gen_note(int(214*44*3),reSharp,3)
    notes_track_array+=chute(int(214*44))
    return notes_track_array

f = open('song.aqraw', 'wb')
maindroite=gen_notes_track(randint(30,120))
maingauche1=gen_note_trackGauche1()
maingauche2=gen_note_trackGauche2()
maingauche=track_fusion(maingauche1,maingauche2)
song=track_fusion(maingauche,maindroite)
note_array=bytearray(song)
f.write(note_array)

f.close()
print("Song generated!")
