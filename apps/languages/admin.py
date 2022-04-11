# TODO: This old code doesn't work, so it needs to be updated.

# SystemCheckError: System check identified some issues:
# ERRORS:
# <class 'languages.admin.LanguageAdmin'>: (admin.E035) The value of 'readonly_fields[0]' is not a callable, an attribute of 'LanguageAdmin', or an attribute of 'languages.Language'.
# <class 'languages.admin.LanguageAdmin'>: (admin.E035) The value of 'readonly_fields[1]' is not a callable, an attribute of 'LanguageAdmin', or an attribute of 'languages.Language'.

from django.contrib import admin

from .models import Language, LanguageVariantName


class LanguageVariantNameInline(admin.StackedInline):
    model = LanguageVariantName
    extra = 2


class LanguageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["name", "description"]}),
        ("Meta Data", {"fields": ["created", "updated"]}),
    ]
    inlines = [LanguageVariantNameInline]
    list_display = ("name", "variant_names")

    def variant_names(self, obj):
        return len(obj.languagevariantname_set.all())


admin.site.register(Language, LanguageAdmin)
