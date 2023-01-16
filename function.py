import pymysql as p
def connect():
    return p.connect(host='localhost',user='root',password='',database='blogauthor',port=3306)
def addregauth(t):
    con=connect()
    cur=con.cursor()
    sql='insert into regdata values(%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()
def addreguser(t):
    con=connect()
    cur=con.cursor()
    sql='insert into user values(%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()
def logdetailsauth(t):
    con=connect()
    cur=con.cursor()
    sql='select email,password from regdata where email=%s'
    cur.execute(sql,t[0])
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
def logdetailsuser(t):
    con=connect()
    cur=con.cursor()
    sql='select email,password from user where email=%s'
    cur.execute(sql,t[0])
    data=cur.fetchall()
    con.commit()
    con.close()
    return data
def newblog(t):
    con=connect()
    cur=con.cursor()
    sql='insert into blog values(%s,%s,%s)'
    cur.execute(sql,t)
    con.commit()
    con.close()
def showall():
    con=connect()
    cur=con.cursor()
    sql='select * from blog'
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data