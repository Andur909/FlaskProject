from flask import Flask, render_template, request, redirect, url_for
import random
from math import sin, cos, tan

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', error="")
    else:
        if request.form.get('username') != "" and request.form.get('password') != "":
            return redirect(url_for('main'))
        else:
            return render_template("login.html", error="Login is required")

@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        button_press = request.form['index'];
        if button_press == "calculator":
            return redirect(url_for('calculator'))
        elif button_press == "rng":
            return redirect(url_for('random_number_generator'));
        elif button_press == "personal":
            return redirect(url_for('personal'));




@app.route('/personal', methods=['GET', 'POST'])
def personal():
    if request.method == 'GET':
        return render_template('PersonalInfo.html')
    else:
        button_press = request.form['btn']
        if button_press == "home":
            return redirect(url_for('main'))
        
        if button_press == 'SUBMIT':
            #<button name='btn' value='submit'>
            name = request.form.get('txtname')
            dob = request.form.get('txtdob')
            addr = request.form.get('txtaddress')
            bplace = request.form.get('txtbirthplace')
            favcol = request.form.get('txtcolor')
            #table with {{ values }}
            print("Sumbit went throught")
            return render_template('personal_output.html', name=name,dob=dob, addr=addr, bplace = bplace, favcol = favcol)

#By Akhtar
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template('calc.html', display='', prev_number='', prev_operation='', density='', finalprice='')
    else:
        display = request.form['display']
        button_pressed = request.form['calc']
        prev_number = request.form.get('prev_number', '')
        prev_operation = request.form.get('prev_operation', '')
        density = request.form.get('density', '')
        finalprice = request.form.get('finalprice', '')
        

        if button_pressed.isdigit():
            display += button_pressed
        elif button_pressed == 'period':
            if '.' not in display:
                display += '.'
        elif button_pressed == 'swap':
            if display:
                display = str(-1*float(display))
        elif button_pressed in ['+', '-', '*', '/']:
            if prev_number and prev_operation:
                try:
                    result = eval(prev_number + prev_operation + display)
                    display = str(result)
                except:
                    display = 'Error'
            prev_number = display
            prev_operation = button_pressed
            display = ''
        elif button_pressed in ['sin', 'cos', 'tan']:
            try:
                value = float(display)
                if button_pressed == 'sin':
                    result = sin(value)
                elif button_pressed == 'cos':
                    result = cos(value)
                elif button_pressed == 'tan':
                    result = tan(value)
                display = str(result)
            except:
                display = 'Error'
        elif button_pressed == 'clear':
            display = ''
            prev_number = ''
            prev_operation = ''
        elif button_pressed == '=':
            if prev_number and prev_operation:
                try:
                    result = eval(prev_number + prev_operation + display)
                    display = str(result)
                    prev_number = ''
                    prev_operation = ''
                except:
                    display = 'Error'
        elif button_pressed == 'subm_dens':
            mass = request.form.get('mass')
            volume = request.form.get('volume')
            try:
                density = "The density is: " + str(float(mass) / float(volume))
            except:
                density = 'Error calculating density'
        elif button_pressed == 'subm.int':
            principal = request.form.get('principal')
            rate = request.form.get('rate')
            timetype = request.form.get('timetype')
            time = request.form.get('time')
            try:
                interest = float(principal) * (1 + float(rate) / int(timetype)) ** (int(time) * int(timetype))
                finalprice = "The final amount from this interest is: " + str(interest)
            except:
                finalprice = 'Error calculating interest'
        elif button_pressed == "home":
            return redirect(url_for('main'))

        return render_template('calc.html', display=display, prev_number=prev_number, prev_operation=prev_operation, density=density, finalprice=finalprice)
    
@app.route('/random_number_generator', methods=['GET', 'POST'])
def random_number_generator():
    if request.method == 'GET':
        #Hide div that shows the number
        return render_template('rng.html')
    else:
        button_press = request.form['back']
        if button_press == "home":
            return redirect(url_for('main'))

        
        limitmin = request.form.get('txtnumlow')
        limitmax= request.form.get('txtnumhigh')
        limitmin = int(limitmin)
        limitmax = int(limitmax)
        if limitmin >= limitmax:
            return render_template('rng.html', high="Numbers Cannot Collide")
        rnum= random.randint(limitmin, limitmax)
        print(str(rnum))
        return render_template('rng.html', high="Your Random Number is " + str(rnum))
        
if __name__ == '__main__':
    app.run()
