# tcp-chat-python

A simple Python TCP chat application with a server and client.

## Features
- Multi-client chat room
- Messages broadcast to all connected clients
- Lightweight implementation using Python's built-in `socket` and `threading` modules

## Project structure

```text
.
├── README.md
├── server.py
├── client.py
└── .gitignore
```

## How to run

Start the server in one terminal:

```bash
python3 server.py
```

Then start one or more clients in separate terminals:

```bash
python3 client.py
```

When prompted, enter a username. Then type messages and press Enter to broadcast them to everyone in the room.

## Notes
- The default configuration runs on `127.0.0.1:5000`, which means only local clients on the same machine can connect.
- To allow connections from other machines on the same network, change the server host to `0.0.0.0` and point clients to the server machine's IP address.
