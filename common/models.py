import datetime

from django.db import models

# Create your models here.

class Users(models.Model):
    # 用户信息模型
    username = models.CharField(max_length=32, verbose_name="账号")
    name = models.CharField(max_length=16, verbose_name="真实姓名")
    password = models.CharField(max_length=32, verbose_name="密码")
    sex = models.IntegerField(default=1, verbose_name="性别（1-男 2-女）")
    address = models.CharField(max_length=255, verbose_name="收货地址")
    code = models.CharField(max_length=6, verbose_name="邮政编码")
    phone = models.CharField(max_length=16, verbose_name="电话号码")
    email = models.CharField(max_length=50, verbose_name="邮箱地址")
    state = models.IntegerField(default=1, verbose_name="会员状态（1-启用 2-禁用 3-后台管理员）")
    # 注册时间，auto_now_add：在创建时设置时间，后面修改时间不会改变
    addtime = models.DateTimeField(auto_now_add=True)
    modifytime = models.DateTimeField(auto_now=True)

    def gender(self):
        if self.sex == 1:
            return "男"
        elif self.sex == 2:
            return "女"
        else:
            return "未知"

    def toDict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'name': self.name,
            'password' : self.password,
            'address' : self.address,
            'phone' : self.phone,
            'email' : self.email,
            'state' : self.state,
            'addtime' : str(self.addtime),
            'modiftime' : str(self.modifytime)
        }

    def __str__(self):
        return self.name

    class Meta:
        # 单数时显示的名称
        verbose_name = "会员信息"
        # 复数时显示的名称
        verbose_name_plural = "会员信息"

class Types(models.Model):
    name = models.CharField(max_length=32, verbose_name="商品名称")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "商品分类信息"
        verbose_name_plural = "商品分类信息"

class Goods(models.Model):
    # 商品信息模型
    typeid = models.ForeignKey('Types', on_delete=False, verbose_name="类别ID")
    goods = models.CharField(max_length=32, verbose_name="商品名称")
    company = models.CharField(max_length=50, verbose_name="生产厂家")
    content = models.TextField(verbose_name="详情描述")
    price = models.FloatField(verbose_name="商品单价")
    picname = models.ImageField(upload_to='upload/%Y/%m', verbose_name="商品图片")
    store = models.IntegerField(default=0, verbose_name="库存量")
    num = models.IntegerField(default=0, verbose_name="购买数量")
    clicknum = models.IntegerField(default=0, verbose_name="点击次数")
    state = models.IntegerField(default=1, verbose_name="商品状态（1-新添加 2-在售 3-下架）")
    addtime = models.DateTimeField(auto_now_add=True, verbose_name="添加时间")
    modifytime = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    def __str__(self):
        return self.goods

    def toDict(self):
        return {
            'id' : self.id,
            'typeid' : self.typeid.id,
            'goods' : self.goods,
            'company' : self.company,
            'price' : self.price,
            'store' : self.store,
            'num' : self.num,
            'clicknum' : self.clicknum,
            'state' : self.state,
            'addtime' : str(self.addtime),
            'modifytime' : str(self.modifytime),
            'picname': self.picname.name
        }

    class Meta:
        # 单数时显示的名称
        verbose_name = '商品信息'
        # 复数时显示的名称
        verbose_name_plural = "商品信息"

class Orders(models.Model):
    # 订单信息
    uid = models.ForeignKey('Users', on_delete=False, verbose_name="用户id")
    linkman = models.CharField(max_length=32, verbose_name="联系人")
    address = models.CharField(max_length=255, verbose_name="地址")
    code = models.CharField(max_length=6, verbose_name="邮编")
    phone = models.CharField(max_length=16, verbose_name="联系电话")
    addtime = models.DateTimeField(auto_now_add=True, verbose_name="购买时间")
    total = models.FloatField(verbose_name="总金额")
    state = models.SmallIntegerField(verbose_name="订单状态（0-新订单 1-已发货 2-已收货 3-无效订单）")

    def __str__(self):
        return self.uid

    class Meta:
        verbose_name = "订单信息表"
        verbose_name_plural = "订单信息表"

class Details(models.Model):
    order_id = models.ForeignKey('Orders', on_delete=False, verbose_name="订单编号")
    goods_id = models.ForeignKey('Goods', on_delete=False, verbose_name="商品编号")
    name = models.CharField(max_length=32, verbose_name="商品名称")
    price = models.FloatField(verbose_name="商品单价")
    num = models.IntegerField(verbose_name="商品数量")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "订单信息详情表"
        verbose_name_plural = "订单信息详情表"
