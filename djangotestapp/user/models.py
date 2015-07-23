from datetime import date

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.sessions.backends.db import SessionStore


class UrlData(models.Model):
    url = models.CharField(max_length=250, primary_key=True)
    tags_count = models.IntegerField(default=0)
    meta_tags_count = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    date_time = models.DateTimeField(default=None)

    @property
    def size_in_mb(self):
        return self.size * 1.0 / 1024


class Anchors(models.Model):
    url = models.ForeignKey('UrlData', related_name='anchors')
    link = models.CharField(max_length=250)


class Session(SessionStore):
    last_session_date = models.DateTimeField(default=date.today())
    current_session_date = models.DateTimeField(default=date.today())
    session_count = models.IntegerField(default=1)


class UserManager(BaseUserManager):
    def create_user(self, email, username, gender, address, password=None):

        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must choose a user name')
        if not gender:
            raise ValueError('Users must select gender')
        if not address:
            raise ValueError('Address must be given.')

        user = self.model(email=UserManager.normalize_email(email), username=username, gender=gender, address=address)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, gender, address, password):
        user = self.create_user(email=email, username=username, gender=gender, address=address, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    username = models.CharField(max_length=255)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'gender', 'address']

    def get_full_name(self):
        """ The user is identified by their email address """
        return self.email

    def get_short_name(self):
        """ The user is identified by their email address """
        return self.email

    def __unicode__(self):
        return self.email

    # noinspection PyMethodMayBeStatic
    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?
           Simplest possible answer: Yes, always"""
        return True

    # noinspection PyMethodMayBeStatic
    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?
           Simplest possible answer: Yes, always"""
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?
           Simplest possible answer: All admins are staff"""
        return self.is_admin




