import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                break
            print(data.decode("utf-8"), end="")
    except (ConnectionError, OSError, UnicodeDecodeError):
        pass
    finally:
        print("\nDisconnected from server.")


def main():
    username = input("Choose a username: ").strip() or "Guest"

    try:
        with socket.create_connection((HOST, PORT)) as sock:
            threading.Thread(
                target=receive_messages,
                args=(sock,),
                daemon=True,
            ).start()

            print("Connected. Type messages below and press Enter.")
            while True:
                message = input()
                if message.lower() in {"exit", "quit"}:
                    break
                sock.sendall(f"{username}: {message}\n".encode("utf-8"))
    except KeyboardInterrupt:
        print("\nClosing chat.")
    except OSError as exc:
        print(f"Unable to connect to {HOST}:{PORT}: {exc}")


if __name__ == "__main__":
    main()
