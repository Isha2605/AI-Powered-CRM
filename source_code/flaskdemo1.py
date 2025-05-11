from flask import Flask, render_template,flash, redirect,url_for,session,logging,request, session,g,Response
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pymysql
import matplotlib.pyplot as plt
plt.switch_backend('agg')
from matplotlib.pyplot import xticks
import seaborn as sns
pymysql.install_as_MySQLdb()
from implement1 import coffee
import pandas as pd
import numpy as np
import joblib
response=Response()
import json
from decimal import Decimal
from flask_mail import Mail,Message
from datetime import date,timedelta



app = Flask(__name__)




db = SQLAlchemy(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='hrcrm0110@gmail.com'
app.config['MAIL_PASSWORD']='LOL@101010'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/be_project'
#app.config['SECRET_KEY'] = 'the random string'


svm_from_joblib = joblib.load('lol2.pkl')

# Use the loaded model to make predictions


# db = SQLAlchemy(app)



class Employees(db.Model):
    EmpID = db.Column(db.Integer, primary_key=True)
    Employee_Name = db.Column(db.String(100), unique=False, nullable=False)
    DeptID = db.Column(db.Integer, unique=False, nullable=False)
    PerfScoreID = db.Column(db.Integer, unique=False, nullable=True)
    Salary = db.Column(db.Integer, unique=False, nullable=False)
    PositionID = db.Column(db.Integer, unique=False, nullable=False)
    DOB = db.Column(db.String(8), unique=False, nullable=False)
    Sex = db.Column(db.String(8), unique=False, nullable=True)
    ManagerID = db.Column(db.Integer, unique=False, nullable=False)
    #PerformanceScore = db.Column(db.Integer,unique=False nullable=False)
    EmpSatisfaction = db.Column(db.Integer, unique=False, nullable=False)
    SpecialProjectsCount = db.Column(db.Integer, unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(60), unique=True, nullable= True)
    number_of_medals = db.Column(db.Integer, unique=False, nullable=True)


    def __repr__(self):
        return f"User('{self.email}')"

class Sales(db.Model):
    Region = db.Column(db.String(50), unique=False, nullable=False )
    Country = db.Column(db.String(50), unique=False, nullable=False)
    Sales_Channel = db.Column(db.String(40), unique=False, nullable=False)
    Order_Priority = db.Column(db.String(2), unique=False, nullable=False)
    Order_Date = db.Column(db.String(20), unique=False, nullable=False)
    Order_ID = db.Column(db.Integer, primary_key=True)
    Ship_Date = db.Column(db.String(20), unique=False, nullable=False)
    Units_Sold = db.Column(db.Integer,unique=False, nullable=False)
    Unit_Price = db.Column(db.Integer, unique=False, nullable=False)
    Unit_Cost = db.Column(db.Integer, unique=False, nullable=True)
    Total_Revenue = db.Column(db.Integer, unique=False, nullable=True)
    Total_Cost = db.Column(db.Integer, unique=False, nullable= True)
    Total_Profit = db.Column(db.Integer, unique=False, nullable=True)
    Employee = db.Column(db.Integer, unique=True, nullable=True)
    Order_Month = db.Column(db.Integer, unique=False, nullable=True)
    Order_Day = db.Column(db.Integer, unique=False, nullable=True)
    Order_Year = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return f"User('{self.Order_ID}')"

class Leads(db.Model):
    Prospect_ID = db.Column(db.String, primary_key=True)
    Lead_Number = db.Column(db.Integer, unique=False, nullable=True)
    Lead_Origin = db.Column(db.String, unique=False, nullable=True)
    Lead_Source = db.Column(db.Integer, unique=False, nullable=True)
    Converted = db.Column(db.Integer, unique=False, nullable=True)
    TotalVisits = db.Column(db.Integer, unique=False, nullable=True)
    Total_Time_Spent_on_Website = db.Column(db.Integer, unique=False, nullable=True)
    Page_Views_Per_Visit = db.Column(db.String, unique=False, nullable=True)
    Last_Activity = db.Column(db.String, unique=False, nullable=True)
    Country = db.Column(db.String, unique=False, nullable=True)
    Specialization = db.Column(db.String, unique=False, nullable=True)
    How_did_you_hear_about_X_Education = db.Column(db.String, unique=False, nullable=True)
    What_is_your_current_occupation = db.Column(db.String, unique=False, nullable=True)
    What_matters_most_to_you_in_choosing_a_course	 = db.Column(db.String, unique=False, nullable=True)
    Search = db.Column(db.String, unique=False, nullable=True)
    Magazine = db.Column(db.String, unique=False, nullable=True)
    Newspaper_Article = db.Column(db.String, unique=False, nullable=True)
    X_Education_Forums = db.Column(db.String, unique=False, nullable=True)
    Newspaper = db.Column(db.String, unique=False, nullable=True)
    Digital_Advertisement = db.Column(db.String, unique=False, nullable=True)
    Through_Recommendations = db.Column(db.String, unique=False, nullable=True)
    Receive_More_Updates_About_Our_Courses = db.Column(db.String, unique=False, nullable=True)
    Tags = db.Column(db.String, unique=False, nullable=True)
    Lead_Quality = db.Column(db.String, unique=False, nullable=True)
    Update_me_on_Supply_Chain_Content = db.Column(db.String, unique=False, nullable=True)
    Get_updates_on_DM_Content = db.Column(db.String, unique=False, nullable=True)
    Lead_Profile = db.Column(db.String, unique=False, nullable=True)
    City = db.Column(db.String, unique=False, nullable=True)
    I_agree_to_pay_the_amount_through_cheque = db.Column(db.String, unique=False, nullable=True)
    A_free_copy_of_Mastering_The_Interview = db.Column(db.String, unique=False, nullable=True)
    Last_Notable_Activity = db.Column(db.String, unique=False, nullable=True)

    def __repr__(self):
        return f"User('{self.Prospect_ID}')"

class Bookmarks(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), unique=False, nullable=False)
    Number_of_medals = db.Column(db.Integer, unique=False, nullable=False)
    def __repr__(self):
        return f"User('{self.ID}')"

