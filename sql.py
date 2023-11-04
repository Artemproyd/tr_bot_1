import sqlite3

class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self, user_id):
        """РџСЂРѕРІРµСЂСЏРµРј, РµСЃС‚СЊ Р»Рё СЋР·РµСЂ РІ Р±Р°Р·Рµ"""
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id))
        return bool(len(result.fetchall()))

    def get_user_id(self, user_id):
        """Р”РѕСЃС‚Р°РµРј id СЋР·РµСЂР° РІ Р±Р°Р·Рµ РїРѕ РµРіРѕ user_id"""
        result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()

    def add_user(self, user_id, st):
        """Р”РѕР±Р°РІР»СЏРµРј СЋР·РµСЂР° РІ Р±Р°Р·Сѓ"""
        self.cursor.execute("INSERT INTO `users` (`user_id`, 'lan', 'phot', 'mx_phot') VALUES (?, ?, ?, ?)", (user_id, 0, 0 , 19))
        return self.conn.commit()
    
    def update_lan(self, a, user_id):
        self.cursor.execute("UPDATE users SET lan = ? WHERE user_id = ?", (a, user_id))
        return self.conn.commit()
    
    def update_vg(self, a, user_id):
        self.cursor.execute("UPDATE users SET vg = ? WHERE user_id = ?", (a, user_id))
        return self.conn.commit()
    
    def update_phot(self, a, user_id):
        self.cursor.execute("UPDATE users SET phot = ? WHERE user_id = ?", (a, user_id))
        return self.conn.commit()
        
    def close(self):
        """Р—Р°РєСЂС‹РІР°РµРј СЃРѕРµРґРёРЅРµРЅРёРµ СЃ Р‘Р”"""
        self.connection.close()
