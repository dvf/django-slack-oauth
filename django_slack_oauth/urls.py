# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import SlackAuthView, DefaultSuccessView, DefaultErrorView


urlpatterns = [
    url('login/', SlackAuthView.as_view(), name='slack_auth'),
    url('success/', DefaultSuccessView.as_view(), name='slack_success'),
    url('error/', DefaultErrorView.as_view(), name='slack_error')
]
