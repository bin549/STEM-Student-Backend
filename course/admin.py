from django.contrib import admin
from .models import Entity, Genre, Selection, Collection, Lecture, Format

admin.site.register(Entity)
admin.site.register(Genre)
admin.site.register(Selection)
admin.site.register(Collection)
admin.site.register(Lecture)
admin.site.register(Format)
