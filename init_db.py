# Read and execute SQL file
import pymysql
from rf4_wiki_scrapy.settings import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT

connection = pymysql.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    port=MYSQL_PORT,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

with open(r'db.sql', 'r', encoding='utf-8') as f:
    sql_script = f.read()
    print(sql_script)
for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)
connection.commit()