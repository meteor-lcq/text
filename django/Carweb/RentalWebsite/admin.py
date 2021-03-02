from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Tag)
admin.site.register(Func)
admin.site.register(Sex)
admin.site.register(Level)
admin.site.register(Stars)
admin.site.register(State)
#admin.site.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','acnum','sex','level']
    fieldsets = (
        ('账号',{'fields':['acnum']}),
        ('姓名',{'fields':['name']}),
        ('密码', {'fields': ['password']}),
        ('性别', {'fields': ['sex']}),
        ('身份证', {'fields': ['identity_id']}),
        ('等级', {'fields': ['level']}),
        ('电话', {'fields': ['phone']}),
        ('邮箱', {'fields': ['email']}),
    )
admin.site.register(User,UserAdmin)
# admin.site.register(Vehicle_leasing)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['id','v_name','v_func','v_type','v_addr']
    fieldsets = (
        ('名称',{'fields':['v_name']}),
        ('车型',{'fields':['v_type']}),
        ('车用', {'fields': ['v_func']}),
        ('座位数', {'fields': ['v_set']}),
        ('租用价格', {'fields': ['v_price_day']}),
        ('超时价格', {'fields': ['v_price_overtime']}),
        ('押金', {'fields': ['v_cash_pledge']}),
        ('所在地', {'fields': ['v_addr']}),
        ('车辆图片', {'fields': ['v_picture']}),
        ('预订次数', {'fields': ['v_browse']})
    )
admin.site.register(Vehicle_leasing,VehicleAdmin)
# admin.site.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ['id','d_acnum','d_name','d_star']
    fieldsets = (
        ('账号',{'fields':['d_acnum']}),
        ('名称', {'fields': ['d_name']}),
        ('头像', {'fields': ['d_photo']}),
        ('联系电话', {'fields': ['d_phone']}),
        ('地址', {'fields': ['d_addr']}),
        ('星级', {'fields': ['d_star']}),
        ('雇用价格', {'fields': ['d_price']}),
        ('经验', {'fields': ['d_exprience']}),
        ('状态', {'fields': ['d_state']}),
        ('预订次数', {'fields': ['d_browse']}),
    )
admin.site.register(Driver,DriverAdmin)
# admin.site.register(Send_driver)
class SendAdmin(admin.ModelAdmin):
    list_display = ['id','sd_acnum','sd_name','sd_num']
    fieldsets = (
        ('账号',{'fields':['sd_acnum']}),
        ('名称', {'fields': ['sd_name']}),
        ('头像', {'fields': ['sd_photo']}),
        ('地址', {'fields': ['sd_addr']}),
        ('联系电话', {'fields': ['sd_phone']}),
        ('订单数', {'fields': ['sd_num']})
    )
admin.site.register(Send_driver,SendAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','o_user','o_vehicle','o_vehicle_use','o_time']
    fieldsets = (
        ('用户',{'fields':['o_user']}),
        ('租用车名称', {'fields': ['o_vehicle']}),
        ('租用车车用', {'fields': ['o_vehicle_use']}),
        ('送车员', {'fields': ['o_send']}),
        ('下单时间', {'fields': ['o_time']}),
        ('开始日期', {'fields': ['o_time_to']}),
        ('租用时长', {'fields': ['o_day']}),
        ('地址', {'fields': ['o_addr']}),
        ('租金', {'fields': ['o_money']})
    )
admin.site.register(Order,OrderAdmin)
# admin.site.register(Order)
class D_orderAdmin(admin.ModelAdmin):
    list_display = ['id','do_user','do_drivid','do_driver','do_time']
    fieldsets = (
        ('用户',{'fields':['do_user']}),
        ('司机id',{'fields':['do_drivid']}),
        ('司机', {'fields': ['do_driver']}),
        ('开始结束', {'fields': ['do_time_to']}),
        ('天数', {'fields': ['do_day']}),
        ('下单时间', {'fields': ['do_time']}),
        ('租金', {'fields': ['do_money']})
    )
admin.site.register(D_order,D_orderAdmin)
admin.site.register(Tag_news)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id','title','tag','date','time','browse']
    fieldsets = (
        ('标题',{'fields':['title']}),
        ('标签', {'fields': ['tag']}),
        ('内容', {'fields': ['content']}),
        ('浏览次数', {'fields': ['browse']})
    )
admin.site.register(News,NewsAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','username','date','text']
    fieldsets = (
        ('用户', {'fields':['username']}),
        ('日期', {'fields': ['date']}),
        ('内容', {'fields': ['text']})
    )
admin.site.register(Comment,CommentAdmin)

# class TagAdmin(admin.ModelAdmin):
#     list_display = ["name"]
#     fieldsets = (
#         ('车辆用途标签',{'fields': ['name']})
#     )
# admin.site.register(Tag,TagAdmin)
#
# class LevelAdmin(admin.ModelAdmin):
#     list_display = ["lve_zi"]
#     fieldsets = (
#         ('用户等级',{'fields':['lev_zi']})
#     )
# admin.site.register(Level,LevelAdmin)
#
# class StarsAdmin(admin.ModelAdmin):
#     list_display=["mumber"]
#     fieldsets = (
#         ('星级数字',{'fields':['mumber']})
#     )
# admin.site.register(Stars,StarsAdmin)

# class StateAdmin(admin.ModelAdmin):
#     list_display = ["id","state"]
#     fieldsets = (
#         ('状态说明',{'fields':['state']})
#     )
# admin.site.register(State,StateAdmin)
