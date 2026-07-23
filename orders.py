import sqlite3


def get_order(request, db):
    oid = request.args.get("oid")
    query = "SELECT * FROM orders WHERE id = '%s'" % oid
    return db.execute(query).fetchall()