@app.route('/')


@app.route("/register", methods=["GET", "POST"])
def register():
    #print(g.user)
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        data = Employees.query.filter_by(email=email).first()
        print(data)
        if data is not None:
            return render_template('register.html', message="Already registered")
        reg = Employees(email=email, password=password)
        db.session.add(reg)
        db.session.commit()
    return render_template("register.html")



@app.route("/adminlogin", methods=["GET", "POST"])
def adminlogin():
    #print(g.user)
    if request.method == 'GET':
        return render_template('login_admin.html')
    else:
        email = request.form['email']
        password = request.form['password']
        data = Employees.query.filter_by(email=email, password=password).first()
        #print(data, password, email)
        session['logger']=data.EmpID

        if data is not None:

            # print("LOL#")
            k=data.__dict__
            del k['_sa_instance_state']
            session['user'] =k
            session['id']=k['email'].split('@')[0]
            # print(session['id'])

            # print(type(session['user']), type(data.DeptID))
            session['logged_in'] = True
            #g.user=email
            if int(data.DeptID)==5:
                # print('admin')
                return render_template('index_admin.html',user=session['id'])
            else:
                # print('user')
                return render_template('index_user.html',user=session['id'])
        return render_template('login_admin.html', message="Incorrect Details")




@app.before_request
def before_request():
    g.user=None
    if 'user' in session:
        g.user=session['user']

@app.route('/dropsession', methods=["GET", "POST"])
def dropsession():
    session.pop('user', None)
    return redirect(url_for('adminlogin'))



@app.route('/adminhomepage', methods=["GET", "POST"])
def adminhomepage():
    if session.get('user') is None:
        print("HAHAHAGA")
        return redirect(url_for('register'))
    print(session['preds'],"LOLOLOL")
    return render_template("index_admin.html",user=session['id'])

@app.route('/userhomepage', methods=["GET", "POST"])
def userhomepage():
    if session.get('user') is None:
        print("HAHAHAGA")
        return redirect(url_for('register'))
    return render_template('index_user.html',user=session['id'])


