from os import system, name
import datetime

def clear():
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')

def ientry():
    idatetime=datetime.datetime.now()
    idate=idatetime.strftime("%d/%b/%Y")
    itime=idatetime.strftime("%H:%M")
    ientry=idate + " " + itime
    return ientry

filename = 'log.txt'

#default_ch = '\ !?QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:{"}|+`~1qazxsw23edcvfr45tgbnhy67ujm,ki89ol./;p0-=[]\'\\'

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

one_time = input('Input one-time word: ')
exit_word = input('Input exit word: ')

while True:
    entry = input('Input entry: ')

    if exit_word == entry:
        break

    extended_ot = 1 + (len(entry)//len(one_time))
    extended_ot = extended_ot * one_time
    extended_ot = extended_ot[:len(entry)]

    print_entry = ''

    for i in range(len(entry)):
        x_index = default_ch.index(entry[i])
        y_index = default_ch.index(extended_ot[i])
        xy = x_index + y_index
        xy = xy % len(default_ch)
        print_entry += default_ch[xy]

    clear()
    print(f'Exit word is "{exit_word}"')
    with open(filename, 'a') as ifile:
        ifile.write(f'{ientry()} - {print_entry}\n')

    with open(filename, 'r') as ifile:
        lines = ifile.readlines()

    for line in lines[-5:]:
        print(line.strip())
