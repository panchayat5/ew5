# from sre_constants import SUCCESS
from http.client import _HTTPConnectionProtocol
from flask import Flask, render_template, request, redirect
from matplotlib import testing
from pip import main
from sqlalchemy import false, true
from flask_mail import Mail, Message
from second import second
# from second1 import second1
from config import mail_username, mail_password
from sqlalchemy import true
from flask_sqlalchemy import SQLAlchemy
import pickle
import sqlite3
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
# import warnings
# warnings.filterwarnings("ignore")

currentlocation = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

sales = pd.read_csv('static/csv/supermarket_sales.csv')
Mum = pd.read_csv('static/csv/Mumbai Sales_Analysis.csv')
Del = pd.read_csv('static/csv/Delhi Sales_Analysis.csv')
Bang = pd.read_csv('static/csv/Bangalore Sales_Analysis.csv') 

app.register_blueprint(second,url_prefix="")
# app.register_blueprint(second1,url_prefix="")

# testing kya hotti h white box and black box testing

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/akshit/Desktop/Final/login.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSl'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)

@app.route("/", methods = ['GET'])
@app.route("/index", methods = ['GET'])
def HomePage():
    return render_template('index.html')   


@app.route("/contactForm", methods = ['GET' , 'POST'])
def contactForm():
    if request.method == "POST":
        name = request.form.get('Name')
        email = request.form.get('Email')
        phone = request.form.get('Phone')
        message = request.form.get('Message')

        msg = Message(subject=f"Mail from{name}", body=f"Name: {name}\nE-Mail: {email}\nPhone: {phone}\n\n\n{message}", sender=mail_username, recipients=['oppanchayat5@gmail.com'])
        mail.send(msg)
        return render_template("contactForm.html", success=True)

    return render_template('contactForm.html')


@app.route("/services")
def services():
    return render_template('services.html')   


@app.route("/aboutus")
def aboutUs():
    return render_template('aboutUs.html')    


@app.route("/login", methods=['POST', 'GET'])
def login():
    return render_template('login.html')   
database = {'akshit':'123654','vedant':'654789','shweta':'789654'}

@app.route('/dashboard', methods=['POST', 'GET'] )
def dashboard():
    if request.method == "POST" :
        name1 = request.form['username1']
        pwd = request.form['password1']

        if name1 not in database:
            return render_template('login.html', info ='Invalid User')
        else:
            if database[name1]!=pwd:
                return render_template('login.html', info = "Invalid Password")
            else:
                return render_template('dashboard.html', Q1 ='static/graph_Img/Total_Sales/Month.png', T2 = 'static/graph_Img/Total_Sales/City.png', Q3 = 'static/graph_Img/Total_Sales/Time.png', 
                Q4 = 'static/graph_Img/Total_Sales/Product.png' ,Q5 = 'static/graph_Img/Total_Sales/Customer.png',Q6 = 'static/graph_Img/Total_Sales/Payment.png' , ProductLine = bpl, BestMonth = bms, BestCity = bcs, Member = mvn, Payment = ppm, SalesByH = sbh_s)
    
    return render_template('dashboard.html',Q1 ='static/graph_Img/Total_Sales/Month.png', T2 = 'static/graph_Img/Total_Sales/City.png', Q3 = 'static/graph_Img/Total_Sales/Time.png', 
    Q4 = 'static/graph_Img/Total_Sales/Product.png' ,Q5 = 'static/graph_Img/Total_Sales/Customer.png',Q6 = 'static/graph_Img/Total_Sales/Payment.png' , ProductLine = bpl, BestMonth = bms, BestCity = bcs, Member = mvn, Payment = ppm, SalesByH = sbh_s)

    #     sqlconnection = sqlite3.Connection(currentlocation + "\login.db")        
        
    #     cursor = sqlconnection.cursor()
    #     query1 = "SELECT username, password from User WHERE username = '{un}' AND password = '{pw}'".format(un = name1, pw = pwd)

    #     rows = cursor.execute(query1)
    #     rows = rows.fetchall()

    # if len(rows) == 1:
    #     return render_template('dashboard.html', Q1 ='static/graph_Img/Total_Sales/Month.png', T2 = 'static/graph_Img/Total_Sales/City.png', Q3 = 'static/graph_Img/Total_Sales/Time.png', 
    #         Q4 = 'static/graph_Img/Total_Sales/Product.png' ,Q5 = 'static/graph_Img/Total_Sales/Customer.png',Q6 = 'static/graph_Img/Total_Sales/Payment.png' , ProductLine = bpl, BestMonth = bms, BestCity = bcs, Member = mvn, Payment = ppm, SalesByH = sbh_s) 
    # else:
    #     error = "invalid password"  
    #     return redirect("/login")


##################################### QUERY 1 #################################
 

Total_Sales = sales.groupby('Month').Total.sum()
months = range(1,4)
        
