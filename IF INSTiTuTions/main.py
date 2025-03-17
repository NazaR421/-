from flask import Flask, redirect, url_for, session, request, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/s1')
def main_menu():
    return render_template('main_menu.html')



@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/cafe', )
def cafe():
    return render_template('cafe.html')

@app.route('/cofee')
def cofee():
    return render_template('cofee.html')

@app.route('/bar')
def bar():
    return render_template('bar.html')

@app.route('/main_menu2')
def main_menu2():
    return render_template('main_menu2.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')



if __name__ == '__main__':
    app.run(debug=True)