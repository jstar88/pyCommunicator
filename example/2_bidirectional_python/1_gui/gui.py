from pyCommunicator.BackEndJsonCallback import BackEndJsonCallback

b = BackEndJsonCallback()
b.run()



import Tkinter

top = Tkinter.Tk()

def helloCallBack():
    b.write('button pressed')

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()