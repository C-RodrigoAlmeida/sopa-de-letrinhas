from django.contrib import admin
from game.models.word import Word
from game.models.joint import Joint

admin.site.register(Word)

class JointInline(admin.TabularInline):
    model = Joint.words.through
    extra = 0 
    can_delete = True
    verbose_name = "Joint"
    verbose_name_plural = "Joints"

@admin.register(Joint)
class JointAdmin(admin.ModelAdmin):
    inlines = [JointInline]

    def display_words(self, obj):
        return ", ".join([word.word for word in obj.words.all()])

    display_words.short_description = "Palavras"