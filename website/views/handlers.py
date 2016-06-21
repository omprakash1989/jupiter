import datetime
import re
import json
import random
import urllib
import ast
from collections import OrderedDict
import itertools

from django.core.management import call_command
from django.http.response import Http404, HttpResponseRedirect, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from serializers import BannerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import StaticHTMLRenderer, JSONRenderer, TemplateHTMLRenderer

from website.models import Banners


class HomePage(APIView):
    def get(self, request):
        response = {"banners": [], "home_segments": {}, "new": []}
        banners = Banners.objects.filter(is_active=1, end_date__gte=datetime.datetime.now()).order_by("priority")
        banner_ser = BannerSerializer(banners, many=True, context={})
        response["banners"] = banner_ser.data

        return Response(response)
