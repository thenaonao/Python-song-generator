import string 
from random import randint
import time 
from math import ceil 
from math import floor
from math import sin
from math import cos
from math import sqrt

do = 32.70320 
re = 36.70810  
mi = 41.20344 
fa = 43.65353 
sol = 48.99943
la = 55.00000 
si = 61.73541 

PI = 3.141592

def abs(a):
    if a<0:
        return -a
    return a

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

#44100 = 1 Sec; 44.1 = 1 ms
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
def gen_note(length, freq):
    note_array=[]
    octave=randint(2,4)
    for i in range(0,length):
        note = int( sin(i*2*PI*freq*pow(2,octave)/44100)*127*((length*3-i)/(length*3))+127)
        #note = int( sin(i*2*PI*freq*pow(2,octave)/44100)*127*(1/sqrt(i+1))+127) #New way of attenuation, very primitive. . .
        note_array.append(note)
    print(length/44100)
    return note_array

#generate the whole music
def gen_notes_track(howmany):
    notes_track_array=[]
    #Hard coded "Au Clair de la Lune"
    notes_track_array+=note_do(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_do(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_do(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_re(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_mi(4800*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_re(4800*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_do(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_mi(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_re(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_re(2400*11,4)
    notes_track_array+=chute(20)
    notes_track_array+=note_do(7200*11,4)
    notes_track_array+=chute(20)
    
    
    #for i in range(howmany):
    #    notes_track_array+=gen_note(randint(440,44100),choose_note())
    return notes_track_array


f = open('song.aqraw', 'wb')
note_array=bytearray(gen_notes_track(randint(30,120)))
f.write(note_array)

f.close()
print("Song generated!")
