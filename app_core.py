import sqlite3


def get_user(request, db):
    # SQL injection kept as-is (this PR only fixes the command injection)
    user_id = request.args.get("id")
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    return db.execute(query).fetchall()
