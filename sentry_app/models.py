from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UserAccountManager(BaseUserManager):
   def create_user(self, email, password=None, **extra_fields):
       email = self.normalize_email(email)
       user = self.model(email=email, **extra_fields)

       user.set_password(password)
       user.save()

       return user
   

class UserAccount(AbstractBaseUser, PermissionsMixin):
   INVESTOR = 'Investor'
   MITRA = 'Mitra'
   ADMIN = 'Admin'
   OPERATOR = 'Operator'
   
   USER_ROLE = [
       (INVESTOR, INVESTOR),
       (MITRA, MITRA),
       (ADMIN, ADMIN),
       (OPERATOR, OPERATOR)
   ]

   email = models.EmailField(max_length=255, unique=True)
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   role = models.CharField(max_length=10,
                           choices=USER_ROLE,
                           default=INVESTOR)
   is_active = models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)

   objects = UserAccountManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

   def get_full_name(self):
       return "{fname} {lname}".format(fname=self.first_name, lname=self.last_name)

   def get_short_name(self):
       return self.first_name

   def get_role(self):
       return self.role

   def __str__(self):
       return self.email
