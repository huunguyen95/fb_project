from PyQt5.QtSql import QSqlQuery, QSqlDatabase

con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("user.sqlite")
con.open()


username = "linda@example.com"
password = "aaaaaa"
fa = "12345"
ip = "192.168.0.2"
status = "logged in"

query = QSqlQuery()
query.exec(
     f"""INSERT INTO user (username, password, fa, ip, status)
    VALUES ('{username}', '{password}', '{fa}', '{ip}', '{status}')"""
)
