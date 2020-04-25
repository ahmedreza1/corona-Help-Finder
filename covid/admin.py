from django.contrib import admin
from .models import State, MyPost, MyProfile

# Register your models here.
admin.site.register(State)
admin.site.register(MyPost)
admin.site.register(MyProfile)