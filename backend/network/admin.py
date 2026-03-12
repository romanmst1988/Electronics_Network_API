from django.contrib import admin
from django.utils.html import format_html
from .models import NetworkNode


@admin.action(description="Очистить задолженность перед поставщиком")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "city",
        "country",
        "supplier_link",
        "debt",
        "created_at",
    )
    list_filter = ("city", "country", "created_at")
    search_fields = ("name", "city", "country", "email")
    actions = [clear_debt]
    readonly_fields = ("created_at",)

    def supplier_link(self, obj):
        if obj.supplier:
            return format_html(
                '<a href="/admin/network/networknode/{}/change/">{}</a>',
                obj.supplier.id,
                obj.supplier.name,
            )
        return "-"

    supplier_link.short_description = "Поставщик"