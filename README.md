# 🔐 CLI 會員系統 - 使用 Python、MySQL、bcrypt

## 📌 專案簡介
這是一個以命令列介面（CLI）為基礎的會員系統，提供使用者註冊與登入功能，
後端使用 MySQL 資料庫，並透過 `bcrypt` 實作密碼加密，強化帳號資訊的安全性。

---

## 🛠️ 技術與工具
- Python：撰寫主程式與資料庫邏輯
- MySQL：使用者資料儲存
- PyMySQL：連接 Python 與 MySQL
- bcrypt：密碼加密與驗證

---

## 🚀 功能列表
- ✅ 使用者註冊（避免帳號重複）
- ✅ 密碼使用 `bcrypt` 加密儲存
- ✅ 使用者登入（加密密碼比對）
- ✅ 自動建立資料庫與資料表
- ✅ CLI 互動式選單介面

---

## 🧰 專案結構
member_system/
1. .env              ← 資料庫連線設定（不公開）
2. config.py         ← 統一管理 db_config、載入 .env
3. init_db.py        ← 建立資料庫與資料表（只跑一次）
4. main.py           ← 主程式登入註冊邏輯
5. .gitignore        ← 忽略 .env 等敏感資料
6. requirements.txt  ← 安裝需要的套件清單

---

## 🖥️ 如何執行
1. 安裝套件
2. 建立使用者與資料庫(init_db.py)
3. 執行主程式(main.py)

---

## 📚 心得筆記
本專案學習到 bcrypt 密碼加密實作、PyMySQL 資料庫操作、會員系統邏輯設計，並強化了系統安全意識與資料完整性設計能力。

---

## 🧑‍💻 作者
GitHub: PoJungHsiao(https://github.com/PoJungHsiao)
Email: happy10246308@gmail.com
