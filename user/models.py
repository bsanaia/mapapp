from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('იმეილი აუცილებელია')
        account = self.model(email=self.normalize_email(email))
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self, email, password, **kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_staff = True
        account.is_admin = True
        account.is_active = True
        account.is_superuser = True
        account.save()
        return account


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
    user Model
    """

    email = models.EmailField(_('email'), blank=True, unique=True,
                              help_text=_('150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                              error_messages={'unique': _("user exists"), })

    username = models.CharField(_("username"), blank=True, null=True, max_length=255)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    address = models.TextField('address', max_length=255, blank=True)
    country = models.CharField('Country', max_length=30, blank=True)
    phone = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("phone number"))

    # DJANGO ADMIN REQUIRED FIELDS
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def get_short_name(self):
        return self.first_name

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

