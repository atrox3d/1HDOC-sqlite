SQLLITE3 = False

if SQLLITE3:
    import sqlite3
    import logging
    import util.logging
    from util.logging import log_decorator

    logger = logging.getLogger(__name__)
    util.logging.get_root_logger()

    sqlite3.connect = log_decorator(sqlite3.connect)

    db = sqlite3.connect('books-collection.db')
    cursor = db.cursor()

    execute = log_decorator(cursor.execute)
    sql = "CREATE TABLE IF NOT EXISTS books (" \
          "id INTEGER PRIMARY KEY," \
          "title VARCHAR(250) NOT NULL UNIQUE," \
          "author VARCHAR(250) NOT NULL," \
          "rating FLOAT NOT NULL" \
          ")"
    logger.info(sql)
    execute(sql)
    try:
        sql = "INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')"
        logger.info(sql)
        execute(sql)
        db.commit()
    except Exception as e:
        logger.error(e.__class__.__name__)
        logger.error(e)

else:
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy

    import logging
    import util.logging
    from util.logging import log_decorator

    logger = logging.getLogger(__name__)
    util.logging.get_root_logger()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)


    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(250), nullable=False, unique=True)
        author = db.Column(db.String(250), nullable=False)
        rating = db.Column(db.Float, nullable=False)

        def __repr__(self):
            return f'<Book {self.title}'


    db.create_all()
