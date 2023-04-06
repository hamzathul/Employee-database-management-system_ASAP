import mysql.connector


# import project1_frontend

def empData():
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="project")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS Mgm(id integer primary key AUTO_INCREMENT,empID text,name text,salary text,dept text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()


def addempRec(empID, name, salary, dept, Age, Gender, Address, Mobile):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("INSERT INTO Mgm VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",
                (empID, name, salary, dept, Age, Gender, Address, Mobile))
    con.commit()
    con.close()


def viewData():
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("select * from Mgm")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(id):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("DELETE FROM Mgm WHERE id=%s", (id,))
    con.commit()
    con.close()


def searchData(empID, name, salary, dept, Age, Gender, Address, Mobile):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute(
        "SELECT * FROM Mgm WHERE empID=%s or name=%s or salary=%s or dept=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",
        (empID, name, salary, dept, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, empID="", name="", salary="", dept="", Age="", Gender="", Address="", Mobile=""):  #
    con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute(
        "UPDATE Mgm SET empID=%s,name=%s,salary=%s,dept=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",
        (empID, name, salary, dept, Age, Gender, Address, Mobile))
    con.commit()
    con.close()