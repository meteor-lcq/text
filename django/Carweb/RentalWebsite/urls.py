from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^loto',views.loto,name="loto"),
    url(r'^login',views.login,name="login"),
    url(r'^register',views.register,name="register"),
    url(r'^base',views.base,name="base"),
    url(r'^ranking',views.ranking,name="ranking"),
    url(r'^news_in/(.+)/$',views.news_in,name='news_in'),
    url(r'^news_out',views.news_out),
    url(r'^self_desc',views.self_desc,name="self_desc"),
    url(r'^check',views.check,name="check"),
    url(r'^dricheck',views.dricheck,name="dricheck"),
    url(r'^modify',views.modify,name="modify"),
    url(r'^signout',views.signout,name="signout"),
    url(r'^rentcar/(.+)/$',views.rentcar,name="rentcar"),
    url(r'^weddingrent/(.+)/$',views.weddingrent,name="weddingrent"),
    url(r'^conference_car/(.+)/$',views.conference_car,name="conference_car"),
    url(r'^com_driving/(.+)/$',views.com_driving,name="com_driving"),
    url(r'^details_page',views.details_page),
    url(r'^sub_driver',views.sub_driver),
    url(r'^ordercar',views.ordercar,name="ordercar"),
    url(r'^orderdriver',views.orderdriver,name="orderdriver"),
    url(r'^coent',views.comment,name="coent"),
    url(r'^showcomment/(.+)/$',views.comment_show,name='showcomment'),
]