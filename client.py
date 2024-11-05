import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    print("..................")
    msg=str(input("le client:   "))
    print("..................")
    if msg == "exit":
        print("by by")
        break
    sdata=msg.encode("UTF-8")
    s.sendto(sdata,("127.0.0.1",50000))
    print("...le client response...!")
    print("...................")
    rdata,address=s.recvfrom(1024)
    data=rdata.decode("UTF-8")
    print("le serveur : " ,data )
s.close()
   
