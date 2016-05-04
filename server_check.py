import time, socket, os

while True:
	time.sleep(3600)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(("127.0.0.1", 745))
        s.shutdown(2)
        print "connection succeeded"
    except:
    	print "connection failed"
        os.system("reboot")
