from rest_framework import serializers
from jupiter.settings import DEFAULT_SITE_DOMAIN


class BannerSerializer(serializers.Serializer):
    name = serializers.CharField()
    image_url = serializers.SerializerMethodField()
    action_url = serializers.CharField()

    def get_image_url(self, obj):
        return "%s/%s" % (DEFAULT_SITE_DOMAIN, obj.image_url)


class ProductListingSerializer(serializers.Serializer):
    name = serializers.CharField()
    title = serializers.CharField()
    product_info = serializers.CharField()
    product_description = serializers.CharField()
    price_effective = serializers.FloatField()
    price_marked = serializers.FloatField()
    discount = serializers.FloatField()
    image_url = serializers.SerializerMethodField()
    action_url = serializers.SerializerMethodField()

    def get_image_url(self, obj):
        return "%s%s%s" % (DEFAULT_SITE_DOMAIN, 'media/', obj.image_url)

    def get_action_url(self, obj):
        return "%s%s" % (DEFAULT_SITE_DOMAIN, obj.image_url)