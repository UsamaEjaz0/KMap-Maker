from tkinter import *
import random
from tkinter import messagebox
root=Tk()
root.geometry("470x210")


string= 'E'

button=[]
canvas=[]

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[0].place(relx=0.082, rely=0.121, height=54, width=57)
canvas.append(Canvas(button[0]))

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[1].place(relx=0.206, rely=0.121, height=54, width=57)
canvas.append(Canvas(button[1]))

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[2].place(relx=0.329, rely=0.121, height=54, width=57)
canvas.append(Canvas(button[2]))

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[3].place(relx=0.454, rely=0.121, height=54, width=57)
canvas.append(Canvas(button[3]))

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[4].place(relx=0.082, rely=0.367, height=54, width=57)
canvas.append(Canvas(button[4]))


button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[5].place(relx=0.206, rely=0.367, height=54, width=57)
canvas.append(Canvas(button[5]))

button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[6].place(relx=0.329, rely=0.367, height=54, width=57)
canvas.append(Canvas(button[6]))


button.append(Button(root,text='',height=1,width=3,fg='red',font="Verdana 19 bold"))
button[7].place(relx=0.454, rely=0.367, height=54, width=57)
canvas.append(Canvas(button[7]))



exp=Label(root,text='expression(w,x,y):')
exp.place(relx=0.0, rely=0.756, height=31, width=144)

lol=Label(root,text='00             01              11             10')
lol.place(relx=0.05, rely=0.000, height=31, width=244)

w=Label(root,text='0')
w.place(relx=0.05, rely=0.140, height=31, width=7)

ww=Label(root,text='1')
ww.place(relx=0.05, rely=0.380, height=31, width=5)





e = Entry(root)
e.place(relx=0.277, rely=0.756,height=30, relwidth=0.307)


e.focus_set()
rows, cols = (2, 4) 
arr = [[0 for i in range(cols)] for j in range(rows)]
def printtext():
    global e
    global string
    global arr
    string = e.get() 
    print (string)

    list=string.split('+')
    print(list)
    # Using above first method to create a  
    # 2D array 
    
    
    for i in list:
        
        if i=="w'x'y'":
            canvas[0].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[0][0]=1
        if i=="w'x'y":
            canvas[1].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[0][1]=1
        if i=="w'xy":
            canvas[2].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[0][2]=1
        if i=="w'xy'":
            canvas[3].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[0][3]=1
        if i=="wx'y'":
            canvas[4].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[1][0]=1
        if i=="wx'y":
            canvas[5].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[1][1]=1
            
        if i=="wxy":
            canvas[6].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[1][2]=1
        if i=="wxy'":
            canvas[7].create_text(20, 30, anchor=W, font="Purisa",
            text="1")
            arr[1][3]=1
    groups();
    print(arr)
    for i in range(8):
        canvas[i].pack()
    
    
    
