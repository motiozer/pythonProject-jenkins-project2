import pymysql



def user_post(user_id, user_name):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzlEesltcX', passwd='wuNwg4KL7Y', db='QzlEesltcX')
    conn.autocommit(True)
    cursor = conn.cursor()
    sql="INSERT into QzlEesltcX.users1 (user_id, user_name,creation_date) VALUES (%s, %s, %s)"
    val=(user_id, user_name, '2.2.21')
    try:
        cursor.execute(sql, val)
        return(True)
    except:
        print("Wrong user Id")
        return(False)
    cursor.close()
    conn.close()

def user_get(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzlEesltcX', passwd='wuNwg4KL7Y', db='QzlEesltcX')

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Getting all data from table “users”
    sql="SELECT user_name,user_id FROM QzlEesltcX.users1 WHERE user_id=%s"
    try:
        cursor.execute(sql,user_id)
        user_name,user_id=cursor.fetchone()
        cursor.close()
        conn.close()
        return(user_name)
    except:
        print('userID does not exist')
        cursor.close()
        conn.close()
        return False

def user_del(user_id):
    # Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzlEesltcX', passwd='wuNwg4KL7Y', db='QzlEesltcX')
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Deleting data into table
    sql="DELETE FROM QzlEesltcX.users1 WHERE user_id =%s"
    val=user_id
    cursor.execute(sql, val)
    if cursor.rowcount > 0:
        cursor.close()
        conn.close()
        return True
    else :
        cursor.close()
        conn.close()
        return False

def user_put(user_id,user_name):
# Establishing a connection to DB
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='QzlEesltcX', passwd='wuNwg4KL7Y', db='QzlEesltcX')
    conn.autocommit(True)

# Getting a cursor from Database
    cursor = conn.cursor()

# Updating data inside the table
    sql="UPDATE QzlEesltcX.users1 SET user_name =%s WHERE user_id =%s"
    val=(user_name,user_id)
    cursor.execute(sql,val)
    if cursor.rowcount > 0:
        cursor.close()
        conn.close()
        return True
    else:
        cursor.close()
        conn.close()
        return False

print(user_put(201,'jonfeee'))
