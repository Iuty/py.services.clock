# coding : utf8
import time,os,datetime
from IutyLib.notice.notice import WeChat_SMS
from IutyLib.commonutil.config import Config



configpath = os.path.join(os.path.abspath("."),"Config","Clock.ini")
print("服务启动")


def sendNotice(msg):
    wx = WeChat_SMS("Wa1gyn8MWpiqPv02372ZEGhoEXUIqv6qSrESK82a1Vw","1000004")
    wx.send_data(msg)
    pass

def getClassTimes():
    
    cfg = Config(configpath)
    cs = cfg.getOptions("Classes")
    
    rtn = {}
    for c in cs:
        rtn[c] = cfg.get("Classes",c)
        print("add class "+ c)
    return rtn

def timeCompare(ta,tb):
    
    return (ta.hour == tb.hour) and (ta.minute == tb.minute) and (ta.second == tb.second)

def checkClasses(kv):
    now = datetime.datetime.now().time()
    for di in kv:
        t = datetime.datetime.strptime(di,'%H.%M').time()
        if timeCompare(t,now):
            sendNotice(kv[di])
    pass



if __name__ == "__main__":
    classes = getClassTimes()
    
    while True:
        checkClasses(classes)
        time.sleep(0.97)