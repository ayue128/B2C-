from django.core.paginator import Paginator, PageNotAnInteger, InvalidPage, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from common.models import Goods, Types
from common.views import loadinfo


def lists(request, page=1):
    """商品列表页（搜索&分页）"""
    context = loadinfo(request)
    # 获取商品信息查询对象
    goods = Goods.objects
    # 根据条件筛选商品列表
    tid = request.GET.get('tid', None)
    if tid:
        # 根据tid筛选
        goods = goods.filter(typeid=tid)
    kw = request.GET.get('kw')
    if kw:
        # 根据关键字模糊搜索
        goods = goods.filter(goods__contains=kw)
    goods = goods.all().order_by('-addtime')
    # 分页

    paginator = Paginator(goods, per_page=2)
    try:
        goods = paginator.page(page)    # 获取指定页的商品
        print("当前页的商品信息：", goods.object_list)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页
        goods = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页
        goods = paginator.page(paginator.num_pages)
    except InvalidPage:
        # 如果请求的页数不存在，重定向页面
        return Http404('找不到页面的内容')

    # 封装信息加载模板输出
    context['goods'] = goods
    context['paginator'] = paginator

    print(goods)
    return render(request, 'goods/list.html', context)


def detail(request, gid):
    """商品详情页"""
    context = loadinfo(request)
    # 加载商品详情信息
    ob = Goods.objects.get(id=gid)
    ob.clicknum += 1   # 点击量加1
    ob.save()
    context['good'] = ob
    return render(request, 'goods/detail.html', context)