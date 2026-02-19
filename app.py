from flask import *
import pymysql

app = Flask(__name__)

@app.route("/api/signup",methods=["POST"])
def signup():
    username= request.form['username']
    email= request.form['email']
    phone= request.form['phone']
    password= request.form['password']

    print(username,email,phone,password)
    #create connection to DB
    connection = pymysql.connect(host="localhost", user="root", password="", database="brighton_sokogarden")
    #create cursor to handle sql queries
    cursor = connection.cursor()
    #create ther sql query
    sql = "insert into users(username,email,phone,password) values(%s, %s, %s, %s)"
    # data to be saved
    data = (username, email, phone, password)
    print(data)

    # execute the sql query
    cursor.execute(sql, data)
    # save the data
    connection.commit()
    # return response
    return jsonify({"message":"Sign up successful                                                                                                                                                                                                                                                                                                                                                                                                                        "})


# quioz 2 login
@app.route("/api/signin",methods=["POST"])
def signin():
    email=request.form['email']
    password=request.form['password']

    print(email,password)
# connection to db
    connection = pymysql.connect(host="localhost",user="root", password="",database="brighton_sokogarden")


    # create cursor to handle sql queries
    cursor =connection.cursor(pymysql.cursors.DictCursor)
    # create the sql query
    sql = "select user_id,username, email,password from users where email=%s and password =%s"
    # data to execute the query
    data = (email,password)

    # execute the query
    cursor.execute(sql,data)

    # check for resulting rows
    if cursor.rowcount ==0:
        return jsonify({"message": "invalid credentials"})
    else:
        # get user data
        user = cursor.fetchone()
        return jsonify({"message": "login successfull", "user": user})
    


# return a response
    



if __name__=="__main__":
    app.run(debug=True)


























































































































































































































































































