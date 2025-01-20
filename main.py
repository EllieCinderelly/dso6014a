import paramiko

"""
Windows-side scipt for SSHing into an rpi, controlling pins, test equipment, etc...

"""

host = ""
username = ""
password = ""

def run_main():
    return input('Enter something to send:')

def send(arg):
    print(host,username)
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=username, password=password)
    _stdin, _stdout,_stderr = client.exec_command("sudo python /home/ellie/code/dso6014a/dso6014a.py %s" % (arg))
    print(_stdout.read().decode())
    client.close()

def init_ssh():
    global host
    global username
    file = open('ssh-info.txt','r')
    info = file.readlines()
    ip = str(info[0])
    name = str(info[1])
    host = ip.strip()
    username = name.strip()

if __name__ == '__main__':
    try:
        init_ssh()
    except:
        print('Please create ssh-info.txt in main.py directory and add SSH host IP on the first line\n and the ssh username on the second line.\n')
    else:
        while(1):
            to_send = run_main()
            if(to_send == 'exit'): 
                break
            else:
                send(to_send)