plt.figure(figsize=(10,7))
colors = ['#e01616', '#612f75', '#db3d7a']
        
plt.bar(months, Total_Sales, color = colors)
        
plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
labels = ['Jaunuary', 'February', 'March']
plt.xticks(months, size = 14, labels = labels)
plt.yticks(size=14)
        
plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
plt.savefig('static/graph_Img/Total_Sales/Month.png')


##################################### QUERY 2 #################################

# Delhi = sales.loc[sales['City'] == 'DELHI'].count()[0]
# Mumbai = sales.loc[sales['City'] == 'MUMBAI'].count()[0]
# Bangalore = sales.loc[sales['City'] == 'BANGALORE'].count()[0]

# Mumbai = sales.loc[sales['City'] == 'MUMBAI'].Total.sum().astype(int)
# Delhi = sales.loc[sales['City'] == 'DELHI'].Total.sum().astype(int)
# Bangalore = sales.loc[sales['City'] == 'BANGALORE'].Total.sum().astype(int)

# labels = ['Mumbai', 'Delhi', 'Bangalore']
# colors = ['#4755a6', '#6da32f']
# explode = (0.1,0.1,0.1)

# plt.pie([Delhi,Mumbai,Bangalore], labels = labels, explode = explode, autopct = '%.2f %%', radius=1.5,textprops={'fontsize': 15} )

# plt.savefig('static/graph_Img/Total_Sales/City.png')


##################################### QUERY 3 #################################



sales['Hour'] = pd.to_datetime(sales['TIME']).dt.hour
sales['Minute'] = pd.to_datetime(sales['TIME']).dt.minute
sales['Count'] = 1

keys = [pair for pair, df in sales.groupby(['Hour'])]

plt.figure(figsize=(9,6))

plt.title('Sales By Hour', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.plot(keys, sales.groupby(['Hour']).count()['Count'], color='#32b865')

plt.xticks(keys,size = 13)
plt.yticks(size = 13)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 20 })
plt.xlabel('Time in Hours', fontdict= {'fontname': 'Georgia','fontsize': 20 })

plt.grid()
plt.savefig('static/graph_Img/Total_Sales/Time.png')



##################################### QUERY 4 #################################



Total_Sales = sales.groupby('Product line').Total.sum()

Product = sales.groupby('Product line')
keys = [pair for pair, df in Product]

plt.figure(figsize=(18,15))

plt.title('Sales Of Product', fontdict= {'fontname': 'Georgia','fontsize': 20 })
colors = ['#4755a6', '#6da32f', '#ad283e', '#d6d01e', '#913d5b', '#5b7fe3']

plt.bar(keys, Total_Sales, color = colors)

plt.xticks(keys, size=13)
plt.yticks(size = 14)

plt.ylabel('Sales', fontdict= {'fontname': 'Georgia','fontsize': 30 })
plt.xlabel('Product Line', fontdict= {'fontname': 'Georgia','fontsize': 30 })

#     # quantity_ordered = Product.sum()['Quantity']

#     # fig, ax1 = plt.subplots()

#     # ax2 = ax1.twinx()

#     # ax1.bar(keys, Total_Sales, color='g')
#     # ax2.plot(keys, quantity_ordered, color='b')

#     # # plt.figure(figsize=(8,4))

#     # ax1.set_xlabel('Product Line', size=20)
#     # ax1.set_ylabel('Sales', color='g', size=20)
#     # ax2.set_ylabel('Quantity', color='b',size=20)
#     # ax1.set_xticklabels(keys, rotation='vertical', size=15)
#     # plt.yticks(size = 13)

plt.savefig('static/graph_Img/Total_Sales/Product.png')



##################################### QUERY 5 #################################



# normal = sales.loc[sales['Customer type'] == 'Normal'].count()[0]
# member = sales.loc[sales['Customer type'] == 'Member'].count()[0]

# labels = ['Normal', 'Member']
# colors = ['#6097a8', '#ab8c26']
# explode = (0.13,0.13)

# plt.pie([normal,member],labels = labels, colors = colors, explode = explode, autopct = '%.2f %%', radius=1.2 ,textprops={'fontsize': 16})

# plt.savefig('static/graph_Img/Total_Sales/Customer.png')



##################################### QUERY 6 #################################



# Credit_card = sales.loc[sales['Payment'] == 'Credit card'].count()[0]
# Cash = sales.loc[sales['Payment'] == 'Cash'].count()[0]
# Ewallet = sales.loc[sales['Payment'] == 'Ewallet'].count()[0]

# labels = ['Credit card', 'Cash', 'Ewallet']
# colors = ['#4755a6', '#6da32f','#c24127']
# explode = (0.1,0.1,0.1)

# plt.pie([Credit_card, Cash, Ewallet], labels = labels,explode = explode, colors = colors, autopct = '%.2f %%', radius=1.3,textprops={'fontsize': 14})

