from django.contrib import admin
from django.urls import reverse
# Register your models here.
from .models import Category,Product,Brand,ProductImage,ProductLine
from django.utils.safestring import mark_safe





class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else:
            return ""

class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInline,
    ]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]



class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]

admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)