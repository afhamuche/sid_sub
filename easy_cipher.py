default_ch = '\ !?QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:{"}|+`~1qazxsw23edcvfr45tgbnhy67ujm,ki89ol./;p0-=[]\'\\'
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

    print(print_entry)
