import os


def ping_host(request):
    # OS command injection kept; this PR removes the SQL injection (get_user)
    host = request.args.get("host")
    os.system("ping -c 1 " + host)
