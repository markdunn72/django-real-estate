from common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F", _("Female")
    OTHER = "O", _("Other")


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    phone_number = PhoneNumberField(_("Phone Number"), null=True, blank=True)
    about_me = models.TextField(
        verbose_name=_("About Me"), default="Say something about yourself"
    )
    license = models.CharField(
        _("Real Estate License"), max_length=20, blank=True, null=True
    )
    profile_photo = models.ImageField(
        verbose_name=_("Profile Photo"), default="/profile_default.png"
    )
    gender = models.CharField(
        _("Gender"),
        max_length=1,
        choices=Gender.choices,
        default=Gender.OTHER,
    )
    country = CountryField(_("Country"), null=True, blank=True)
    city = models.CharField(
        verbose_name=_("City"), max_length=180, null=True, blank=True
    )
    is_buyer = models.BooleanField(
        verbose_name=_("Buyer"),
        default=False,
        help_text=_("Are you looking to buy a property?"),
    )
    is_seller = models.BooleanField(
        verbose_name=_("Seller"),
        default=False,
        help_text=_("Are you looking to sell a property?"),
    )
    is_agent = models.BooleanField(
        verbose_name=_("Agent"), default=False, help_text=_("Are you an agent?")
    )
    top_agent = models.BooleanField(verbose_name=_("Top Agent"), default=False)

    def __str__(self):
        return f"{self.user}"