# plt.savefig('static/graph_Img/Total_Sales/Payment.png')

mm=dict()
# best product line--------------------------------------
ea=Bang[Bang['Product line']=='Electronics accessories']['Quantity'].sum()
fa=Bang[Bang['Product line']=='Fashion ccessories']['Quantity'].sum()
fb=Bang[Bang['Product line']=='Food and beverages']['Quantity'].sum()
hb=Bang[Bang['Product line']=='Health and beauty']['Quantity'].sum()
hl=Bang[Bang['Product line']=='Home and lifestyle']['Quantity'].sum()
sp=Bang[Bang['Product line']=='Sports and travel']['Quantity'].sum()
pl={'electronics accessories':ea,'Fashion accessories':fa,'food and beverages':fb,'health and beauty':hb,'home and lifestyle':hl,'sports and travel':sp}
bpl=max(pl,key=pl.get)
# print(f"{bpl}")


#best month----------------------------------
jan=sales[sales['Month']=='January']['Total'].sum()
feb=sales[sales['Month']=='February']['Total'].sum()
mar=sales[sales['Month']=='March']['Total'].sum()
monthlysalesdict={'January':jan,'february':feb,'march':mar}
bms=max(monthlysalesdict,key=monthlysalesdict.get)
# print(f"{bms}")  

#best city---------------------------------------------
mum=sales[sales['City']=='MUMBAI']['Total'].sum()
delh=sales[sales['City']=='DELHI']['Total'].sum()
blr=sales[sales['City']=='BANGALORE']['Total'].sum()
citysalesdict={'MUMBAI':mum,'DELHI':delh,'BANGALORE':blr}
bcs=max(citysalesdict,key=citysalesdict.get)
# print(f'{bcs}')

#membersVnormal---------------------------------------
mem=sales[sales['Customer type']=='Member']['Total'].sum()
non=sales[sales['Customer type']=='Normal']['Total'].sum()
memvsnordict={'Member':mem,'Normal':non}
mvn=max(memvsnordict,key=memvsnordict.get)
# print(f'MOST CUSTOMER WERE:{mvn}')

#preferablepaymentmode--------------------------------
cc=sales[sales['Payment']=='Credit Card']['Total'].sum()
cash=sales[sales['Payment']=='Cash']['Total'].sum()
ew=sales[sales['Payment']=='Ewallet']['Total'].sum()
paymentmodedict={'credit card':cc,'cash':cash,'Ewallet':ew}
ppm=max(paymentmodedict,key=paymentmodedict.get)
# print(f'most preferred payment mode:{ppm}')

#salesbyhour----------------------------------------
sales['Hour']=pd.to_datetime(sales['TIME']).dt.hour
sales['Minute']=pd.to_datetime(sales['TIME']).dt.minute
sales['Count']=1
ten=sales[sales['Hour']==10]['Total'].sum()
elv=sales[sales['Hour']==11]['Total'].sum()
twl=sales[sales['Hour']==12]['Total'].sum()
thr=sales[sales['Hour']==13]['Total'].sum()
frt=sales[sales['Hour']==14]['Total'].sum()
fif=sales[sales['Hour']==15]['Total'].sum()
six=sales[sales['Hour']==16]['Total'].sum()
svn=sales[sales['Hour']==17]['Total'].sum()
eig=sales[sales['Hour']==18]['Total'].sum()
nin=sales[sales['Hour']==19]['Total'].sum()
twn=sales[sales['Hour']==20]['Total'].sum()
salesbyhourdict={'10am':ten,'11am':elv,'12pm':twl,'1pm':thr,'2pm':frt,'3pm':fif,'4pm':six,'5pm':svn,'6pm':eig,'7pm':nin,'8pm':twn}
sbh_s=max(salesbyhourdict,key=salesbyhourdict.get)
# print(f'best time for sales:{sbh}')


@app.route("/settings")
def settings():
    return render_template('settings.html')


# @app.route('/test_aki')
# def chartTest():  
#     return render_template('akshit.html', name = 'new_plot', url ='static/images/Month.png')

# Total_Sales = sales.groupby('Month').Total.sum()
# months = range(1,4)
        
# plt.figure(figsize=(10,7))
# colors = ['#e01616', '#612f75', '#db3d7a']
        
# plt.bar(months, Total_Sales, color = colors)
        
# plt.title('Sales By Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
# labels = ['Jaunuary', 'February', 'March']
# plt.xticks(months, size = 14, labels = labels)
# plt.yticks(size=14)
        
# plt.ylabel('Sales of each Month', fontdict= {'fontname': 'Georgia','fontsize': 20 })
# plt.xlabel('Months', fontdict= {'fontname': 'Georgia','fontsize': 20 })
        
# plt.savefig('static/images/Month.png')  

if __name__ == '__main__':
    app.run(debug=true,port = 112)
