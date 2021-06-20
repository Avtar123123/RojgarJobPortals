from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Company)
admin.site.register(Candidates)

admin.site.register(Course)
admin.site.register(Question)
admin.site.register(ScoreBoard)