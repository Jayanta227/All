import multiprocessing
import time
print("hello")
def square(number):
    for x in number:
        print("square "+str(x*x))
        time.sleep(.1)
def cube(number):
    for x in number:
        print("cube", x*x*x)
        time.sleep(.1)
arr=[1,2,3,4,5]
if __name__=="__main__":
    t1=multiprocessing.Process(target=square,args=(arr,))
    t2=multiprocessing.Process(target=cube,args=(arr,))         
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done")
