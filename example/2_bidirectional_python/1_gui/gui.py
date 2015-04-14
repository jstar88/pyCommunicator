from pyCommunicator.BackEndMarshalCallback import BackEndMarshalCallback

b = BackEndMarshalCallback()
b.run()



import Tkinter

top = Tkinter.Tk()

def helloCallBack():
    b.write('button pressed')

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B.pack()
top.mainloop()