import os
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second
a=2
f = open('myfile221.txt', 'w')
##    print("opem")
##    text= open("read.txt","r")
##    a=text.read(1)
print("opem")
#text= open("readyy.txt","a")

def main():
    global a
    c="hih"+str(a*100)
    
    f.write(c+"\n")  # python will convert \n to os.linesep
    a=a*2

   

while 1:   
    main()
f.close()
