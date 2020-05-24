from django.contrib import admin
from .models import User, ProfileImage, FriendShip

admin.site.register(User)
admin.site.register(ProfileImage)
admin.site.register(FriendShip)
