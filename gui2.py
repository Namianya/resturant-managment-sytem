"""
returant management system
@PaulWekesa

"""


from tkinter import *
import time
from random import randint




def btnClick(numbers):
   global operator
   operator = operator + str(numbers)
   textInput.set(operator)

def btnClear():
    global operator
    operator=""
    textInput.set("")


    
def equal():
    global operator
    total=str(eval(operator))
    textInput.set(total)
    operator=""
    


    
    
def btnClearRes():
    tfries.set("")
    tjuice.set("")
    tsausage.set("")
    recipt.set("")
    afries.set("")
    ajuice.set("")
    asausage.set("")
    total.set("")
       
def Exit():
   res.destroy()







#====================================================================variables=================================================================



res=Tk()
res.title("restaurant")
res.geometry("1600x900")

#------------------------------------------------------------------------------------------------------------------------------------------------


operator=""
textInput = StringVar()
recipt=StringVar()
total=StringVar()
tfries=IntVar()
tjuice=IntVar()
tsausage=IntVar()
afries=StringVar()
ajuice=StringVar()
asausage=StringVar()

def reciptNo():
    global number
    number=randint(100000,999999)
    recipt.set(number)

def GrandTotal():

    
    CoF=float(afries.get())
    CoJ=float(ajuice.get())
    CoS=float(asausage.get())
    

    costfries = CoF * 100
    costjuice = CoJ * 40
    costsausage = CoS * 20


    tfries.set(costfries)
    tjuice.set(costjuice)
    tsausage.set(costsausage)

  
    purchasecost=(costfries+costjuice+costsausage)

    total.set(purchasecost)

    

    

    

    


#-----------------------------------------------------------------------time-----------------------------------------------------------------------------------------

localtime=time.asctime(time.localtime(time.time()))

#----------------------------------------------------------------------frames-----------------------------------------------------------------------------------------
window3= Frame(res,width=1600, height=200)
window3.pack(side=TOP)

window= Frame(res,width=500, height=700)
window.pack(side=RIGHT)

window2= Frame(res,width=800, height=700)
window2.pack(side=LEFT)

#=======================================================================title=========================================================================================

ttle=Label(window3, text="PAUL`S ",fg="black",font=("forte",35,"italic"))
ttle.grid()

tym=Label(window3, text=localtime,fg="black" ,font=("calibri",20,"italic"))
tym.grid(column=0, row=1)
#======================================================================entry box========================================================================================
eb=Entry(window,textvariable = textInput,bg="powder blue",width=60,
         bd=20,justify="right" )
eb.grid(columnspan=4)


#===================================================================buttons===============================================================================================

b9=Button(window, padx=20, pady=20, text="9",bd=20,font=(50),command=lambda:btnClick(9))
b9.grid(column=0, row=1)

b8=Button(window,padx=20, pady=20,text="8",bd=20,font=(50), command=lambda:btnClick(8))
b8.grid(column=1, row=1)

b7=Button(window,padx=20, pady=20,text="7",bd=20,font=(50),command=lambda:btnClick(7))
b7.grid(column=2, row=1)

b6=Button(window,padx=20, pady=20,text="6",bd=20,font=(50),command=lambda:btnClick(6))
b6.grid(column=0, row=2)

b5=Button(window,padx=20, pady=20,text="5",bd=20,font=(50),command=lambda:btnClick(5))
b5.grid(column=1, row=2)

b4=Button(window,padx=20, pady=20,text="4",bd=20,font=(50),command=lambda:btnClick(4))
b4.grid(column=2, row=2)

b3=Button(window,padx=20, pady=20,text="3",bd=20,font=(50),command=lambda:btnClick(3))
b3.grid(column=0, row=3)

b2=Button(window,padx=20, pady=20,text="2",bd=20,font=(50),command=lambda:btnClick(2))
b2.grid(column=1, row=3)

