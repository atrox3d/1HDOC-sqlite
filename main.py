import sqlite3
import logging
import util.logging
logger = logging.getLogger(__name__)
util.logging.get_root_logger()

db = sqlite3.connect('books-collection.db')
cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS books (" \
      "id INTEGER PRIMARY KEY," \
      "title VARCHAR(250) NOT NULL UNIQUE," \
      "author VARCHAR(250) NOT NULL," \
      "rating FLOAT NOT NULL" \
      ")"
logger.info(sql)
cursor.execute(sql)
try:
    sql = "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')"
    logger.info(sql)
    cursor.execute(sql)
    db.commit()
except Exception as e:
    logger.error(e.__class__.__name__)
    logger.error(e)
