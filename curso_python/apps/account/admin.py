from django.contrib import admin

# Register your models here.
from .models import Move, MoveLine


@admin.register(Move)
class Move(admin.ModelAdmin):
    list_display = ('name', 'date', 'numero_documento', 'total')


# @admin.register(MoveLine)
# class MoveLineaAdmin(admin.ModelAdmin):
#     list_display = ('product', 'detail', 'qty', 'price', 'subtotal')
admin.site.register(MoveLine)