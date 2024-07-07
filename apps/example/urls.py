# coding: utf8
""" 
@software: PyCharm
@author: Lionel Johnson
@contact: https://fairy.host
@organization: https://github.com/FairylandFuture
@since: 2024-06-15 15:12:04 UTC+8
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.example.views.test import Test
from apps.example.views.example import ExampleViewSet
from apps.example.views.generic import PublishViewSet, AuthorViewSet
from apps.example.views.generic import PublishAPIView, AuthorAPIView
from apps.example.views.generic import AuthorDetailAPIView

router = DefaultRouter()
router.trailing_slash = ""
router.register(r"example", ExampleViewSet)
router.register(r"publish", PublishViewSet)
router.register(r"author", AuthorViewSet)

urlpatterns = [
    path(r"drf/", include(router.urls)),
    path(r"apiview", Test.as_view()),
    path(r"publish-apiview", PublishAPIView.as_view()),
    path(r"author-apiview", AuthorAPIView.as_view()),
    path(r"author-apiview/<int:pk>", AuthorDetailAPIView.as_view()),
]
