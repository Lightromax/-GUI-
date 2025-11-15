from tkinter import *
from tkinter.ttk import *

root=Tk()
root.title("Pizza App")
root.geometry("550x220")

def order():
    sizes=pizz.get()
    types=pizzatypes.get()
    quantity=pizzaamount.get()
    orderlabel.config(text="You ordered "+str(quantity)+" "+str(sizes)+" "+str(types)+" pizzas.Thankyou for ordering")

Title_Label=Label(root,text="Pizza App")
choose_label=Label(root,text="Choose your pizza type and amount")
pizz=StringVar()
pizzasize1=Radiobutton(root,text="S",variable=pizz,value="S")
pizzasize2=Radiobutton(root,text="M",variable=pizz,value="M")
pizzasize3=Radiobutton(root,text="L",variable=pizz,value="L")
pizza=["chicken and beef","extra cheesy special","veggie pool","pepperonni"]
pizzatypes=Combobox(root,values=pizza)
pizzatypes.current(0)
pizzaam=IntVar()
pizzaamount=Combobox(root,textvariable=pizzaam)
pizzaamount['values']=tuple(range(31))
orderbutton=Button(root,text="Order",command=order)
orderlabel=Label(root)

#placement
Title_Label.grid(row=1,column=5)
choose_label.grid(row=2,column=1)
pizzatypes.grid(row=2,column=5)
pizzaamount.grid(row=2,column=6)
orderbutton.grid(row=5,column=5)
orderlabel.grid(row=6,column=5)
pizzasize1.grid(row=2,column=7)
pizzasize2.grid(row=3,column=7)
pizzasize3.grid(row=4,column=7)

root.mainloop()