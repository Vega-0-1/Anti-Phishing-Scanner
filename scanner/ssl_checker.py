import ssl
import socket
from utils.logger import log_message

def check_ssl(url):
    try:
        hostname = url.replace("https://", "").replace("http://", "").split("/")[0]
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as secure_sock:
                cert = secure_sock.getpeercert()
        log_message("info", f"SSL Certificate for {hostname} is valid")
        return True
    except Exception:
        log_message("error", f"No valid SSL certificate found for {hostname}")
        return False