b = Button(root,text='Calculate',command=printtext)
b.place(relx=0.717, rely=0.311, height=44, width=77)
def groups():
    global arr
    if arr[0][0]==1 and arr[0][1]==1 and arr[0][2]==1 and arr[0][3]==1 and arr[1][0]==1 and arr[1][1]==1 and arr[1][2]==1 and arr[1][3]==1:
        canvas[0].create_line(0, 2, 80, 2)
        canvas[0].create_line(2, 2, 2, 80)
        canvas[1].create_line(0, 2, 80, 2)
        canvas[2].create_line(0, 2, 80, 2)
        canvas[3].create_line(0, 2, 80, 2)
        canvas[3].create_line(46, 0, 46, 80)
        canvas[4].create_line(0, 43, 92,43 )
        canvas[4].create_line(2, 2, 2, 80)
        
        canvas[6].create_line(0, 43, 92,43)
        canvas[5].create_line(0, 43, 92,43 )
        canvas[7].create_line(46, 0, 46, 80)
        canvas[7].create_line(0, 43, 92,43 )




        
        for i in range(8):
            canvas[i].pack()
    if arr[0][0]==1 and arr[0][1]==1 and arr[0][2]==1 and arr[0][3]==1:
        canvas[0].create_line(0, 2, 80, 2)
        canvas[0].create_line(2, 2, 2, 80)
        canvas[1].create_line(0, 2, 80, 2)
        canvas[2].create_line(0, 2, 80, 2)
        canvas[3].create_line(0, 2, 80, 2)
        canvas[3].create_line(46, 0, 46, 80)
        canvas[0].create_line(0, 43, 92,43 )
        canvas[1].create_line(0, 43, 92,43 )
        canvas[2].create_line(0, 43, 92,43 )
        canvas[3].create_line(0, 43, 92,43 )
    if arr[1][0]==1 and arr[1][1]==1 and arr[1][2]==1 and arr[1][3]==1:
        canvas[4].create_line(0, 2, 80, 2)
        canvas[4].create_line(2, 2, 2, 80)
        canvas[5].create_line(0, 2, 80, 2)
        canvas[6].create_line(0, 2, 80, 2)
        canvas[7].create_line(0, 2, 80, 2)
        canvas[7].create_line(46, 0, 46, 80)
        canvas[4].create_line(0, 43, 92,43 )
        canvas[5].create_line(0, 43, 92,43 )
        canvas[6].create_line(0, 43, 92,43 )
        canvas[7].create_line(0, 43, 92,43 )
    
    if arr[0][2]==1 and arr[0][3]==1 and arr[1][2]==1 and arr[1][3]==1:
        canvas[2].create_line(0, 2, 80, 2)
        canvas[2].create_line(2, 2, 2, 80)
        canvas[3].create_line(0, 2, 80, 2)
        canvas[3].create_line(46, 0, 46, 80)
        canvas[6].create_line(0, 43, 92,43 )
        canvas[6].create_line(2, 2, 2, 80)
        canvas[7].create_line(46, 0, 46, 80)
        canvas[7].create_line(0, 43, 92,43 )
        #canvas[0].create_line(46, 0, 46, 80)
        #canvas[0].create_line(0, 43, 92,43 )
        
        canvas[2].pack()
        canvas[3].pack()
        canvas[6].pack()
        canvas[7].pack()
        return 1;
        print('0')    
    
    elif arr[0][0]==1 and arr[0][1]==1 and arr[1][0]==1 and arr[1][1]==1:
        canvas[0].create_line(0, 2, 80, 2)
        canvas[0].create_line(2, 2, 2, 80)
        canvas[1].create_line(0, 2, 80, 2)
        canvas[1].create_line(46, 0, 46, 80)
        canvas[4].create_line(0, 43, 92,43 )
        canvas[4].create_line(2, 2, 2, 80)
        canvas[5].create_line(46, 0, 46, 80)
        canvas[5].create_line(0, 43, 92,43 )
        #canvas[0].create_line(46, 0, 46, 80)
        #canvas[0].create_line(0, 43, 92,43 )
        
        canvas[0].pack()
        canvas[1].pack()
        canvas[4].pack()
        canvas[5].pack()
        return 1;
        print('0')
    
        
    elif arr[0][0]==1 and arr[0][1]==1 :
        canvas[0].create_line(0, 2, 80, 2)
        canvas[0].create_line(0, 43, 92,43 )
        canvas[0].create_line(2, 2, 2, 80)
        canvas[1].create_line(0, 2, 80, 2)
        canvas[1].create_line(46, 0, 46, 80)
        canvas[1].create_line(0, 43, 92,43 )
        #canvas[1].create_line(2, 2, 2, 80)
        canvas[0].pack()
        canvas[1].pack()
        if arr[1][1]==1:
            canvas[1].create_line(2, 2, 2, 80)
            canvas[5].create_line(46, 0, 46, 80)
            canvas[5].create_line(0, 43, 92,43 )
            canvas[5].create_line(2, 2, 2, 80)
            canvas[1].pack()
            canvas[5].pack()
        if arr[1][0]==1:
            canvas[0].create_line(46, 0, 46, 80)
            canvas[4].create_line(46, 0, 46, 80)
            canvas[4].create_line(0, 43, 92,43 )
            canvas[4].create_line(2, 2, 2, 80)
            canvas[4].pack()
            canvas[0].pack()
            
            
        print('1')
    elif arr[1][0]==1 and arr[1][1]==1 :
        canvas[4].create_line(0, 2, 80, 2)
        canvas[4].create_line(0, 43, 92,43 )
        canvas[4].create_line(2, 2, 2, 80)

        canvas[5].create_line(0, 2, 80, 2)
        canvas[5].create_line(46, 0, 46, 80)
        canvas[5].create_line(0, 43, 92,43 )
        canvas[4].pack()
        canvas[5].pack()

        if arr[0][0]==1:
            canvas[4].create_line(46, 0, 46, 80)
            canvas[0].create_line(0, 2, 80, 2)
            canvas[0].create_line(46, 0, 46, 80)
            canvas[0].create_line(2, 2, 2, 80)
            canvas[0].pack()
            canvas[4].pack()
        if arr[0][1]==1:
            canvas[5].create_line(2, 2, 2, 80)
            canvas[1].create_line(0, 2, 80, 2)
            canvas[1].create_line(46, 0, 46, 80)
        
            canvas[1].create_line(2, 2, 2, 80)
            canvas[1].pack()
            canvas[5].pack()
            
            
        
        
    elif arr[0][0]==1 and arr[1][0]==1:
        canvas[0].create_line(0, 2, 80, 2)
        canvas[0].create_line(46, 0, 46, 80)
        canvas[0].create_line(2, 2, 2, 80)

        
        canvas[4].create_line(46, 0, 46, 80)
        canvas[4].create_line(0, 43, 92,43 )
        canvas[4].create_line(2, 2, 2, 80)
        
        canvas[0].pack()
        canvas[4].pack()
        if arr[0][1]==1:
            canvas[0].create_line(46, 0, 46, 80)
            canvas[1].create_line(0, 2, 80, 2)
            canvas[1].create_line(46, 0, 46, 80)
            canvas[1].create_line(0, 43, 92,43 )
            canvas[1].pack()
            canvas[0].pack()
        if arr[1][1]==1:
            canvas[4].create_line(46, 0, 46, 80)
            canvas[5].create_line(0, 2, 80, 2)
            canvas[5].create_line(46, 0, 46, 80)
            canvas[5].create_line(0, 43, 92,43 )
            canvas[5].pack()
            canvas[4].pack()
    elif arr[0][1]==1 and arr[1][1]==1:
        canvas[1].create_line(0, 2, 80, 2)
        canvas[1].create_line(46, 0, 46, 80)
        canvas[1].create_line(2, 2, 2, 80)
        canvas[5].create_line(46, 0, 46, 80)
        canvas[5].create_line(0, 43, 92,43 )
        canvas[5].create_line(2, 2, 2, 80)
        canvas[1].pack()
        canvas[5].pack()
        print('2')
    
    
        
    #if arr[1][1]==1:
        #canvas[3].create_line(0, 2, 80, 2)
        #canvas[3].create_line(46, 0, 46, 80)
        #canvas[3].create_line(0, 43, 92,43 )
        #canvas[3].create_line(2, 2, 2, 80)
        #canvas[3].pack()
        #print('3')
   

def clear():
    global arr
    arr = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(8):
        canvas[i].delete('all')
        
    
   
    pass
    
a = Button(root,text='Clear',command=clear)
a.place(relx=0.717, rely=0.551, height=44, width=77)


root.mainloop()
