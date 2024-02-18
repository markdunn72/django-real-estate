from common.models import TimeStampedUUIDModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import Profile

User = get_user_model()


class Rating(TimeStampedUUIDModel):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        User,
        verbose_name=_("User providing the rating"),
        on_delete=models.SET_NULL,
        null=True,
    )
    agent = models.ForeignKey(
        Profile,
        verbose_name=_("Agent being rated"),
        related_name="ag",
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        choices=Range,
        verbose_name=_("Rating"),
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
        default=0,
    )
    comment = models.TextField(verbose_name=_("Comment"))

    class Meta:
        unique_together = ("rater", "agent")

    def __str__(self):
        return f"{self.agent} rated {self.rating} by {self.rater}"
