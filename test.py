import tkinter as tk
from tkinter import messagebox        #引入弹窗库
import time
import sched  # 定时器

window=tk.Tk()
# window.title('该吃药了')
# window.geometry('500x600')

def hit_me():
    #tc1=messagebox.askokcancel(title='hello',message='hello word') #弹窗 return True/False
    #print (tc1)
    #tc2=messagebox.askquestion(title='hello',message='hello word') #return yes/no
    #print (tc2)
    tc3=messagebox.showinfo(title='吃药吧',message='吃了药就好了！')  # return ok
    print (tc3)
# tk.Button(window,text='你打我呀!',command=hit_me).pack()
schedule = sched.scheduler ( time.time, time.sleep )
print(time.time())
schedule.enter(10,0,hit_me)
schedule.enter(20,0,hit_me)
schedule.enter(30,0,hit_me)
schedule.enter(40,0,hit_me)
schedule.run()
print(time.time())
window.mainloop()
