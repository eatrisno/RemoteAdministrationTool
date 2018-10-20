import socket
import os
import time

port = 52918

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('0.0.0.0', port))
conn.listen(1)
while 1:
	try:
		os.system("clear")
		print('[*] Listening for upcoming connections...')

		client_conn , info = conn.accept()
		print('[+] New client found from ip ' + str(info[0]) + ' !')
		
		try:
			msg = b''
			while msg != 'end':
				try:
					msg = raw_input(str(info[0]) + ' > ')
					if(msg == b''):
						pass
					else:
						msg = msg.encode()
						client_conn.send(msg)
						recv = client_conn.recv(1024*3)
						recv = recv.decode()
						print(recv)
				except BrokenPipeError:
					print('[-] Client disconnected...')
					break
		except KeyboardInterrupt:
			print('\n[-] Session Closed')
			msg = 'end'
			msg = msg.encode()
			client_conn.send(msg)
			client_conn.close()
			time.sleep(2)
	except KeyboardInterrupt:
		print('\n[-] Shutting down the server...')
		break