b1=Button(window,padx=20, pady=20,text="1",bd=20,font=(50),command=lambda:btnClick(1))
b1.grid(column=2, row=3)

b0=Button(window,padx=20, pady=20,text="0",bd=20,font=(50),command=lambda:btnClick(0))
b0.grid(column=1, row=4)

ba=Button(window,padx=20, pady=20,text="+",bd=20,font=(50),command=lambda:btnClick("+"))
ba.grid(column=3, row=1)

bs=Button(window,padx=20, pady=20,text="-",bd=20,font=(50),command=lambda:btnClick("-"))
bs.grid(column=3, row=2)

b1=Button(window,padx=20, pady=20,text="/",bd=20,font=(50),command=lambda:btnClick("/"))
b1.grid(column=3, row=3)

bc=Button(window,padx=20, pady=20,text="cc",bd=20,font=(50),command=lambda:btnClear())
bc.grid(column=2, row=4)

bp=Button(window,padx=20, pady=20,text=".",bd=20,font=(50),command=lambda:btnClick("."))
bp.grid(column=0, row=4)

be=Button(window,padx=20, pady=20,text="=",bd=20,font=(50),command=lambda:equal())
be.grid(column=3, row=4)
#=======================================================================res. section=====================================================

l1=Label(window2, text="Recipt No.", font=(50))
l1.grid()
rn=Entry(window2,textvariable = recipt,bd=20,justify="right",width=60)
rn.grid(column=1,columnspan=2,row=0)


l2=Label(window2, text="Fries", font=(50))
l2.grid(column=0,row=1)
fries=Entry(window2,width=60,textvariable=afries, bd=20,justify="right",)
fries.grid(column=1,columnspan=2,row=1)


#---------------------------------------------------------------------------totals---------------------------------------------------

total1=Label(window2, text="Total", font=(50))
total1.grid(column=3,row=1)
total1=Entry(window2,bd=20,textvariable =tfries ,justify="right",width=40)
total1.config(state="disabled")
total1.grid(column=4,row=1)


total2=Label(window2, text="Total", font=(50))
total2.grid(column=3,row=2)
total2=Entry(window2,width=40,bd=20,textvariable = tjuice,justify="right",)
total2.config(state="disabled")
total2.grid(column=4,row=2)


total3=Label(window2, text="Total", font=(50))
total3.grid(column=3,row=3)
total3=Entry(window2,width=40,bd=20,textvariable = tsausage ,justify="right",)
total3.config(state="disabled")
total3.grid(column=4,row=3)



total4=Label(window2, text="Grand Total", font=(50))
total4.grid(column=0,row=4)
totals=Entry(window2,width=40,bd=20,textvariable = total )

totals.config(state="disabled")
totals.grid(column=1,columnspan=2,row=4)

#-----------------------------------------------------------------------------------------------------------------------------------


lsausage=Label(window2, text="Sausage", font=(50))
lsausage.grid(column=0,row=2)
sausage=Entry(window2,bd=20,textvariable=asausage,justify="right",width=60)
sausage.grid(column=1,columnspan=2,row=2)


ljuice=Label(window2, text="Juice", font=(50))
ljuice.grid(column=0,row=3)
juice=Entry(window2,width=60,textvariable=ajuice,bd=20,justify="right",)
juice.grid(column=1,columnspan=2,row=3)



reciptb=Button(window2,padx=30, pady=10,text="PRINT",bd=20,font=(50),command=lambda:reciptNo())
reciptb.grid(column=0, row=5)

bclear=Button(window2,padx=30, pady=10,text="CLEAR",bd=20,font=(50),command=btnClearRes)
bclear.grid(column=1, row=5)

btotals=Button(window2,padx=30, pady=10,text="EXIT",bd=20,font=(50),command=lambda:Exit())
btotals.grid(column=4, row=5)


btotals=Button(window2,padx=30, pady=10,text="TOTAL",bd=20,font=(50),command=GrandTotal)
btotals.grid(column=2, row=5)


res.mainloop()

                
