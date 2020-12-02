import socket

host = input('rhost: ')
try:
    for port in range(1,1000):
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((host,port))
        if result == 0: 
            def non():
                print('------------------')
            print("port {} is open. ".format(port))
            non()
except:
    print("erorr")

    #اداه فحص اذا البورت مفتوح او لا 