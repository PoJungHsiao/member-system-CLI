# 建立資料庫(初始化)
import pymysql
from config import db_config, db_name

# 連線到MySQL server並建立指令游標
with pymysql.connect(**db_config) as conn, conn.cursor() as cursor:
    # 建立一新的資料庫
    cursor.execute(
        f"CREATE DATABASE IF NOT EXISTS {db_name} DEFAULT CHARACTER SET utf8mb4"
    )

# 連線到剛建立的資料庫
with pymysql.connect(database=db_name, **db_config) as conn, conn.cursor() as cursor:
    # 建立資料表
    sql = '''CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE,
        password BLOB NOT NULL,
        create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        DEFAULT CHARACTER SET utf8mb4 
'''
    cursor.execute(sql)
    print("users 資料表建立完成")
