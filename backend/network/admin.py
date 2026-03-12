from django.contrib import admin
from .models import NetworkNode


@admin.action(description="Clear debt to supplier")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "city",
        "supplier",
        "debt",
        "created_at",
    )

    list_filter = ("city",)

    actions = [clear_debt]