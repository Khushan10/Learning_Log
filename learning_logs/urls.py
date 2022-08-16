from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
	# Home page
	re_path(r'^$', views.index, name='index'),

	# Show all topics
	re_path(r'^topics/$', views.topics, name='topics'),

	# Detail page for a single topic
	re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

	# Page for adding a new topic
	re_path(r'^new_topic/$', views.new_topic, name='new_topic'),

	# Page for adding new entry
	re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

	# Page for editing entry
	re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
