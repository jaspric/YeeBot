import sqlite3

class Memebucks:
    def __init__(self, yeebot):
        self.yeebot = yeebot
        self.conn = sqlite3.connect('db/yee.db')
        self.cur = self.conn.cursor()

    def check_if_exists(self, user_id):
        self.cur.execute("SELECT meme_bucks FROM users WHERE user_id = ?;", (user_id,))
        row = self.cur.fetchone()
        if row:
            return True
        else:
            return False
 
    def check_balance(self, user_id):
        self.cur.execute("SELECT meme_bucks FROM users WHERE user_id = ?", (user_id,))    
        row = self.cur.fetchone()
        print('Balance checked.')
        return row[0]
 

    def withdraw(self, user_id, amount):
        self.cur.execute("UPDATE users set meme_bucks = meme_bucks - ? WHERE user_id = ?", (amount, user_id))
        self.conn.commit()
            

    def deposit(self, user_id, amount):
        self.cur.execute("UPDATE users set meme_bucks = meme_bucks + ? WHERE user_id = ?", (amount, user_id))
        self.conn.commit()
