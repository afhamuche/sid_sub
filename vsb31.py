#!/usr/bin/env python3

'''
Documentation, License etc.
@package vig_list

v_sub by Alessandro Hamuche
Version: 3.0
Date: 20 October 2021
Modified: 4 October 2022
'''
import math
import datetime
from os import system, name
from time import sleep

#print("\n- - - - T e s t - - - -")
print("\n- - - -S-t-a-r-t- - - -\n")

def clear():
    # Windows?
    if name == 'nt':
        _=system('cls')
    # Unix-based
    else:
        _=system('clear')

def list_print(alist):
    for i in range(len(alist)):
        print(alist[i])

def ientry():
    idatetime=datetime.datetime.now()
    idate=idatetime.strftime("%d/%b/%Y")
    itime=idatetime.strftime("%H:%M")
    ientry=idate + " " + itime
    return ientry

startstamp=datetime.datetime.now()

d_0=" (08@HPX`hpxÇêÉÿá¿░©└╚ðÏÓÞ≡°"
d_1="%-5=EMU]emu}àìòØÑ¡Á¢┼═ı¦ÕÝ§²"
d_2="!)19AIQYaiqyüëæÖí®▒╣┴╔Ð┘ßÚ±¨"
d_3="&.6>FNV^fnv~áÄû×ª«Â¥ã╬ÍÌµ¯÷■"
d_4="\"*2:BJRZbjrzéèÆÜó¬▓║┬╩Ê┌ÔÛ‗·"
d_5="'/7?GOW_gow"
d_6="#+3;CKS[cks{âïôøú½│╗├╦Ë█ÒÙ¾¹"
d_7="çÅùƒº»À┐Ã¤Î▀þ´¸"
d_8="$,4<DLT\\dlt|äîö£ñ¼┤╝─╠È▄õý¶³"


default_ch=d_0+d_1+d_2+d_3+d_4+d_5+d_6+d_7+d_8

# Translate
vig_list=[]
for i in range(len(default_ch)):
    vig_list.append(default_ch[i])

# Key
def vig_keyloop(key):
    vig_keylist=[]
    vig_key=key
    for i in range(len(vig_key)):
        vig_keylist.append(vig_key[i])
    return vig_keylist

vig_keylist=vig_keyloop("kindness")

# Initialize vars
wb=""
x=0
y=0
z0=0
z1=0
word=""
entry=[]

clear()

# File Open
fname="log.txt"
f=open(fname, "a")
print("log opened")

# Sub Loop
kindword="exit"

while word!=kindword:

    word=input("\n" + ientry() + " - ")

    if word==kindword:
        clear()
        list_print(entry)
        print("\n- Tomorrow is a good day!\n")
        break

    word_list=[]
    for i in range(len(word)):
        word_list.append(word[i])
        # Reverse Entry
        word_list.reverse()

    # Initialize Belt
    belt=[]
    belt_ch=""
    for i in range(len(word_list)):
        belt_ch=vig_keylist[0]
        belt.append(belt_ch)
        vig_keylist.pop(0)
        vig_keylist.append(belt_ch)

    vig_keylist=vig_keyloop(word)

    #Index and Replace
    word=""
    for i in range(len(word_list)):
        wb=word_list[i]
        x=vig_list.index(wb)
        wb=belt[i]
        y=vig_list.index(wb)

        z0=math.floor((x+y)/len(vig_list))
        z1=x+y-(len(vig_list)*z0)
        belt[i]=vig_list[z1]
        word+=belt[i]

    entry.append(ientry() + " - " + word)

    # File Write and Print
    f.write("\n" + ientry() + " - " + word + "\n")
    clear()
    list_print(entry)

# File Close
f.close()
print("log closed\n")

# Print Timestamps
endstamp=datetime.datetime.now()
starttime=startstamp.strftime("%H:%M")
endtime=endstamp.strftime("%H:%M")
print("entry info (-v)\n  stt: " + starttime + "\n  end: " + endtime)

print("\n- - - - -E-n-d- - - - -\n")