@app.route('/contact_form', methods=["GET", "POST"])
def contact_form():
    if session.get('user') is None:
        print("HAHAHAGA")
        return redirect(url_for('register'))
    if (request.method == 'POST'):
        users=Employees.query.all()
        #email = request.form.get('email')
        message = request.form.get('message')
        # print(message,"LOL2")
        for user in users:
            if len(user.email)>0:
                # print(user.email,"LOLI")
                msg= Message(subject='Hello',sender='hrcrm0110@gmail.com',recipients=[user.email])
                # print(msg, "LOL1")
                msg.body=message
                mail.send(msg)
        success="Message sent!"
        #k=url_for("userhomepage")
        return render_template('contact_form.html', success=success,user=session['id'])
    else:
        return render_template("contact_form.html",user=session['id'])




@app.route('/get_msg', methods=["GET", "POST"])
def get_msg():
    usertext = request.args.get('msglol')
    # print(usertext)
    return str(coffee.bot(usertext))
@app.route('/open_chat', methods=["GET", "POST"])
def open_chat():
    if session.get('user') is None:
        print("HAHAHAGA")
        return redirect(url_for('register'))
    return render_template("chatbot.html",user=session['id'])


@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    if session.get('user') is None:
        #print("HAHAHAGA")
        return redirect(url_for('register'))
    #print(g.user)
    if request.method == "POST":
        # headings=["NO Bookmarks"]
        # print(session['preds'],session['user'],"!!!!!")
        users = Employees.query.all()
        #print(users)
        # for user in users:
        #     #print(user.Salary)
        li=["The Employee doesn't exist"]
        empid = int(request.form.get('emp_id'))


        #print(empid,type(empid))
        for k in users:
            if k.EmpID==empid:
                #print("LOLA")
                user = k
                #print(user,session['preds'])
                li=svm_from_joblib.predict([[user.EmpSatisfaction,user.Salary,user.SpecialProjectsCount,user.ManagerID]])
                if user.EmpID not in [i[0] for i in session['preds']]:
                    session['preds'].append([user.EmpID,user.Employee_Name,user.number_of_medals,int(li[0])])

                break
        enable=False
        str1="Added"
        reg=0
        headings=['EmpID','EmpName','Number of Medals','Predicted Performance Score']
        if Bookmarks.query.filter_by(ID=user.EmpID).first() is None:
            str1="Bookmark"
            enable=True
            reg=user.EmpID
            print(reg)

        # print(session['preds'],"Session preds")
        print(session['id'])
        return render_template('welcome.html', message=li,user=session['id'],headings=headings,data=session['preds'],Butname=str1,value1=reg, enable=enable)

    return render_template('welcome.html',user=session['id'])







@app.route('/sales', methods=["GET", "POST"])
def sales():
    if session.get('user') is None:
        #print("HAHAHAGA")
        return redirect(url_for('register'))
    #print("LOLSALE")
    if request.method == "GET":
        #print("CHUP")
        sale = Sales.query.all()
        col1=sale[0].__dict__
        del col1["_sa_instance_state"]
        cols=col1.keys()
        # print(cols)
        arr=[]
        #print(session['logger'])
        for k in sale:
            #print(k.Employee)
            #k.Employee,logger)
            if k.Employee==session['logger']:
                # print("BHAG CHOMU")
                z=k.__dict__
                del z["_sa_instance_state"]
                # print(z.keys())
                # print(z)
                # print(z.values())

                arr.append(z.values())
        return render_template('sales.html',headings=cols,data=arr,user=session['id'])

