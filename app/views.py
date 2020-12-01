import json, re
from django.db.models import Q
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

#START VIEWS



#END VIEWS

def json_arr(serializer):
    return json.loads(JSONRenderer().render(serializer.data))