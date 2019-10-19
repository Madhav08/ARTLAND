from flask import Flask, render_template, request
import mysql.connector

mydb = mysql.connector.connect(host="127.0.0.1",
                                user="root",
                                password="root",
                                database="agms",
                                auth_plugin='mysql_native_password')
mycursor = mydb.cursor()

app=Flask(__name__)

curr_user = ""
curr_user_type=""

@app.route('/toLogin', methods = ['POST','GET'])
def home1():
    return render_template("login.html")

@app.route('/',methods = ['POST','GET'])
def home2():
    return render_template("register.html")
    #return render_template('wishlist.html')

@app.route('/signIn', methods = ['POST', 'GET'])
def signIn():
    global curr_user
    global curr_user_type
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        print(username)
        print(password)
        myquery = "select exists(select * from users where username=%s)"
        rec_tup = (username,)
        mycursor.execute(myquery, rec_tup)
        if mycursor.fetchone()[0]==1:
            new_query = "select password from users where username=%s"
            mycursor.execute(new_query, rec_tup)
            if mycursor.fetchone()[0]==password:
                curr_user = username
                req_query = "select usertype from users where username=%s"
                mycursor.execute(req_query,rec_tup)
                curr_user_type=mycursor.fetchone()[0]
                return render_template("homepage.html")
            else:
                return render_template('Err.html', message="Username/Password Wrong")
        else:
            return render_template('Err.html', message="Username/Password Wrong")

@app.route('/signUp', methods = ['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        name = request.form["name"]
        username = request.form["username"]
        password = request.form["password"]
        confirmPassword = request.form["cnfpassword"]
        usertype = request.form["usertype"]
        email = request.form["email"]

        print(name, username, password, email)
        
        myquery = "select exists(select * from users where username=%s)"
        rec_tup = (username,)
        mycursor.execute(myquery, rec_tup)
        if mycursor.fetchone()[0]==1:
            return render_template('Err.html', message="Username already exists")
        elif password!=confirmPassword:
            return render_template('Err.html', message="Passwords Don't Match")
        else:
            mysql_query = "insert into users values(%s, %s, %s, %s, %s)"
            records = (name, username, password, email, usertype)
            mycursor.execute(mysql_query, records)
            print(name, username, password, email, usertype)
            mydb.commit()
        return render_template("login.html")

@app.route('/addArtToWishlist<id>', methods = ['POST', 'GET'])
def addArtToWishlist(id):
    if request.method == 'POST':
        # return render_template('Err.html', message="HELLO")
        if curr_user_type=="Customer":
            myquery = "select username, art_id from wishlist where username=%s"
            rec_tup = (curr_user,)           
            mycursor.execute(myquery,rec_tup)
            for i in mycursor.fetchall():
                print(i)
                if i[1]==id:
                    # return '<body>Art already in wishlist!</body>'
                    return render_template('Err.html', message="Art already in wishlist!")
                else:
                    continue
            mysql_query = "insert into wishlist values(%s, %s)"
            records = (curr_user, id)
            mycursor.execute(mysql_query, records)
            # print(name, username, password, email, usertype)
            mydb.commit()
            # return '<body>Art added to wishlist successfully!</body>'
            return render_template('Err.html', message="Art added to wishlist successfully!")
        else:
            # return '<body>Only customers are allowed to add art(s) to wishlist!</body>'
            return render_template('Err.html', message="Only customers are allowed to add art(s) to wishlist!")
    else:
        return render_template('Err.html', message="You are not allowed to add art to wishlist!")
        # return '<body>You are not allowed to add art to wishlist!</body>'

@app.route('/addArt', methods = ['POST', 'GET'])
def addArt():
    return render_template('addart.html')

@app.route('/insertArt', methods = ['POST', 'GET'])
def insertArt():
    if request.method == 'POST':
        art_id = request.form["art_id"]
        price = request.form["price"]
        if curr_user_type=="Artist":
            mysql_query = "insert into arts values(%s, %s, %s)"
            records = (curr_user, art_id, price)
            mycursor.execute(mysql_query, records)
            # print(name, username, password, email, usertype)
            mydb.commit()
            return render_template('Err.html', message="Art added successfully")
        else:
            return render_template('Err.html', message="Only artists are allowed to add art")

@app.route('/showWishlist', methods = ['POST', 'GET'])
def showWishlist():
    # global curr_user
    if request.method == 'POST':
        # fromDest = request.form["from"]
        # toDest = request.form["to"]
        # #depDate = request.form["depDate"]
        # classF = request.form["classF"]

        username = ""
        art_id = ""
        # a_code = []
        # depTime = []
        # arrTime = []
        # fare = []
        myquery = "select wishlist.art_id, arts.price from arts inner join wishlist on arts.art_id=wishlist.art_id where wishlist.username=%s"
        rec_tup = (curr_user,)
        mycursor.execute(myquery, rec_tup)
        data = mycursor.fetchall()
        print(data) 
        return render_template('showwishlist.html', data = data)
        # myquery = "select exists(select username, art_id from wishlist where username=%s)"
        # rec_tup = (curr_user,)
        # mycursor.execute(myquery, rec_tup)
        # if mycursor.fetchone()[0]==1:
        #     myquery = "select username, art_id from wishlist where username=%s"
        #     mycursor.execute(myquery, rec_tup)
        #     for i in mycursor.fetchall():
        #         username = i[0]
        #         art_id = i[1]
        #     return render_template("wishlist.html", username = username, art_id = art_id)
        # else:
        #     return "<body>No Flights Found according to your choices</body>"

@app.route('/userProfile', methods = ['POST', 'GET'])
def userProfile():
    # global curr_user
    if request.method == 'POST':
        # fromDest = request.form["from"]
        # toDest = request.form["to"]
        # #depDate = request.form["depDate"]
        # classF = request.form["classF"]

        name = ""
        username = ""
        email = ""        
        usertype = ""
        # a_code = []
        # depTime = []
        # arrTime = []
        # fare = []

        myquery = "select exists(select name, username, email, usertype from users where username=%s)"
        rec_tup = (curr_user,)
        mycursor.execute(myquery, rec_tup)
        if mycursor.fetchone()[0]==1:
            myquery = "select name, username, email, usertype from users where username=%s"
            mycursor.execute(myquery, rec_tup)
            for i in mycursor.fetchall():
                name = i[0]
                username = i[1]
                email = i[2]
                usertype = i[3]
            return render_template("userprofile.html", usertype = usertype, name = name, username = username, email = email)

@app.route('/logout', methods = ['POST', 'GET'])
def logout():
    curr_user=""
    curr_user_type=""
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)