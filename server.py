import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

clients = set()
clients_lock = threading.Lock()


def broadcast(message):
    """Send a message to every connected client."""
    payload = message.encode("utf-8")
    with clients_lock:
        active_clients = list(clients)

    for client in active_clients:
        try:
            client.sendall(payload)
        except OSError:
            with clients_lock:
                clients.discard(client)
            client.close()


def handle_client(conn, address):
    print(f"Connected: {address}")

    try:
        while True:
            data = conn.recv(4096)
            if not data:
                break

            message = data.decode("utf-8").strip()
            if message:
                print(f"{address}: {message}")
                broadcast(f"{address}: {message}\n")
    except (ConnectionError, OSError, UnicodeDecodeError):
        pass
    finally:
        with clients_lock:
            clients.discard(conn)
        conn.close()
        print(f"Disconnected: {address}")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Chat server listening on {HOST}:{PORT}")

        while True:
            conn, address = server.accept()
            with clients_lock:
                clients.add(conn)
            threading.Thread(
                target=handle_client,
                args=(conn, address),
                daemon=True,
            ).start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nServer stopped.")
