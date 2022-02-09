from django.contrib import admin
from .models import Entity, Genre, Selection, Wishlist, Lecture, Format

admin.site.register(Entity)
admin.site.register(Genre)
admin.site.register(Selection)
admin.site.register(Wishlist)
admin.site.register(Lecture)
admin.site.register(Format)
