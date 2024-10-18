# Written by siembra1978
import socket

REMOTE_SERVER = "www.google.com"


def is_connected(hostname):
    try:
        host = socket.gethostbyname(hostname)
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
    except:
        pass
    return False
