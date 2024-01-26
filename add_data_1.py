# Creating a query for later execution using .prepare()
from PyQt5.QtSql import QSqlQuery,QSqlDatabase
import sys

# Create the connection
con = QSqlDatabase.addDatabase("QSQLITE")
con.setDatabaseName("user.sqlite")

# Open the connection
if not con.open():
    print("Database Error: %s" % con.lastError().databaseText())
    sys.exit(1)
insertDataQuery = QSqlQuery()
insertDataQuery.prepare(
    """
    INSERT INTO user (
        username,
        password,
        fa,
        ip,
        status
    )
    VALUES (?, ?, ?, ?, ?)
    """
)

# Sample data
data = [
    ("Joe", "Senior Web Developer", "joe@example.com", "1.1.1.1", "ok"),
    ("Lara", "Project Manager", "lara@example.com", "1.1.1.1", "ok"),
    ("David", "Data Analyst", "david@example.com", "1.1.1.1", "ok"),
    ("Jane", "Senior Python Developer", "jane@example.com", "1.1.1.1", "ok"),
]

# Use .addBindValue() to insert data
for username, password, fa, ip, status in data:
    insertDataQuery.addBindValue(username)
    insertDataQuery.addBindValue(password)
    insertDataQuery.addBindValue(fa)
    insertDataQuery.addBindValue(ip)
    insertDataQuery.addBindValue(status)
    insertDataQuery.exec()