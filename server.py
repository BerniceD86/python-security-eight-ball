# #def create_server():
#   print('Do your work here!')

# if __name__ == '__main__':
#   create_server() 
import socket
import _thread #import all functions from the thread library by their own name
import random 

host= '127.0.0.1'
port = 4445

def  clientthread(conn):
  conn.send(b'You have summoned the Security Eight Ball, what is your question?\n')

  responses = [b'ok...' , b'just do it', b'i guess', b'no']

  while True: 
    data = conn.recv(1024)
    reply = (responses[random.randint(0, len(responses)-1)] +b'\n')
    if not data: 
      break
    conn.sendall(reply)
  conn.close()

def create_server():
  print('hello world')
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  s.listen(5)

  while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    _thread.start_new_thread(clientthread, (c, ))
  s.close()

#if __name__ == '__main___':
create_server()