from django.contrib import admin

# Register your models here.
from v_sqlite.models import *

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Note)
