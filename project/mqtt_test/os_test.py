import os
import threading
def t1():
	os.system("python3 test1.py")
def t2():
        os.system("python3 test2.py")
def t0():
        os.system("python3 test.py")
def main():
    thread1 = threading.Thread(target=t0, name='T0')
    thread1.start()

    thread2 = threading.Thread(target=t1, name='T1')
    thread2.start()

    thread3 = threading.Thread(target=t2, name='T2')
    thread3.start()

if __name__=='__main__':
    main()

