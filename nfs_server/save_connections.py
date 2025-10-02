# save_connections.py  (run as admin so binding to port 443 works)
import socket, threading, os, time
from datetime import datetime

HOST = '0.0.0.0'
PORTS = [443]   # listen on HTTPS port (add 80/8080 if you saw other ports)
OUTDIR = "captures"
os.makedirs(OUTDIR, exist_ok=True)

def dump(prefix, data):
    ts = datetime.utcnow().strftime("%Y%m%dT%H%M%S.%f")[:-3]
    fn = f"{prefix}_{ts}.bin"
    p = os.path.join(OUTDIR, fn)
    with open(p,"wb") as f:
        f.write(data)
    return p

def handle_client(conn, addr, port):
    try:
        conn.settimeout(3.0)
        data = b""
        while True:
            try:
                chunk = conn.recv(4096)
            except socket.timeout:
                break
            if not chunk:
                break
            data += chunk
            if len(data) > 2_000_000:
                break
    except Exception as e:
        print("recv err:", e)
    finally:
        if data:
            p = dump(f"p{port}_{addr[0].replace('.','_')}", data)
            print(f"[+] Saved {len(data)} bytes -> {p}")
        try:
            conn.sendall(b"OK")  # minimal reply so client doesn't hang
        except:
            pass
        try: conn.close()
        except: pass

def listener(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, port))
    s.listen(5)
    print(f"Listening on {HOST}:{port}")
    while True:
        conn, addr = s.accept()
        threading.Thread(target=handle_client, args=(conn, addr, port), daemon=True).start()

if __name__ == "__main__":
    import threading
    for p in PORTS:
        threading.Thread(target=listener, args=(p,), daemon=True).start()
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped")
