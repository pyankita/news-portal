from django.contrib import admin
from newspaper.models import Category,Post,Tag,Advertisement,Contact,UserProfile,Comment

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
