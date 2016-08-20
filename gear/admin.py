from django.contrib import admin
from .models import List, Item, UserProfile


admin.site.register(UserProfile)
admin.site.register(List)
admin.site.register(Item)

