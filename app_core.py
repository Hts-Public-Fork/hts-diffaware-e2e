import os


def ping_host(request):
    # OS command injection kept; this PR removes the SQL injection (get_user)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
tion (untrusted input concatenated into query)
    user_id = request.args.get("id")
    query = "SELECT * FROM users WHERE id = '%s'" % user_id
    return db.execute(query).fetchall()


def ping_host(request):
    # BASELINE VULN #2 — OS command injection (untrusted input to os.system)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)

# isolated re-scan comment (Test A)

# concurrency-test bump

# concurrency-test bump
