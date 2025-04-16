import pymysql  # 資料庫套件
import bcrypt  # 密碼加密套件
from config import db_config, db_name

# 註冊函式


def register():
    username = input("請設定帳號 : ").strip()  # 去除前後空格，統一帳號格式
    password = input("請設定密碼 : ")
    # 密碼加密
    hash_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # 連線檢查資料庫內帳號是否存在
    with pymysql.connect(database=db_name, **db_config) as conn, conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        result = cursor.fetchone()

        if result is not None:
            print("帳號已存在，請重新註冊")
        else:
            # 新增資料到資料庫
            sql = "INSERT INTO users(username, password) VALUES (%s, %s)"
            cursor.execute(sql, (username, hash_pw))
            print("註冊成功")

# 登入函式


def login():
    username = input("請輸入帳號 : ").strip()
    password = input("請輸入密碼 : ")
    # 檢查帳號密碼
    # 檢查帳號是否存在
    with pymysql.connect(database=db_name, **db_config) as conn, conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE username = %s"
        cursor.execute(sql, (username,))
        user = cursor.fetchone()
        # 確認帳號存在後比對密碼
        if user:
            check_pw = bcrypt.checkpw(password.encode(
                'utf-8'), user['password'])
            if check_pw:
                print(f"登入成功 ! 歡迎回來，{username} !")
            else:
                print("密碼錯誤，請重新輸入")

        else:
            print("查無此帳號，請重新輸入")


# 主程式
while True:
    print("歡迎來到會員系統")
    print("1. 註冊")
    print("2. 登入")
    print("3. 離開")
    choice = input("請選擇服務 (1/2/3) : ")

    if choice == "1":
        # 呼叫註冊函式
        register()
    elif choice == "2":
        # 呼叫登入函式
        login()
    elif choice == "3":
        print("感謝使用，再見!")
        break
    else:
        print("請選擇有效服務")
