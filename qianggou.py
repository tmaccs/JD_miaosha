#京东秒杀
#加入购物车 再结算
from splinter.browser import Browser
from selenium import webdriver
import time
import datetime

#登录页面
def login(b):  #登录京东
    b.click_link_by_text("你好，请登录")
    b.click_link_by_text("账户登录")
    time.sleep(1)
    b.fill("loginname","tmaccs")  #填写账户密码
    b.fill("nloginpwd","Zz236668777")
    b.find_by_id("loginsubmit").click()
    # time.sleep(0.1)
    return b

#订单页面
def loop(b):  #循环点击
    try:
        if b.title=="订单结算页 -京东商城":
            # b.find_by_text("保存收货人信息").click()
            # b.find_by_text("保存支付及配送方式").click()
            b.find_by_id("order-submit").click()
            return b
        else:  #多次抢购操作后，有可能会被转到京东首页，所以要再打开手机主页
            b.visit("hhttps://item.jd.com/4918296.html")
            b.find_by_id("choose-btn-qiang").click()
            time.sleep(10)
            loop(b)  #递归操作
    except Exception as e: #异常情况处理，以免中断程序
        b.reload()  #重新刷新当前页面，此页面为订单提交页
        time.sleep(2)
        loop(b)  #重新调用自己

def buy_time(buytime):
    while True:
        now = datetime.datetime.now()
        #print(now.strftime('%Y-%m-%d %H:%m:%S'))
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            while True:
                b.find_by_id("choose-btn-ko").click()  # 找到抢购按钮，点击
                b.find_by_id("GotoShoppingCart").click()#只有使用这个才能配套使用 b.find_by_css(".submit-btn").click()
                b.find_by_css(".submit-btn").click()
                loop(b)
                if b.is_element_present_by_id("tryBtn"):  # 订单提交后显示“再次抢购”的话
                    b.find_by_id("tryBtn").click()  # 点击再次抢购，进入读秒5，跳转订单页
                    time.sleep(6.5)
                elif b.title == "订单结算页 -京东商城":  # 如果还在订单结算页
                    time.sleep(3)
                    b.find_by_id("order-submit").click()
                else:
                    print('恭喜你，抢购成功')
                    print(now.strftime('%Y-%m-%d %H:%M:%S'))
                    break

b=Browser(driver_name="chrome") #打开浏览器
b.visit("https://item.jd.com/4918296.html")
login(b)
#获取现在时间
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
#设置抢购的时间
buy_time('2017-10-10 21:58:01')



