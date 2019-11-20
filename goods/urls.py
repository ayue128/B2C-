from django.conf.urls import url
from goods import views

urlpatterns = [
    url(r'^list$', views.lists, name='list'),
    url(r'^list/(?P<page>[0-9]+)$', views.lists, name="list"), # 分页商品列表展示
    url(r'^detail/(?P<gid>[0-9]+)$', views.detail, name="detail"),  # 商品详情
]