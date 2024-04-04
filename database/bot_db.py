import sqlite3
from database import query


class Database():
    def __init__(self):
        self.connection = sqlite3.connect('tg_bot.db')
        self.cursor = self.connection.cursor()

    def creat_table(self):
        if self.connection:
            print('Connection established')
        self.connection.execute(query.CREATE_TG_USER_TABLE)
        self.connection.execute(query.CREATE_BAN_TABLE)
        self.connection.execute(query.CREATE_REGISTER_TABLE)
        self.connection.execute(query.CREATE_LIKE_DISLIKE_TABLE)
        self.connection.execute(query.CREATE_REFERRAL_TABLE)
        try:
            self.connection.execute(query.ALTER_R_USER_TABLE)
            self.connection.execute(query.ALTER_B_USER_TABLE)
        except sqlite3.OperationalError:
            pass
        self.connection.execute(query.CREATE_SCRAP_TABLE)
        self.connection.commit()

    def insert_user(self, tg_user_id, tg_username):
        self.cursor.execute(query.INSERT_TG_USER_TABLE, (None, tg_user_id, tg_username, None, 0))
        self.connection.commit()

    def insert_ban(self, tg_id, first_name):
        self.cursor.execute(query.INSERT_BAN_TABLE, (None, tg_id, first_name, 0))
        self.connection.commit()

    def select_count_bun_table(self, tg_id):
        self.cursor.execute(query.SELECT_COUNT_BAN_TABLE, (tg_id,))
        return self.cursor.fetchone()

    def update_count_bun_table(self, tg_id):
        self.cursor.execute(query.UPDATE_COUNT_BAN_TABLE, (tg_id,))
        self.connection.commit()

    def delete_user(self, tg_id):
        self.cursor.execute(query.DELETE_USER, (tg_id,))
        self.connection.commit()

    def select_from_ban(self):
        self.cursor.execute(query.SELECT_USER_FROM_BAN)
        rows = self.cursor.fetchall()
        return rows
    def insert_info(self, tg, name, bio, age, zodiac, gender, color, photo):
        self.cursor.execute(query.INSERT_REGISTER_TABLE, (None, tg, name, bio, age, zodiac, gender, color, photo))
        self.connection.commit()

    def select_id_info(self, tg):
        self.cursor.execute(query.SELECT_TG_ID_REGISTER_TABLE, (tg,))
        rows = self.cursor.fetchone()
        return rows

    def select_info_register_table(self, tg_id):
        self.cursor.execute(query.SELECT_INFO_REGISTER_TABLE, (tg_id,))
        row = self.cursor.fetchone()
        return row
    def insert_like_dislike_table(self, user, liker, what):
        self.cursor.execute(query.INSERT_LIKE_DISLIKE_TABLE, (None, user, liker, what))
        self.connection.commit()

    def select_all_registr(self, tg_id):
        self.cursor.execute(query.FILTER_LEFT_JOIN, (tg_id, tg_id))
        rows = self.cursor.fetchall()
        return rows
    def select_balance_totalreferral_table(self, tg_id):
        self.cursor.execute(query.DOUBLE_SELECT_REFERRAL_USER_QUERY, (tg_id,))
        row = self.cursor.fetchone()
        return row

    def select_all_from_tl_users(self, tg_id):
        self.cursor.execute(query.SELECT_ALL_USER_TL_USERS, (tg_id,))
        row = self.cursor.fetchone()
        return row

    def update_tg_user_link(self, link, tg_id):
        self.cursor.execute(query.UPDATE_USER_TL_USERS_LINK, (link, tg_id))
        self.connection.commit()

    def select_all_from_tl_users_by_link(self, link):
        self.cursor.execute(query.SELECT_BY_LINK_TG_USERS, (link,))
        row = self.cursor.fetchone()
        return row

    def insert_referral_table(self, owner, referral):
        self.cursor.execute(query.INSERT_REFERRAL_TABLE, (None, owner, referral))
        self.connection.commit()

    def update_tg_user_balance(self, tg_id):
        self.cursor.execute(query.UPDATE_USER_TL_USERS_BALANCE, (tg_id,))
        self.connection.commit()

    def select_tg_id_user_table(self, tg_id):
        self.cursor.execute(query.SELECT_TG_ID_USER_TABLE, (tg_id,))
        row = self.cursor.fetchone()
        return row

    def select_referrals_referral_table(self, tg_id):
        self.cursor.execute(query.SELECT_REFERRALS_REFERRAL_TABLE, (tg_id,))
        row = self.cursor.fetchall()
        return row

    def select_balance(self, tg):
        self.cursor.execute(query.SELECT_BALANCE_TL_USERS, (tg,))
        row = self.cursor.fetchone()
        return row

    def insert_scrap_table(self, link):
        self.cursor.execute(query.INSERT_SCRAP_TABLE, (None, link))
        self.connection.commit()