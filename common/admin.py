from django.contrib import admin

# Register your models here.
from .models import Users, Goods, Types, Orders, Details


class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'gender', 'address', 'phone', 'addtime']
    list_filter = ['name']
    search_fields = ['name']
    # 每页显示10条信息
    list_per_page = 10

admin.site.register(Users, UserAdmin)
admin.site.register(Goods)
admin.site.register(Types)
admin.site.register(Orders)
admin.site.register(Details)
