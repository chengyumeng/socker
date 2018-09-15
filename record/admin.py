from django.contrib import admin
from .models import  *

class DBAdmin(admin.ModelAdmin):
    list_display = []
admin.site.register(Club,DBAdmin)
admin.site.register(Record,DBAdmin)
admin.site.register(Socker,DBAdmin)
admin.site.register(Goal,DBAdmin)
admin.site.register(Assist,DBAdmin)
admin.site.register(Competition,DBAdmin)

# Register your models here.
