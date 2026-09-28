# Python Practice 80: Socket Networking
import socket
import threading

# 1. Hostname
hostname = socket.gethostname()
print("1. Hostname:", hostname)

# 2. Resolve local hostname
try:
    print("2. IP:", socket.gethostbyname(hostname))
except socket.gaierror:
    print("2. IP unavailable")

# 3. Parse IPv4
address = "192.168.1.10"
print("3. Parts:", address.split("."))

# 4. Validate IPv4
def is_valid_ipv4(value):
    parts = value.split(".")
    return len(parts) == 4 and all(
        p.isdigit() and 0 <= int(p) <= 255 for p in parts
    )

print("4.", is_valid_ipv4("192.168.1.10"), is_valid_ipv4("999.1.1.1"))

# 5. Address information
try:
    info = socket.getaddrinfo("localhost", 80)
    print("5. Records:", len(info))
except socket.gaierror:
    print("5. Resolution failed")

# 6. TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("6. TCP:", sock.family, sock.type)
sock.close()

# 7. UDP socket
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("7. UDP:", udp.family, udp.type)
udp.close()

# 8. Local TCP echo server/client
result = {}

def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        s.listen(1)
        result["port"] = s.getsockname()[1]
        conn, _ = s.accept()
        with conn:
            data = conn.recv(1024)
            conn.sendall(data.upper())

thread = threading.Thread(target=server)
thread.start()
while "port" not in result:
    pass

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect(("127.0.0.1", result["port"]))
    client.sendall(b"hello socket")
    response = client.recv(1024)

thread.join()
print("8. Response:", response.decode())

# 9. Local UDP echo
result = {}

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind(("127.0.0.1", 0))
        result["port"] = s.getsockname()[1]
        data, addr = s.recvfrom(1024)
        s.sendto(data.upper(), addr)

thread = threading.Thread(target=udp_server)
thread.start()
while "port" not in result:
    pass

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.sendto(b"hello udp", ("127.0.0.1", result["port"]))
    data, _ = client.recvfrom(1024)

thread.join()
print("9. UDP response:", data.decode())

# 10. Socket timeout
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.settimeout(0.5)
    print("10. Timeout:", s.gettimeout())

# 11. Reusable echo-server function
def run_echo_server(host="127.0.0.1", port=5000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen(5)
        print(f"11. Echo server ready: {host}:{port}")

# run_echo_server()  # Uncomment for a real local server.
