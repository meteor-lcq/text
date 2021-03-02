from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.core.paginator import Paginator
from django.utils import timezone
import json
from django import forms
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request, 'renweb/html/home.html')

def loto(request):
    return render(request, 'renweb/html/login.html')

def login(request):
    # if request.method == 'post':
    #     username=request.POST.get('username')
    #     passwd=request.POST.get('password')
    #     log=User.objects.filter(acnum=username,password=passwd)
    #     if log:
    #         return JsonResponse({'success': '200', 'msg': '登录成功'})
    #     else:
    #         return JsonResponse({'success': '201', 'msg': '登录失败'})
    if request.method == 'GET':
        return render(request, 'renweb/html/login.html')
    if request.method == 'POST':
        username=request.POST.get('username')
        passwd=request.POST.get('passwd')
        log=User.objects.values().filter(acnum=username,password=passwd)
        if log:
            request.session['acnum'] = username
            request.session['password'] = passwd
            return JsonResponse({'log': '200', 'acnum': username,'passwd':passwd})
        else:
            return JsonResponse({'log': '201', 'msg': '登录失败'})
    # return render(request, 'renweb/html/login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'renweb/html/login.html')
    if request.method == 'POST':
        ruser=request.POST.get('ruser')
        rname = request.POST.get('rname')
        rpass = request.POST.get('rpass')
        rsex = request.POST.get('rsex')
        riden = request.POST.get('ridentity')
        rlevel = request.POST.get('rlevel')
        rphone = request.POST.get('rphone')
        rmail = request.POST.get('rmail')
        c_acnum=User.objects.values().filter(acnum=ruser)
        if c_acnum:
            return JsonResponse({'reg':'211','msg':'账号存在'})
        c_name = User.objects.values().filter(name=rname)
        c_iden=User.objects.values().filter(identity_id=riden)
        if c_name and c_iden:
            return JsonResponse({'reg': '212', 'msg': '姓名与身份证存在'})
        wsex=Sex.objects.get(sex=rsex)
        wlevel=Level.objects.get(lev_zi=rlevel)
        reg=User(acnum=ruser,name=rname,password=rpass,sex=wsex,identity_id=riden,level=wlevel,phone=rphone,email=rmail)
        reg.save()
        return JsonResponse({'reg': '210', 'msg': '注册成功'})
    return render(request, 'renweb/html/login.html')

def base(request):
    if request.method=='GET':
        user=request.session.get('acnum')
        passwd=request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        return render(request, 'renweb/html/base.html',context={'user':user,'passwd':passwd,'log':log})

def ranking(request):
    if request.method=='GET':
        user=request.session.get('acnum')
        passwd=request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        rankcar=Vehicle_leasing.objects.order_by("-v_browse")[0:5]
        rankdriver=Driver.objects.order_by("-d_browse")[0:5]
        return render(request, 'renweb/html/ranking.html',context={'log':log,'rankcar':rankcar,'rankdriver':rankdriver})

