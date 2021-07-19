from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    first_name = models.CharField(verbose_name='first name', max_length=255, null=False)
    last_name = models.CharField(verbose_name='last name', max_length=255, null=False)
    username = models.CharField(verbose_name='username', max_length=255, null=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name', 'username']

    class Meta:
        db_table = 'users'

        permissions = (
            ("add_user", "Can add user"),
            ("delete_user", "Can remove user"),
            ("edit_user", "Can edit user"),
            ("view_user", "Can view user"),
        )

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
