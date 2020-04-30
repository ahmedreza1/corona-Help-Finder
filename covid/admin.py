from django.contrib import admin
from .models import State, MyPost, MyProfile, MyPayment

# Register your models here.
admin.site.register(State)
admin.site.register(MyPost)
admin.site.register(MyProfile)
admin.site.register(MyPayment)