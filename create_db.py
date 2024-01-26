import sys

from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("user.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)

# Create a query and execute it right away using .exec()
createTableQuery = QSqlQuery()
createTableQuery.exec(
    """
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        username VARCHAR(40) NOT NULL,
        password VARCHAR(50) NOT NULL,
        fa VARCHAR(40) NOT NULL,
        ip VARCHAR(40) ,
        status VARCHAR(40) NOT NULL
    )
    """
)

print(con.tables())