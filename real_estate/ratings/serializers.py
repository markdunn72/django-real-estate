from ratings.models import Rating
from rest_framework import serializers


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.StringRelatedField(read_only=True)
    agent = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Rating
        exclude = ("updated_at", "pkid")


