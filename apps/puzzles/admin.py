from django.contrib import admin

from .models import Puzzle


class PuzzleAdmin(admin.ModelAdmin):
    readonly_fields = (
        "cooked_description",
        "slug",
        "original_raw_data",
    )
    list_display = ("title", "source", "difficulty", "is_active")


admin.site.register(Puzzle, PuzzleAdmin)