def news_in(request,pindex):
    if request.method=='GET':
        user=request.session.get('acnum')
        passwd=request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        allnews = News.objects.order_by('-date','-time')
        paginator = Paginator(allnews, 8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        return render(request, 'renweb/html/news_in.html',context={'log':log,'page':page})

def news_out(request):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        newsid=request.GET.get('id')
        news=News.objects.get(id=newsid)
        news.browse+=1
        news.save()
        news=News.objects.get(id=newsid)
        return render(request,'renweb/html/news_out.html',context={'log':log,'news':news})

def self_desc(request):
    if request.method=='GET':
        user=request.session.get('acnum')
        passwd=request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        return render(request, 'renweb/html/self_description.html',context={'user':user,'passwd':passwd,'log':log})

def send_check(request):
    user = request.session.get('acnum')
    passwd = request.session.get('password')
    log = User.objects.get(acnum=user, password=passwd)
    subject = '明汽租赁'	#主题
    message = '预订信息'	#内容
    sender = settings.EMAIL_FROM		#发送邮箱，已经在settings.py设置，直接导入
    receiver = [log.email]		#目标邮箱
    html_message = '<h1>欢迎您使用明汽租赁！</h1></br>' \
                   '<h1>您刚才已经完成订单！<h1>' \
                   '<h1>欢迎继续使用！<h1>'		#发送html格式
    send_mail(subject,message,sender,receiver,html_message=html_message)

def check(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        order=Order.objects.filter(o_user=user)
        if order:
            have=True
            send_check(request)
            return render(request, 'renweb/html/check.html', context={'log': log, 'order':order[0],"have":have})
        else:
            have=False
            return render(request, 'renweb/html/check.html', context={'log': log, 'have':have})
    if request.method == 'POST':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        if request.POST.get('finish')=="ok":
            Order.objects.filter(o_user=user).delete()
            return JsonResponse({'finish': '201', 'msg': "订单完成"})
        else:
            return JsonResponse({'finish': '202', 'msg': "出问题啦！"})

def dricheck(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        dorder=D_order.objects.filter(do_user=user)
        if dorder:
            have=True
            send_check(request)
            return render(request, 'renweb/html/checkdri.html', context={'log': log, 'dorder':dorder[0], "have":have})
        else:
            have=False
            return render(request, 'renweb/html/checkdri.html', context={'log': log, 'have':have})
    if request.method == 'POST':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        if request.POST.get('finish')=="ok":
            dodriid=D_order.objects.get(do_user=user)
            modify = Driver.objects.get(id=dodriid.do_drivid)
            modify.d_state = "在岗"
            modify.save()
            D_order.objects.filter(do_user=user).delete()
            return JsonResponse({'finish': '201', 'msg': "订单完成"})
        else:
            return JsonResponse({'finish': '202', 'msg': "出问题啦！"})

def modify(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        return render(request, 'renweb/html/infomodify.html', context={'log': log})
    if request.method == "POST":
        modsex = request.POST.get('msex')
        modphone = request.POST.get('mphone')
        modemail = request.POST.get('memail')
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        User.objects.filter(acnum=user,password=passwd)[0].update(sex=modsex,phone=modphone,email=modemail)
        log=User.objects.get(acnum=user, password=passwd)
        if log.sex==modsex and log.phone==modphone and log.email==modemail:
            return JsonResponse({'modify': '201', 'msg': "修改完成"})
        else:
            return JsonResponse({'modify': '202', 'msg': "修改出错"})

def signout(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'renweb/html/login.html')

def rentcar(request,pindex):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        allcar=Vehicle_leasing.objects.filter(v_func=1)
        paginator = Paginator(allcar,8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        context = {"log": log, "page": page}
        return render(request,"renweb/html/RentCar.html", context)

def weddingrent(request,pindex):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        allcar=Vehicle_leasing.objects.filter(v_func=3)
        paginator = Paginator(allcar,8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        context = {"log": log, "page": page}
        return render(request,"renweb/html/weddingrent.html", context)

def conference_car(request,pindex):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        allcar=Vehicle_leasing.objects.filter(v_func=4)
        paginator = Paginator(allcar,8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        context = {"log": log, "page": page}
        return render(request,"renweb/html/conference_car.html", context)

def details_page(request):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        vid=request.GET.get('id')
        d_car=Vehicle_leasing.objects.get(id=vid)
        return render(request,'renweb/html/details_page.html',context={'log':log,'detcar':d_car})

def ordercar(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        vid = request.GET.get('ocarid')
        d_car = Vehicle_leasing.objects.get(id=vid)
        return render(request, 'renweb/html/details_page.html', context={'log': log, 'detcar': d_car})
    if request.method == 'POST':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        iforder=Order.objects.filter(o_user=user)
        if iforder.count()>0:
            return JsonResponse({'order': '202', 'msg': "已经有订单，请先完成上一个订单"})
        else:
            odate=str(request.POST.get('odate'))#开始日期
            oday = int(request.POST.get('oday'))#天数
            oaddr = request.POST.get('oaddr')#送车地址
            ocarid = request.POST.get('ocarid')
            date = timezone.now()#系统当前时间
            odatenow = date.strftime("%Y-%m-%d %H:%M:%S")#现在时间g格式化
            ocar=Vehicle_leasing.objects.get(id=ocarid)
            ocname=ocar.v_name#车名
            ocuse=ocar.v_func#车用
            ocash=ocar.v_cash_pledge#押金
            odaymoney=ocar.v_price_day#每日租金
            oallmoney=odaymoney*oday+ocash#总租金
            osdall=Send_driver.objects.all()
            osdname=""
            for osd in osdall:
                if osd.sd_num==0:
                    osdname=osd.sd_name#送车员
                    break
            # ord=Order.objects.all()
            # if ord:
            #     ord.delete()
            order = Order(o_user=user, o_vehicle=ocname,o_vehicle_use=ocuse, o_send=osdname,
                        o_time=odatenow,o_time_to=odate,o_day=oday, o_addr=oaddr,
                        o_money=oallmoney)
            order.save()
            ocar.v_browse+=1
            ocar.save()
            return JsonResponse({'order':'201','msg': "预订成功"})

def com_driving(request,pindex):#司机
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        alldriver=Driver.objects.filter(d_state="在岗")
        paginator = Paginator(alldriver,8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        context = {"log": log, "page": page}
        return render(request,"renweb/html/Com_driving.html", context)

def sub_driver(request):
    if request.method=="GET":
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        did=request.GET.get('id')
        driver=Driver.objects.get(id=did)
        return render(request,'renweb/html/sub_driver.html',context={'log':log,'driver':driver})

def send_order(request):
    user = request.session.get('acnum')
    passwd = request.session.get('password')
    log = User.objects.get(acnum=user, password=passwd)
    subject = '明汽租赁'	#主题
    message = '预订信息'	#内容
    sender = settings.EMAIL_FROM		#发送邮箱，已经在settings.py设置，直接导入
    receiver = [log.email]		#目标邮箱
    html_message = '<h1>欢迎您使用明汽租赁！</h1></br>' \
                   '<h1>您刚才预定的车辆或雇佣的司机已经生成！<h1>' \
                   '<h1>请前往网站查看订单！<h1>'		#发送html格式
    send_mail(subject,message,sender,receiver,html_message=html_message)

def orderdriver(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        did = request.GET.get('driverid')
        driver = Driver.objects.get(id=did)
        return render(request, 'renweb/html/sub_driver.html', context={'log': log, 'driver': driver})
    if request.method == 'POST':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        iforder=D_order.objects.filter(do_user=user)
        if iforder.count()>0:
            return JsonResponse({'order': '202', 'msg': "已经有订单，请先完成上一个订单"})
        else:
            dodate=str(request.POST.get('drdate'))#开始日期
            doday = int(request.POST.get('drday'))#天数
            dodriid = request.POST.get('driverid')  # 司机id
            date = timezone.now()#系统当前时间
            dodatenow = date.strftime("%Y-%m-%d %H:%M:%S")#现在时间g格式化
            driver=Driver.objects.get(id=dodriid)
            drname=driver.d_name#司机名
            drprice=driver.d_price#雇佣价格
            drmoney=drprice*doday#每日租金
            # ord=D_order.objects.all()
            # if ord:
            #     ord.delete()
            dorder = D_order(do_user=user,do_drivid=dodriid,do_driver=drname,do_time_to=dodate,
                            do_day=doday,do_time=dodatenow,do_money=drmoney)
            dorder.save()
            modify = Driver.objects.get(id=dodriid)
            modify.d_state = "接单中"
            modify.d_browse+=1
            modify.save()
            send_order(request)
            return JsonResponse({'order':'201','msg': "预订成功"})

def comment(request):
    if request.method == 'GET':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        return render(request, 'renweb/html/base.html', context={'user':user,'passwd':passwd,'log':log})
    if request.method == 'POST':
        user = request.session.get('acnum')
        passwd = request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        comtext=request.POST.get('comtext')
        date = timezone.now()  # 系统当前时间
        datenow = date.strftime("%Y-%m-%d %H:%M:%S")  # 现在时间g格式化
        comment=Comment(username=user,date=datenow,text=comtext)
        comment.save()
        return JsonResponse({'com': '201', 'msg': "评论成功"})


def comment_show(request,pindex):
    if request.method=='GET':
        user=request.session.get('acnum')
        passwd=request.session.get('password')
        log = User.objects.get(acnum=user, password=passwd)
        allcomment = Comment.objects.order_by('-date')
        paginator = Paginator(allcomment, 8)
        if pindex == "":  # django中默认返回空值，所以加以判断，并设置默认值为1
            pindex = 1
        else:  # 如果有返回在值，把返回值转为整数型
            int(pindex)
        page = paginator.page(pindex)  # 传递当前页的实例对象到前端
        return render(request,'renweb/html/comment_show.html',context={'log':log,'page':page})
