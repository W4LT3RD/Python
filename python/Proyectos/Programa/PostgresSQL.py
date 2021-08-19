import psycopg2

# Global constant
PSQL_HOST = "localhost"
PSQL_USER = "postgres"
PSQL_PASS = "135792468"
PSQL_DB = "postgres"

# Connection
connection = psycopg2.connect(
    PSQL_HOST,
    PSQL_DB, 
    PSQL_USER, 
    PSQL_PASS 
)
print("Conxión exitosa :)")

cursor = connection.cursor()

# Query
SQL = "SELECT * FROM Distro;"
cursor.execute(SQL)

# Get Values
all_values = cursor.fetchall()

cursor.close()
connection.close()

print('Get values: ', all_values)
