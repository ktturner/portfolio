from django.contrib import admin
from collection.models import Pattern, Illustration, Sketchbook

class PatternAdmin(admin.ModelAdmin):
    model = Pattern
    list_display = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Pattern, PatternAdmin)

class IllustrationAdmin(admin.ModelAdmin):
    model = Illustration
    list_display = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Illustration, IllustrationAdmin)

class SketchbookAdmin(admin.ModelAdmin):
    model = Sketchbook
    list_display = ('name', 'description')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Sketchbook, SketchbookAdmin)
