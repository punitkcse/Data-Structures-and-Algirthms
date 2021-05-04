def shiftAndUpdate(arra,num,index):
    for i in range(index+1):
        if(i==index):
            arra[i]=num
        else:
            arra[i]=arra[i+1]
def updateLargest(threeLargest,num):
    if(threeLargest[2] is None or num > threeLargest[2]):
        shiftAndUpdate(threeLargest,num,2)
    elif(threeLargest[1] is None or num > threeLargest[1]):
        shiftAndUpdate(threeLargest,num,1)
    elif(threeLargest[0] is None or num > threeLargest[0]):
        shiftAndUpdate(threeLargest,num,0)

def findThreeLargestNumbers(array):
    threeLargest = [None,None,None]
    for num in array:
        updateLargest(threeLargest,num)
    print(threeLargest)
    return threeLargest


array = [100,20,-5,6,5,8]
print(findThreeLargestNumbers(array))
