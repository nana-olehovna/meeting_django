from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Category, Cart, CartItem, Order, OrderItem, Purchase

# Register your models here.

class CustomProduct(admin.ModelAdmin):
    list_display = ['title', 'director', 'category', 'year', 'rating', 'price', 'isInStock']
    search_fields = ('title', 'description', 'category')
    list_filter = ('director', 'category')
    fieldsets = (
        ('Main info:', {'fields': ('title', 'description')}),
        ('Additional_data:', {'fields': ('director', 'category', 'year', 'rating', 'price', 'image', 'isInStock')}),
        ('Dates', {'fields': ('create_at', 'update_at')}),
        )
    readonly_fields = ('create_at', 'update_at')


class CustomUser(UserAdmin):
    list_display = ['username', 'is_staff', 'is_active']
    search_fields = ('username',)
    list_filter = ('is_staff', 'is_active')


class CustomCart(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ('user',)


class CustomCartItem(admin.ModelAdmin):
    list_display = ['item', 'quantity', 'cart']
    search_fields = ('item', 'cart')


class CustomOrder(admin.ModelAdmin):
    list_display = ['user', 'total_price']
    search_fields = ('user',)


class CustomOrderItem(admin.ModelAdmin):
    list_display = ['product', 'order']
    search_fields = ('order', 'product')


class CustomPurchase(admin.ModelAdmin):
    list_display = ['item', 'paid_at']
    search_fields = ('item',)


admin.site.register([ Category])
admin.site.register(Product, CustomProduct)
admin.site.register(User, CustomUser)
admin.site.register(Cart, CustomCart)
admin.site.register(CartItem, CustomCartItem)
admin.site.register(Order, CustomOrder)
admin.site.register(OrderItem, CustomOrderItem)
admin.site.register(Purchase, CustomPurchase)

