import os
def main():
        if not os.path.exists('output'):
            os.mkdir('output')
        with open("input/unsorted_1.txt","r") as f1:
                data1=f1.read().splitlines()
        with open("input/unsorted_2.txt","r") as f2:
                data2=f2.read().splitlines()
        with open("input/unsorted_3.txt","r") as f3:
                data3=f3.read().splitlines()
        with open("input/unsorted_4.txt","r") as f4:
                data4=f4.read().splitlines()
        with open("input/unsorted_5.txt","r") as f5:
                data5=f5.read().splitlines()
        with open("input/unsorted_6.txt","r") as f6:
                data6=f6.read().splitlines()
        with open("input/unsorted_7.txt","r") as f7:
                data7=f7.read().splitlines()
        with open("input/unsorted_8.txt","r") as f8:
                data8=f8.read().splitlines()
        with open("input/unsorted_9.txt","r") as f9:
                data9=f9.read().splitlines()
        with open("input/unsorted_10.txt","r") as f10:
                data10=f10.read().splitlines()


        data1=[int(x) for x in data1]
        data2=[int(x) for x in data2]
        data3=[int(x) for x in data3]
        data4=[int(x) for x in data4]
        data5=[int(x) for x in data5]
        data6=[int(x) for x in data6]
        data7=[int(x) for x in data7]
        data8=[int(x) for x in data8]
        data9=[int(x) for x in data9]
        data10=[int(x) for x in data10]

        
        data1.sort()
        data2.sort()
        data3.sort()
        data4.sort()
        data5.sort()
        data6.sort()
        data7.sort()
        data8.sort()
        data9.sort()
        data10.sort()



#get first 1 nums from 10 sorted files those are the samllest number from
#each file. We put these 10 numbers into a list unsorted[]
#then we find the smallest number from the list unsorted[] and 
#output the samllest one to a result[] list
# when reult[] list get 100 numbers, we output those 100 smallest numbr to the
#file and clean the result[] list, and keep doing previous steps, until we sort
#1000 nums. When the list from file is empty, we will mark -1 to mark as empty
#, then for the next time the unsorted[] travel this -1, it will skip to next
#index.

        #print (data1)
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
        with open('output/sorted.txt',m)as ff:
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


def msort(data1,data2):
        if len(data1)==0:
                return data2
        elif len(data2)==0:
                return data1
        elif data1[0]<data2[0]:
                return [data1[0]]+sort(data1[1:],data2)
        else:
                return [data2[0]]+sort(data2[1:],data1)


        
if __name__ == '__main__':
	main()
