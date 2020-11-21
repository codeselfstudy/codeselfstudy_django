from django.contrib import admin

from .models import Language, LanguageVariantName


class LanguageVariantNameInline(admin.StackedInline):
    model = LanguageVariantName
    extra = 2


class LanguageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    fieldsets = [
        (None, {"fields": ["name", "description"]}),
        ("Meta Data", {"fields": ["created_at", "updated_at"]}),
    ]
    inlines = [LanguageVariantNameInline]
    list_display = ("name", "variant_names")

    def variant_names(self, obj):
        return len(obj.languagevariantname_set.all())


admin.site.register(Language, LanguageAdmin)
