import os
from dotenv import load_dotenv  # 載入讀取環境變數套件
import pymysql
# 讀取環境變數
load_dotenv()

# 資料庫伺服器連線設定
db_config = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT")),
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}
# 拿出資料庫名字(連線與資料庫名字分開較好指定資料庫)
db_name = os.getenv("DB_NAME")
