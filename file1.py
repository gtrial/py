import cx_Oracle

host = 'testdb.247ms.com'
port = 1521
sid = 'DESHP03'
username = 'music_247'
password = 'munchen'

dsn = cx_Oracle.makedsn(host, port, sid)
conn = cx_Oracle.connect(username, password, dsn)
print(conn.version)
conn.close()