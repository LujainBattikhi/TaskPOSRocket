
#recursion function for calculating summation of each element
def Fac(number):
    if number == 1:
        return 1
    else :
        return number+Fac(number-1)


inputList =[5 , 3 , 6 , 1]
outputList=[]

for element in inputList:
    outputList.append(Fac(element))


print(outputList)