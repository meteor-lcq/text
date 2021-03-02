from django.db import models
from DjangoUeditor.models import UEditorField
# Create your models here.

class Tag(models.Model):#标签
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "标签"

class Func(models.Model):#标签
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "车用"

class Sex(models.Model):#性别
    sex=models.CharField(max_length=6)

    def __str__(self):
        return self.sex
    class Meta:
        verbose_name_plural="性别"

class Level(models.Model):#等级
    lev_zi=models.CharField(max_length=4)

    def __str__(self):
        return self.lev_zi
    class Meta:
        verbose_name_plural="用户等级"

class Stars(models.Model):#星级
    mumber=models.CharField(max_length=2)

    def __str__(self):
        return self.mumber
    class Meta:
        verbose_name_plural="星级"

class State(models.Model):#司机状态
    state=models.CharField(max_length=10)#状态说明
    def __str__(self):
        return self.state
    class Meta:
        verbose_name_plural="司机状态"

class User(models.Model):#用户
    id = models.AutoField(primary_key=True)#用户id
    acnum=models.CharField(max_length=10,default="")#用户账号
    name=models.CharField(max_length=20)#用户姓名
    password=models.CharField(max_length=12)#用户密码
    sex=models.ForeignKey(Sex,default="保密")#性别
    identity_id=models.CharField(max_length=18)#省份证
    level=models.ForeignKey(Level,default="普通")#等级
    phone=models.CharField(max_length=11)#联系电话
    email=models.CharField(max_length=30)#邮箱

    def __str__(self):
        return self.acnum
    class Meta:
        verbose_name_plural = "用户"

class Vehicle_leasing(models.Model):#租赁车辆
    id = models.AutoField(primary_key=True)#车辆id
    v_name=models.CharField(max_length=30,null=True)#车辆名称
    v_type=models.ForeignKey(Tag)#车辆车型
    v_func=models.ForeignKey(Func,null=True)#车辆作用
    v_set = models.IntegerField(max_length=2)  # 车辆座位
    v_price_day=models.IntegerField(max_length=5,null=True)#车辆租用价格(每日）
    v_price_overtime=models.IntegerField(max_length=3)#车辆租用超时(每小时)
    v_cash_pledge=models.IntegerField(max_length=6)#车辆押金
    v_addr=models.CharField(max_length=30)#车辆所在地
    v_picture=UEditorField(width=500,height=300,toolbars="full",imagePath="RentalWebsite/")
    v_browse=models.IntegerField(max_length=100,default=0)#预订次数

    def __str__(self):
        return self.v_name
    class Meta:
        verbose_name_plural = "租用车辆"

class Driver(models.Model):#司机
    id = models.AutoField(primary_key=True)#司机id
    d_acnum=models.CharField(max_length=8,default="")#司机账号
    d_name=models.CharField(max_length=20)#司机名称
    d_photo=UEditorField(width=500,height=300,toolbars="full",imagePath="RentalWebsite/")#司机头像
    d_phone = models.CharField(max_length=11,default="")  # 联系电话
    d_addr=models.CharField(max_length=100,default="")#地址
    d_star=models.ForeignKey(Stars)
    d_price=models.IntegerField(max_length=4)#司机雇佣价格
    d_exprience=models.CharField(max_length=5)#司机经验
    # d_state = models.ForeignKey(State, null=True)  # 司机状态
    d_state=models.CharField(max_length=10,default="在岗")#司机状态
    d_browse=models.IntegerField(max_length=100,default=0)#预订次数

    def __str__(self):
        return self.d_acnum
    class Meta:
        verbose_name_plural="司机"

class Send_driver(models.Model):#送车员
    id = models.AutoField(primary_key=True)#送车员id
    sd_acnum = models.CharField(max_length=8,default="")  # 送车员账号
    sd_name = models.CharField(max_length=20)  # 送车员名称
    sd_photo = UEditorField(width=500, height=300, toolbars="full",imagePath="RentalWebsite/")  # 送车员头像
    sd_addr = models.CharField(max_length=100, default="")  # 地址
    sd_phone = models.CharField(max_length=11)  # 联系电话
    sd_num=models.IntegerField(max_length=2,default=0)#订单数
    def __str__(self):
        return self.sd_acnum
    class Meta:
        verbose_name_plural="送车员"

class Order(models.Model):#租车订单
    id =models.AutoField(primary_key=True)#订单id
    o_user=models.CharField(max_length=20)#用户
    o_vehicle=models.CharField(max_length=30)#车名
    o_vehicle_use=models.CharField(max_length=12,null=True)#车用
    o_send=models.CharField(max_length=20)#送车员
    o_time=models.CharField(max_length=50,null=True)#下单时间
    o_time_to=models.CharField(max_length=50,null=True)#租车日期开始
    o_day = models.IntegerField(max_length=3)  #租车时长
    o_addr=models.CharField(max_length=100,null=True)#地址
    o_money=models.IntegerField(max_length=10)#租金
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural="租车订单"

class D_order(models.Model):#代驾订单
    id = models.AutoField(primary_key=True)  # 订单id
    do_user = models.CharField(max_length=20)  # 用户
    do_drivid=models.IntegerField(max_length=10,null=True)#司机编号
    do_driver=models.CharField(max_length=20)#司机名字
    do_time_to = models.CharField(max_length=50,null=True)  # 代驾日期开始
    do_day=models.IntegerField(max_length=3,null=True)#天数
    do_time = models.CharField(max_length=50,null=True) # 下单时间
    do_money=models.IntegerField(max_length=10)#租金
    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name_plural="代驾订单"

class Tag_news(models.Model):#新闻标签
    tag=models.CharField(max_length=10)#标签内容

    def __str__(self):
        return self.tag
    class Meta:
        verbose_name_plural="新闻标签"

class News(models.Model):#新闻
    id=models.AutoField(primary_key=True)#新闻id
    title=models.CharField(max_length=30)# 标题
    tag=models.ForeignKey(Tag_news)#标签
    content=UEditorField(width=500, height=300, toolbars="full",imagePath="RentalWebsite/")#内容
    date=models.DateField(auto_now_add=True)#日期
    time=models.TimeField(auto_now_add=True)#时间
    browse=models.IntegerField(max_length=50,default=0)#浏览次数

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural="新闻"

class Comment(models.Model):#评论
    id = models.AutoField(primary_key=True)  # 评论id
    username=models.CharField(max_length=20)#用户名
    date = models.CharField(max_length=50,null=True)  # 日期
    text=models.CharField(max_length=20)#内容

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural="评论"
