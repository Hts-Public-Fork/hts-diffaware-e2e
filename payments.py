import sqlite3


def get_payment(request, db):
    pid = request.args.get("pid")
    query = "SELECT * FROM payments WHERE id = '%s'" % pid
    return db.execute(query).fetchall()