@app.route('/add_sales', methods=["GET", "POST"])
def add_sales():
    if request.method == "POST":
        Order_Priority = request.form.get('op')
        Region = request.form.get('region')
        Item_Type = request.form.get('it')
        Units_Sold = request.form.get('unitsold')
        Unit_Cost = request.form.get('unitcost')
        Total_Cost = request.form.get('totalcost')
        Total_Profit = request.form.get('totalprofit')
        Sales_Channel = request.form.get('saleschannel')
        Country = request.form.get('country')
        Unit_Price = request.form.get('unitprice')
        Total_Revenue = request.form.get('totalrevenue')
        Employee=session['user']['EmpID']
        todays_date = date.today()
        d = timedelta(days=3)
        Order_Date= todays_date.day
        Order_Month=todays_date.month
        Order_Year=todays_date.year
        Ship_Date=todays_date+d
        Order_ID=session['max']+1
        session['max']+=1
        print(Region,'loli')
        db.session.add(Sales(Region=Region,Order_Priority =Order_Priority,Item_Type =Item_Type,Units_Sold =Units_Sold,
                             Unit_Cost =Unit_Cost,Total_Cost =Total_Cost,Total_Profit =Total_Profit,Sales_Channel =Sales_Channel,
                             Country =Country,Unit_Price =Unit_Price,Total_Revenue=Total_Revenue,Ship_Date=Ship_Date,Order_Day=Order_Date,
                             Order_Month=Order_Month,Order_Year=Order_Year,Order_Date=todays_date,Order_ID=Order_ID))
        db.session.commit()
        return redirect(url_for('sales'))
    else:
        print("nahi hua")
        return redirect(url_for('sales'))




@app.route('/track_performance', methods=["GET", "POST"])
def track_performance():
    if session.get('user') is None:
        print("HAHAHAGA")
        return redirect(url_for('register'))
    if request.method == "GET":
        sales_data=[]
        result = [row.EmpID for row in Employees.query.with_entities(Employees.EmpID).filter(Employees.DeptID == 19)]
        for i in result:
            k=sum([row.Total_Profit for row in Sales.query.with_entities(Sales.Total_Profit).filter(Sales.Employee==i)])
            l=len([row.Total_Profit for row in Sales.query.with_entities(Sales.Total_Profit).filter(Sales.Employee==i)])
            print(i,k,l)
            columns=['EmpID','Total_Sales','Total_Profit']
            sales_d=[i,l,k]
            sales_data.append(sales_d)
        return render_template('perf_track.html',headings=columns,data=sales_data,user=session['id'])

@app.route('/my_achievements', methods=["GET", "POST"])
def my_achievements():

    if request.method=="GET":
        arr1=[]
        admin = Employees.query.filter_by(email=session['user']['email']).first()
        # print(admin)
        # print(admin.number_of_medals)
        k=admin.number_of_medals
        for i in range(k):
            arr1.append('static/imgs/medal'+str(i)+'.png')
        lol=[]
        for i in session['month']:
            if i[0]==session['user']['EmpID']:
                lol.append(i[1])


        return render_template('achieve.html',user=session['id'],arr=arr1,lol=lol)

@app.before_first_request
def _run_on_start():

        sale = Sales.query.all()
        #print(sale)
        session['max']=max([i.__dict__["Order_ID"] for i in sale])
        # print(session['max'])
        #print(sale)
        #print(tuplefied_list)
        #print([i.__dict__ for i in sale],'LOL')
        d= [i.__dict__ for i in sale]
        df = pd.DataFrame(d)
        df.drop(['_sa_instance_state'],axis=1,inplace=True)
        # print(df.columns)

        df_agg = df.groupby(['Order_Month', 'Employee']).agg({'Total_Profit': sum}).reset_index()


        k=df_agg.sort_values(['Order_Month','Total_Profit'],ascending=[True,False])
        t=k.groupby(['Order_Month']).head(1)
        Month=1
        arr=[]
        a=0
        session['month']=[]
        for index, row in t.iterrows():
            a=row['Employee']
            arr.append(a)
            datetime_object = datetime.strptime(str(Month), "%m")
            month_name = datetime_object.strftime("%B")
            session['month'].append([int(row['Employee']),month_name.upper()])
            Month+=1
        print(session['month'])
        for i in set(arr):
            arr.count(i)
            print(i,arr.count(i))
            #update set medals received=arr.count(i) where EmployeeID=i;
            admin = Employees.query.filter_by(EmpID=i).first()
            print(admin)

            admin.number_of_medals = arr.count(i)
            db.session.commit()
        session['preds'] = []
        print("ZZ",session['preds'])


@app.route('/emp_profile', methods=["GET", "POST"])
def emp_profile():
    return render_template('emp_profile.html',user=session['user']['Employee_Name'],dob=session['user']['DOB'],sex=session['user']['Sex'],email=session['user']['email'],medal=session['user']['number_of_medals'])

