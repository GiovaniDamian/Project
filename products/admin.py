from django.contrib import admin
from .models import Product, ProductSala, ProductQuarto, ProductLimpeza, ProductEletronico, ProductCozinha, ProductAcampamento, ProductBanheiro, ProductCapacetes


class ProductAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'description', 'image_url')


class ProductSalaAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'price', 'description', 'image_url')


admin.site.register(Product,ProductAdmin)
admin.site.register(ProductSala, ProductSalaAdmin)
admin.site.register(ProductEletronico, ProductAdmin)
admin.site.register(ProductLimpeza, ProductAdmin)
admin.site.register(ProductQuarto, ProductAdmin)
admin.site.register(ProductBanheiro, ProductAdmin)
admin.site.register(ProductCapacetes, ProductAdmin)
admin.site.register(ProductAcampamento, ProductAdmin)
admin.site.register(ProductCozinha, ProductAdmin)
