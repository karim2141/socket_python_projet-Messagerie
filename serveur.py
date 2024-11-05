import socket 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("127.0.0.1",50000))
while True :
    rdata,address=s.recvfrom(1024)
    data=rdata.decode("UTF-8")
    print ("le client :",data)
    print(".....................")
    msg=str(input("le serveur:   "))
    print(".....................")
    sdata=msg.encode("UTF-8")
    s.sendto(sdata,address)
    print("...le serveur response...!")
    print(".......................")
