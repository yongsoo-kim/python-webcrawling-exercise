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

try:
    with conn.cursor() as c:
        #Data update1
        c.execute("UPDATE users SET username =%s WHERE id =%s",('yongsoo',1) )
        # Data update2
        c.execute("UPDATE users SET username ='%s' WHERE id ='%d'" % ('jessica', 2))

        #data check 1
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 >', row)

        #Data delete 1
        c.execute("DELETE FROM users WHERE id=%s",(1,))
        # Data delete 2
        c.execute("DELETE FROM users WHERE id='%s'", (2,))


        #data check 2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in c.fetchall():
            print('check1 >', row)

    conn.commit()
finally:
    conn.close()



# try:
#     # default result is tuple
#     # with conn.cursor() as c:
#
#     # You can get in format of dictionary like this:
#     with conn.cursor(pymysql.cursors.DictCursor) as c:
#
#         c.execute("SELECT * FROM users")
#         # 1 row
#         # print(c.fetchone())
#         # selected  3 rows
#         # print(c.fetchmany(3))
#         # fetch all
#         # print(c.fetchall())
#
#         # Loop 1
#         c.execute("SELECT * FROM users ORDER BY id ASC")
#         rows = c.fetchall()
#         for row in rows:
#             print('usage1 >', row)
#
#         # Loop2
#         c.execute("SELECT * FROM users ORDER BY id DESC")
#         for row in c.fetchall():
#             print('usage2 >', row)
#
#         # condition 1
#         param1 = (1,)
#         c.execute("SELECT * FROM users WHERE id = %s", param1)
#         print('param1', c.fetchall())
#
#         # condition 2
#         param2 = 1
#         c.execute("SELECT * FROM users WHERE id = '%d'" % param2)
#         print('param2', c.fetchall())
#
#         # condition 3
#         param3 = (4, 5)
#         c.execute("SELECT * FROM users WHERE id IN(%s,%s)", param3)
#         print('param1', c.fetchall())
#
#         # condition 4
#         param4 = (4, 5)
#         c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % param4)
#         print('param1', c.fetchall())
#
# finally:
#     conn.close()

# # pymysql version check(0.9.3)
# # print('pymysql.version',pymysql.__version__)
#
# # select database(python_01 -> hr)
# # conn.select_db('hr')
#
# # Cursor connection
# c = conn.cursor()
# print(type(c))
#
# # Database creation
# # c.execute('create database python_02')
#
# # Close cursor -> Resource will be returned!(good)
# # c.close()
#
# # Connection close
# # conn.close()
#
# # Connection & cursor can be closed by 'with' statements.
#
# # Transaction start.
# # conn.begin()
#
# # Commit
# # conn.commit()
#
# # Rollback
# # conn.rollback()
#
# # Create datetime
# now = datetime.datetime.now()
# nowDateTime = now.strftime('%Y-%m-%d %H:%M:%S')
# print('nowDateTime', nowDateTime)
# # print(type(now))
# # print(type(nowDateTime))
#
# # This can also work.
# # sql = """
# # CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL,\
# #                                             username varchar(20), \
# #                                             email varchar(30), \
# #                                             phone varchar(30), \
# #                                             website varchar(30), \
# #                                             regdate varchar(20) NOT NULL, PRIMARY KEY(id))"
# #
# # """
#
# c.execute("CREATE TABLE IF NOT EXISTS users(id bigint(20) NOT NULL,\
#                                             username varchar(20), \
#                                             email varchar(30), \
#                                             phone varchar(30), \
#                                             website varchar(30), \
#                                             regdate varchar(20) NOT NULL, PRIMARY KEY(id))")
#
# # conn.commit()
# # c.execute("CREATE TABLE IF NOT EXISTS users(id int(20) NOT NULL, username varchar(20), email varchar(30), phone varchar(30), website varchar(30), regdate varchar(20) NOT NULL, PRIMARY KEY(id))")
#
#
# try:
#     with conn.cursor() as c:
#         # Json to Mysql
#         with open('./user-json/users.json', 'r') as infile:
#             r = json.load(infile)
#             userData = []
#             for user in r:
#                 # Make a tuple
#                 t = (user['id'], user['username'], user['email'], user['phone'], user['website'], nowDateTime)
#                 userData.append(t)
#             c.executemany("INSERT INTO users(id,username,email,phone,website, regdate) VALUES (%s, %s, %s, %s, %s, %s)",userData)
#         conn.commit()
# finally:
#     conn.close()
