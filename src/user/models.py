from django.db import models
from django.contrib.auth.models import (BaseUserManager,
                                        AbstractBaseUser,
                                        PermissionsMixin)
from django.conf import settings

class CommonModelFields:
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

class UserManager(BaseUserManager):
    """
    Prodives helper functions to create user and super user
    to the custom model
    """

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(CommonModelFields, AbstractBaseUser, PermissionsMixin):
    """
    Custom user model.
    """

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    is_acitve = models.BooleanField(default=True)

    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class ProfileImage(CommonModelFields, models.Model):
    image_url = models.URLField()
    is_current_profile = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             related_name='profile_images')

    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)


class FriendShip (CommonModelFields, models.Model):
    """
    User friend ship model

    ======================

    This model records information about users incoming and outgoing
    friend requests with their status which can be one of
    (accepted, rejected, pending, and blocked)

    """

    FRIENDSHIP_STATUS = (
        ('Accepted', 'accepted'),
        ('Pending', 'pending'),
        ('Rejected', 'rejected'),
        ('Blocked', 'blocked')
    )
    request_from = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friend_requests')

    request_to = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   models.CASCADE, related_name='sent_requests')

    friendship_status = models.CharField(
        max_length=255, choices=FRIENDSHIP_STATUS, default='Pending')
