from django.conf.urls import url
from users import views

urlpatterns = [
    # 会员个人信息的路由配置
    url(r'^login$', views.login, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout')
]