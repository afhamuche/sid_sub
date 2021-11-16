'''
sid_sub by Alessandro Hamuche
Version: 1.3-Beta
Date: 2 November 2021
Git: 16 November 2021
'''

import math
import datetime

print("\n- - - -S-t-a-r-t- - - -\n")

startstamp=datetime.datetime.now()

default_ch="AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz., /\\\"\'{}[]:;+=_-)0(9*8&7^6%5$4#3@2!1~`?<>"

# Translate
vig_list=[]
for i in range(len(default_ch)):
    vig_list.append(default_ch[i])

# Key
vig_keylist=[]
vig_key=input("passkey: ")
for i in range(len(vig_key)):
    vig_keylist.append(vig_key[i])

# Initialize vars
wb=""
x=0
y=0
z0=0
z1=0
word=""

# File Open
fname="logc.txt"
f=open(fname, "a")
print("log opened")

# Sub Loop
kindword=input("exit string: ")

while word!=kindword:

    idatetime=datetime.datetime.now()
    idate=idatetime.strftime("%d/%b/%Y")
    itime=idatetime.strftime("%H:%M")
    ientry=idate + " " + itime

    word=input("\n" + ientry + " - ")

    if word==kindword:
        print("\n- See you later!\n")
        break

    word_list=[]
    for i in range(len(word)):
        word_list.append(word[i])

    # Initialize Belt
    belt=[]
    belt_ch=""
    for i in range(len(word_list)):
        belt_ch=vig_keylist[0]
        belt.append(belt_ch)
        vig_keylist.pop(0)
        vig_keylist.append(belt_ch)

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

    # File Write and Print
    f.write("\n" + ientry + " - " + word + "\n")
    print("\n" + ientry + " - " + word)

# File Close
f.close()
print("log closed\n")

# Print Timestamps
endstamp=datetime.datetime.now()
starttime=startstamp.strftime("%H:%M")
endtime=endstamp.strftime("%H:%M")
print("Entry Info (-v)\n  start: " + starttime + "\n  stop: " + endtime)

print("\n- - - - -E-n-d- - - - -\n")