@app.route('/admin_profile', methods=["GET", "POST"])
def admin_profile():
    return render_template('profile_admin.html',user=session['user']['Employee_Name'],dob=session['user']['DOB'],sex=session['user']['Sex'],email=session['user']['email'],medal=session['user']['number_of_medals'])


@app.route("/bookmarks", methods=["GET", "POST"])
def bookmarks():
    if request.method =="GET" or request.method =="POST":
        msg=""
        bkmrk = Bookmarks.query.all()
        print(session['id'])
        lol = session['id']
        if len(bkmrk)>0:
            col1 = bkmrk[0].__dict__
            cols=col1
            #del cols["_sa_instance_state"]
            cols = cols.keys()
            arr = []
            for k in bkmrk:
                # k.Employee,logger)
                # print("BHAG CHOMU")
                z = k.__dict__
                # print(z)
                del z["_sa_instance_state"]
                # print(z.keys())
                # print(z)
                # print(z.values())

                arr.append(list(z.values()))
        else:
            msg="No bookmarks added. Predict a performance to bookmark"
            arr=[]
            cols=[]
        return render_template('bookmarks.html',headings=cols,data=arr,msg=msg,user1=lol)

@app.route("/remove_bookmarks", methods=["GET", "POST"])
def remove_bookmarks():
    if request.method=="POST":
        z=request.form['lol']
        print(z)
        Bookmarks.query.filter_by(ID=z).delete()

        db.session.commit()
        return redirect(url_for('bookmarks'))

@app.route("/add_bookmarks", methods=["GET", "POST"])
def add_bookmarks():
    if request.method=="POST":
        y=request.form['lol']
        a=Employees.query.filter_by(EmpID=y).first()
        print(type(a),a)

        db.session.add(Bookmarks(ID=a.EmpID,Name=a.Employee_Name,Number_of_medals=a.number_of_medals))
        db.session.commit()
        return redirect(url_for('welcome'))

