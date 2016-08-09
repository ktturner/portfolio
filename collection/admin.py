from django.contrib import admin
from collection.models import Pattern, Illustration, Sketchbook, UploadPattern, UploadIllustration, UploadSketchbook

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

class UploadPatternAdmin(admin.ModelAdmin):
    list_display = ('pattern', )
    list_display_links = ('pattern', )

admin.site.register(UploadPattern, UploadPatternAdmin)

class UploadIllustrationAdmin(admin.ModelAdmin):
    list_display = ('illustration', )
    list_display_links = ('illustration', )

admin.site.register(UploadIllustration, UploadIllustrationAdmin)

class UploadSketchbookAdmin(admin.ModelAdmin):
    list_display = ('sketchbook', )
    list_display_links = ('sketchbook', )

admin.site.register(UploadSketchbook, UploadSketchbookAdmin)
