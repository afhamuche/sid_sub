from flask import Flask, render_template, request

app = Flask(__name__)


def encrypt_entry(one_time, entry):
    default_ch = ' !?QAZ@.SX#Fdcvfr4/;p0-=[]\'\\W5tgbnJM*IK<(Ow23ehL>)P~1qaEDC$Rzxsy67ujV%TGB^YH:{"}|+`N&Um,ki89ol'
    extended_ot = 1 + (len(entry) // len(one_time))
    extended_ot = extended_ot * one_time
    extended_ot = extended_ot[:len(entry)]

    print_entry = ''

    for i in range(len(entry)):
        x_index = default_ch.index(entry[i])
        y_index = default_ch.index(extended_ot[i])
        xy = x_index + y_index
        xy = xy % len(default_ch)
        print_entry += default_ch[xy]

    return print_entry


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        one_time = request.form['one_time']
        entry = request.form['entry']
        result = encrypt_entry(one_time, entry)

        return render_template('index.html', result=result)
    else:
        return render_template('index.html', result=None)


if __name__ == '__main__':
    app.run(debug=True)
