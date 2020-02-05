import asyncio
import time
import os

#Due to sorting is using memory of RAM, the speed of sorting is the same.
#I just asynchronize the process of I/O. Also, accelerating the speed of IO is
#the main function that asyncaio can help with, according to the lectures'
#context. Compare to the not async version, the version with async is slower
#because the data are so a few that, the time for I/O is very short.
#Moreover, the time that using function of async has been added up, So
#the version without async is faster than async. 

async def do_some_work(x,y):
    with open(y,"r") as f:
                x=f.read().splitlines()
    x=[int(j) for j in x]
    x.sort()
    f.close()
    return x

def main():
    if not os.path.exists('output'):
            os.mkdir('output')
    data1=[]
    data2=[]
    data3=[]
    data4=[]
    data5=[]
    data6=[]
    data7=[]
    data8=[]
    data9=[]
    data10=[]
                



    coroutine1 = do_some_work(data1,"input/unsorted_1.txt")
    coroutine2 = do_some_work(data2,"input/unsorted_2.txt")
    coroutine3 = do_some_work(data3,"input/unsorted_3.txt")
    coroutine4 = do_some_work(data4,"input/unsorted_4.txt")
    coroutine5 = do_some_work(data5,"input/unsorted_5.txt")
    coroutine6 = do_some_work(data6,"input/unsorted_6.txt")
    coroutine7 = do_some_work(data7,"input/unsorted_7.txt")
    coroutine8 = do_some_work(data8,"input/unsorted_8.txt")
    coroutine9 = do_some_work(data9,"input/unsorted_9.txt")
    coroutine10 = do_some_work(data10,"input/unsorted_10.txt")


    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
        asyncio.ensure_future(coroutine4),
        asyncio.ensure_future(coroutine5),
        asyncio.ensure_future(coroutine6),
        asyncio.ensure_future(coroutine7),
        asyncio.ensure_future(coroutine8),
        asyncio.ensure_future(coroutine9),
        asyncio.ensure_future(coroutine10)
    ]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    i=0
    for task in tasks:
        if(i==0):
            data1=task.result()
            i+=1
            continue
        elif(i==1):
            data2=task.result()
            i+=1
            continue
        elif(i==2):
            data3=task.result()
            i+=1
            continue
        elif(i==3):
            data4=task.result()
            i+=1
            continue
        elif(i==4):
            data5=task.result()
            i+=1
            continue
        elif(i==5):
            data6=task.result()
            i+=1
            continue
        elif(i==6):
            data7=task.result()
            i+=1
            continue
        elif(i==7):
            data8=task.result()
            i+=1
            continue
        elif(i==8):
            data9=task.result()
            i+=1
            continue
        else:
            data10=task.result()


#Above are asynchonizing the process of input data from files


        unsorted=[None]*10
        result=[]

        append_unsorted(unsorted,0,data1)
        append_unsorted(unsorted,1,data2)
        append_unsorted(unsorted,2,data3)
        append_unsorted(unsorted,3,data4)
        append_unsorted(unsorted,4,data5)
        append_unsorted(unsorted,5,data6)
        append_unsorted(unsorted,6,data7)
        append_unsorted(unsorted,7,data8)
        append_unsorted(unsorted,8,data9)
        append_unsorted(unsorted,9,data10)

        sort(unsorted, result,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10)

        

#initialize the unsorted

def sort(unsorted, result,data1,data2,data3,data4,data5,data6,data7,data8,data9,data10):
        w=0
        while(len(result)<1000):
                if(len(result)==100):
                        if(w==0):
                                write(result,'w')
                                result=[]
                                w+=1
                        else:
                                write(result,'a')
                                result=[]
                                w+=1
                if(w==10):
                        break
                result.append(unsorted[get_minindex(unsorted)])
                if(get_minindex(unsorted)==0):
                        append_unsorted(unsorted,get_minindex(unsorted),data1)
                elif(get_minindex(unsorted)==1):
                        append_unsorted(unsorted,get_minindex(unsorted),data2)
                elif(get_minindex(unsorted)==2):
                        append_unsorted(unsorted,get_minindex(unsorted),data3)
                elif(get_minindex(unsorted)==3):
                        append_unsorted(unsorted,get_minindex(unsorted),data4)
                elif(get_minindex(unsorted)==4):
                        append_unsorted(unsorted,get_minindex(unsorted),data5)
                elif(get_minindex(unsorted)==5):
                        append_unsorted(unsorted,get_minindex(unsorted),data6)
                elif(get_minindex(unsorted)==6):
                        append_unsorted(unsorted,get_minindex(unsorted),data7)
                elif(get_minindex(unsorted)==7):
                        append_unsorted(unsorted,get_minindex(unsorted),data8)
                elif(get_minindex(unsorted)==8):
                        append_unsorted(unsorted,get_minindex(unsorted),data9)
                else:
                        append_unsorted(unsorted,get_minindex(unsorted),data10)
                

def write(result,m):
        with open('output/async_sorted.txt',m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)

def append_unsorted(unsorted,index,data):
        if(len(data)==1):
                unsorted[index]=data[0]
                data[0]=-1
        else:
                unsorted[index]=data[0]
                del data[0]


def get_minindex(unsorted):
        min=-100000
        index_min=-1
        for j in range(0,10):
                if unsorted[j]!=-1:
                        index_min=j
                        min=unsorted[j]
        for i in range(0,10):
                if min> unsorted[i] and unsorted[i]!=-1:
                        min=unsorted[i]
                        index_min=i
                else:
                        continue
        return index_min


        
if __name__ == '__main__':
	main()


