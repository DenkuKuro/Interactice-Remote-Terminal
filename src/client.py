import socket
import subprocess
import os
from dotenv import load_dotenv

load_dotenv()

s = socket.socket()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))

s.connect((host, port))
print("Enter commands: ", end="")
while True:
    # data = s.recv(1024)
    cmd = input()
    # if data[:2].decode("utf-8") == "cd":
    #     os.chdir(data[3:].decode("utf-8"))
    if len(str.encode(cmd)) > 0:
        s.send(str.encode(cmd))
        if (cmd == "quit"):
            break
        server_res = str(s.recv(1024), "utf-8")
        print(server_res, end="")