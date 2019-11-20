from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from common.models import Types, Goods
from common.views import loadinfo


def index(request):
    """浏览购物车"""
    context = loadinfo(request)
    # 缓存/会话session中没有ShopList（购物车列表），默认指定为空
    if 'ShopList' not in request.session:
        request.session['ShopList'] = {}
    context['shoplist'] = request.session['ShopList']
    return render(request, 'cart/cart_list.html', context)

def add(request, gid):
    """在购物车中放入的商品信息"""
    # 获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=gid)
    shop = goods.toDict()
    shop['m'] = int(request.POST.get('m', 1))

    # 从session获取的购物车信息，没有默认空字典
    ShopList = request.session.get('ShopList', {})
    # 判断该商品是否存在在购物车中
    if gid in ShopList:
        # 商品数量加
        ShopList[gid]['m'] += shop['m']
    else:
        # 新商品添加
        ShopList[gid] = shop
    # 将购物车信息放回到session中
    request.session['ShopList'] = ShopList
    # 重定向到浏览购物车页面
    return redirect(reverse('cart_index'))

def delete(request, gid):
    """删除一个商品"""
    ShopList = request.session['ShopList']
    del ShopList[gid]
    request.session['ShopList'] = ShopList
    return redirect(reverse('cart_index'))

def clear(request):
    """清空购物车"""
    request.session['ShopList'] = {}
    return redirect(reverse('cart_index'))

def change(request,gid):
    """更改购物车数量"""
    ShopList = request.session['ShopList']
    # 获取信息
    shopid = gid
    num = int(request.GET['num'])
    if num < 1:
        num = 1
    ShopList[shopid]['m'] = num   # 更改商品数量
    request.session['ShopList'] = ShopList
    return redirect(reverse('cart_index'))
