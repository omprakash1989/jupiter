from rest_framework import serializers
from jupiter.settings import DEFAULT_SITE_DOMAIN


class BannerSerializer(serializers.Serializer):
    name = serializers.CharField()
    image_url = serializers.SerializerMethodField()
    action_url = serializers.CharField()

    def get_image_url(self, obj):
        return "%s/%s" % (DEFAULT_SITE_DOMAIN, obj.image_url)