@app.route('/lead_track', methods=["GET", "POST"])
def lead_track():
    lead=Leads.query.all()
    d = [i.__dict__ for i in lead]
    df = pd.DataFrame(d)
    #print(df)
    df.drop(['_sa_instance_state'], axis=1, inplace=True)
    df = df.replace('Select', np.nan)

    #FOR PIE CHARTZ
    #print(df.City.describe())
    df['City'] = df['City'].replace(np.nan, 'Mumbai')
    group_by = df['City'].value_counts(normalize=True)
    print(group_by)
    my_data = group_by.to_numpy()
    print(my_data)
    my_labels = ['Mumbai', 'Thane & Outskirts', 'Other Cities', 'Other Cities of Maharashtra', 'Other Metro Cities', 'Tier II Cities']
    labels = list(my_labels)
    my_explode = (0.1, 0, 0, 0, 0, 0)
    plt.pie(my_data, labels= labels, autopct='%1.1f%%', shadow = True, explode = my_explode)
    plt.title('Location')
    plt.axis('equal')
    plt.savefig('static/imgs/PIE.png',bbox_inches='tight')

    #FOR BAR GRAPHZ2
    df.Specialization.describe()
    fig, axs = plt.subplots(figsize=(15, 7.5))
    xticks(rotation=90)
    df['Specialization'] = df['Specialization'].replace(np.nan, 'Others')
    k=sns.countplot(df.Specialization)
    figure =k.get_figure()
    plt.tight_layout()
    figure.savefig('static/imgs/Specialization.png',bbox_inches='tight');
    #round(100 * (df.isnull().sum() / len(df.index)), 2)
    #df.Tags.describe()
    #sns.countplot(data.Tags)
    # xticks(rotation = 90)
    # df['Tags'] = df['Tags'].replace(np.nan, 'Will revert after reading the email')
    # #df['What_matters_most to you in choosing a course'].describe()
    # df['What_matters_most_to_you_in_a_course'] = df['What_matters_most_to_you_in_choosing_a_course'].replace(np.nan, 'Better Career Prospects')
    # #df['What is your current occupation'].describe()
    df['Lead_Source'] = df['Lead_Source'].replace(['google'], 'Google')
    df['Lead_Source'] = df['Lead_Source'].replace(
        ['Click2call', 'Live Chat', 'NC_EDM', 'Pay per Click Ads', 'Press_Release',
         'Social Media', 'WeLearn', 'bing', 'blog', 'testone', 'welearnblog_Home', 'youtubechannel'], 'Others')
    # sns.countplot(x = "Lead Source", hue = "Converted", data = data)
    # xticks(rotation = 90)  #ishaan's format
    #graph 3

    k = df.groupby(["Lead_Source", "Converted"]).count()
    k = k["Country"]
    z = pd.DataFrame(k).unstack().values[:, :, np.newaxis]
    z
    fig, axs = plt.subplots(figsize=(12, 12.5))
    x = ['Prospects', 'Converted']
    q = z[0].flatten()
    w = z[1].flatten()
    e = z[2].flatten()
    r = z[3].flatten()
    t = z[4].flatten()
    u = z[5].flatten()
    i = z[6].flatten()
    o = z[7].flatten()
    p = z[8].flatten()
    plt.bar(x, q, color='r')
    plt.bar(x, w, bottom=q, color='b')
    plt.bar(x, e, bottom=q + w, color='y')
    plt.bar(x, r, bottom=q + w + e, color='g')
    plt.bar(x, t, bottom=q + w + e + r, color='c')
    plt.bar(x, u, bottom=q + w + e + r + t, color='m')
    plt.bar(x, i, bottom=q + w + e + r + t + u, color='darkviolet')
    plt.bar(x, o, bottom=q + w + e + r + t + u + i, color='aqua')
    plt.bar(x, p, bottom=q + w + e + r + t + u + i + o, color='peru')
    plt.xlabel("Leads")
    plt.ylabel("Count")
    plt.legend(["Direct Traffic", "Facebook", "Google", "Olark Chat", "Organic Search", "Others", "Reference",
                "Referral Sites",
                "Welingak Website"])
    plt.title("Lead Origin Prospect-Conversion Ratio Chart")
    plt.savefig('static/imgs/StackedBar.png')
    #GRAPH NO.4
    # df['TotalVisits'].describe(percentiles=[0.05, .25, .5, .75, .90, .95, .99])
    # #print(type(df['TotalVisits'][0]),'loltttttttt')
    # df['TotalVisits']=df['TotalVisits'].astype('float')
    # #print(type(df['TotalVisits'][0]), 'loltttttttt')
    # percentiles = df['TotalVisits'].quantile([float(0.05), float(0.95)]).values
    # df['TotalVisits'][df['TotalVisits'] <= percentiles[0]] = percentiles[0]
    # df['TotalVisits'][df['TotalVisits'] >= percentiles[1]] = percentiles[1]
    # df['Total_Time_Spent_on_Website'].describe()
    # df['Page_Views_Per_Visit'].describe()
    # percentiles = df['Page_Views_Per_Visit'].quantile([0.05, 0.95]).values
    # df['Page_Views_Per_Visit'][df['Page_Views_Per_Visit'] <= percentiles[0]] = percentiles[0]
    # df['Page_Views_Per_Visit'][df['Page_Views_Per_Visit'] >= percentiles[1]] = percentiles[1]
    # df['Last_Activity'] = df['Last_Activity'].replace(['Had a Phone Conversation', 'View in browser link Clicked',
    #                                                        'Visited Booth in Tradeshow', 'Approached upfront',
    #                                                        'Resubscribed to emails', 'Email Received',
    #                                                        'Email Marked Spam'], 'Other_Activity')
    # fig, axs = plt.subplots(figsize=(10, 5))
    # sns.countplot(x="Last Activity", hue="Converted", data=df)
    # xticks(rotation=90)
    # plt.savefig('LastBar.png')
    plt.cla()
    plt.clf()
    return render_template('leadgraphs.html',user=session['user']['Employee_Name'])


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """

    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'

    return response

if __name__ == '__main__':
    app.secret_key = "ThisIsNotASecret:p"
    app.run(debug=True)
