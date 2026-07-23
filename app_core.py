# Added a header comment (Test A: fingerprint-stability, no code change)
# second comment line
import os
import sqlite3


def get_user(request, db):
    # BASELINE VULN #1 — SQL injection (untrusted input concatenated into query)
    user_id = request.args.get("id")
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    return db.execute(query).fetchall()


def ping_host(request):
    # BASELINE VULN #2 — OS command injection (untrusted input to os.system)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
