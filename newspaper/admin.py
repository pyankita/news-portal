from django.contrib import admin
from newspaper.models import Category,Post,Tag,Advertisement

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
