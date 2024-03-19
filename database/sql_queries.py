CREATE_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS telegram_users
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
USERNAME CHAR(50),
FIRST_NAME CHAR(50),
LAST_NAME CHAR(50),
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES(?,?,?,?,?)
"""

CREATE_BAN_USER_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS ban_user
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
BAN_COUNT INTEGER,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_user VALUES(?,?,?)
"""

SELECT_BAN_USER_QUERY = """
SELECT * FROM ban_user WHERE TELEGRAM_ID = ?
"""

UPDATE_BAN_COUNT_QUERY = """
UPDATE ban_user SET BAN_COUNT = BAN_COUNT + 1 WHERE TELEGRAM_ID = ?
"""

CREATE_PROFILE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS profile
(
ID INTEGER PRIMARY KEY,
TELEGRAM_ID INTEGER,
NICKNAME CHAR(50),
BIO TEXT,
AGE INTEGER,
MARRIED CHAR(10),
LOCATION CHAR(10),
HOBBY CHAR(40),
GENDER CHAR(40),
PHOTO TEXT,
UNIQUE (TELEGRAM_ID)
)
"""

INSERT_PROFILE_QUERY = """
INSERT INTO profile VALUES(?,?,?,?,?,?,?,?)
"""