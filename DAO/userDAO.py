import sqlite3
from Been.UserBean import UserBean
from Config import Config

class UserDAO:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def create_table(self):
        self.connect()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                assets INTEGER,
                department INTEGER,
                description TEXT
            )
        ''')
        self.conn.commit()
        self.disconnect()

    def insert_user(self, user: UserBean):
        self.connect()
        self.cursor.execute('INSERT INTO users (id, name,assets,department,description) VALUES (?, ?, ?, ?, ?)',
                            (user.id, user.name, user.assets, user.department, user.description))
        self.conn.commit()
        self.disconnect()

    def get_user_by_id(self, user_id):
        self.connect()
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = self.cursor.fetchone()
        self.disconnect()
        return user

    def get_all_users(self):
        self.connect()
        self.cursor.execute('SELECT * FROM users')
        users = self.cursor.fetchall()
        self.disconnect()
        return users

    def delete_user(self, user_id):
        self.connect()
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()
        self.disconnect()


# 使用示例
if __name__ == "__main__":
    user_dao = UserDAO(Config.get_config()['database']['path'])

    # 创建表格
    user_dao.create_table()

    # 插入用户
    user_dao.insert_user(UserBean(id="zhangsan3", name="张三", assets=1, department="社畜科", description=""))

    # 获取所有用户
    all_users = user_dao.get_all_users()
    print("All Users:", all_users)
    print(type(all_users[0]))

    # 删除用户
    user_dao.delete_user("zhangsan3")

    # 获取特定用户
    user = user_dao.get_user_by_id("zhangsan3")
    print("User with ID 1:", user)
