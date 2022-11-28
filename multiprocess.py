import random
import time
from multiprocessing import *

###### start #########
def sayRandom(name):
    myid = current_process().pid
    while True:
        subject =random.choice(['We','They','I','You'])
        verb = random.choice(['like','hate','need','buy','sale'])
        objects = random.choice(['apple','book','milk','candy','house'])
        print(f'Process {name} : {myid} says: {subject} {verb} {objects} ') 
        time.sleep(random.randint(1,2))  


if __name__ == '__main__':
    childProcess1 = Process(target=sayRandom,args=('Bob',))
    childProcess1.start()
    
    print("I am here")

###### end ############
