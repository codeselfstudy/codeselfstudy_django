from django.contrib import admin

from .models import Language, LanguageVariantName


class LanguageVariantNameInline(admin.StackedInline):
    model = LanguageVariantName
    extra = 2


class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    fieldsets = [
        (None,               {"fields": ["name"]}),
        ("Meta Data", {"fields": ["created_at", "updated_at"]}),
    ]
    inlines = [LanguageVariantNameInline]
    # list_display = ("name", "")


admin.site.register(Language, LanguageAdmin)
# admin.site.register(LanguageVariantName, LanguageVariantNameInline)
