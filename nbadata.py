import requests
import json
from tkinter import *
import tkinter  as tk

def response(date):
    realurl = "http://matchweb.sports.qq.com/kbs/list"+"?"+\
        "from=NBA_PC&columnId=100000&startTime="+date+"&endTime="+date+"&callback=ajaxExec&_=1521188243644"
    req = requests.post(realurl)
    rsp = req.text

    #切片
    rex = str(rsp.split('ajaxExec(')[1])
    #获取rex长度
    s = len(rex)
    #取s-个字符
    rex = str(rex[:s-1])
    return rex

def reslove():
    date = var.get()
    str1 = response(date)
    js = json.loads(str1)
    gameList = js["data"][date]
    scoreboard.delete(0.0,END)
    str2 = "客队".ljust(5)+ "     比分   ".ljust(13) +"主队  ".ljust(7)+"节次".ljust(7)+"   剩余时间\n"
    scoreboard.insert(2.0, str2)

    for list in gameList:
        liststr = str(list)
        liststr = liststr.replace("'", '"')
        json1 = json.loads(liststr)
        leftName = json1["leftName"]
        leftGoal = json1["leftGoal"]
        rightName = json1["rightName"]
        rightGoal = json1["rightGoal"]
        quarter = json1["quarter"]
        quarterTime = json1["quarterTime"]
        str1 = leftName.ljust(5)+" "+leftGoal.ljust(5)+" : "+rightGoal.ljust(5)+" "+rightName.ljust(5)+"   "+quarter.ljust(5)+"   "+quarterTime.ljust(5)+"\n"

        scoreboard.insert(3.0,str1)

root = Tk()
root.title("NBA数据")
scoreboard = Text(root)
scoreboard.pack()
var = StringVar()
Entry(root,textvariable=var).pack()
goBtn = Button(text = "输入时间:",command = reslove)
goBtn.pack()
root.mainloop()


