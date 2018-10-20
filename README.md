# RemoteAdministrationTool
Simple Project to Remote Access antoher Server
A -> B

#Requirement
- Python 2 / Python 3
- Basic knowledge python (https://learnxinyminutes.com/docs/python/)

#How to use
0. Make Sure you have python installed. check with ($ python -v) *optional
1. Run RAT Server
	$ python server.py 
2. Run RAT Client
	$ python client.py
	
![alt text](http://i.imgur.com/ivSV5Et.png)

This Project :
- Learn about TCP protocol sending and recieve packet with encrypt and decrypt
- Create Simple RAT Client
- Create Simple RAT Server

Soon :
- Add authentication
- Add Feature to checking server health
- Add feature to get disk size information
- Add Feature auto deployment remotely with one action to multiple client

Plan A:
Server  -> Client A
	-> Client B
	-> Client C

can get report :
- Downtime
- Disk Space
- Processor & memory status

