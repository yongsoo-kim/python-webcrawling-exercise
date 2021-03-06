import pymysql
import simplejson as json
import datetime

# MySQL Connection start
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       password='sesame',
                       db='python_01',
                       charset='utf8')

# pymysql version check(0.9.3)
# print('pymysql.version',pymysql.__version__)

# select database(python_01 -> hr)
# conn.select_db('hr')

# Cursor connection
c = conn.cursor()
print(type(c))

# Database creation
# c.execute('create database python_02')

# Close cursor -> Resource will be returned!(good)
# c.close()

# Connection close
# conn.close()

# Connection & cursor can be closed by 'with' statements.

# Transaction start.
# conn.begin()

# Commit
# conn.commit()

# Rollback
# conn.rollback()

# Create datetime
now = datetime.datetime.now()
nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
print('nowDateTime', nowDateTime)
# print(type(now))
# print(type(nowDateTime))

# This can also work.
# sql = """
# CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL,\
#                                             username varchar(20), \
#                                             email varchar(30), \
#                                             phone varchar(30), \
#                                             website varchar(30), \
#                                             regdate varchar(20) NOT NULL, PRIMARY KEY(id))"
#
# """

c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL,\
                                            username varchar(20), \
                                            email varchar(30), \
                                            phone varchar(30), \
                                            website varchar(30), \
                                            regdate varchar(20) NOT NULL, PRIMARY KEY(id))")

# conn.commit()
# c.execute("CREATE TABLE IF NOT EXISTS users(id int(20) NOT NULL, username varchar(20), email varchar(30), phone varchar(30), website varchar(30), regdate varchar(20) NOT NULL, PRIMARY KEY(id))")


try:
    with conn.cursor() as c:
        # Json to Mysql
        with open('./user-json/users.json', 'r') as infile:
            r = json.load(infile)
            userData = []
            for user in r:
                # Make a tuple
                t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDateTime)
                userData.append(t)
            c.executemany("INSERT INTO users(id,username,email,phone,website, regdate) VALUES (%s, %s, %s, %s, %s, %s)",userData)
        conn.commit()
finally:
    conn.close()