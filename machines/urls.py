from django.conf.urls import url

from .views import *



urlpatterns=[
    
    url(r'^$',index, name='index'),
    url(r'^Monitor-tb.html$',monitor_tb, name='monitor_tb'),
    url(r'^CPU-tb.html$',CPU_tb, name='CPU_tb'),
    url(r'^Keyboard-tb.html$',keyboard_tb, name='keyboard_tb'),
    url(r'^Mouse-tb.html$',mouse_tb, name='mouse_tb'),
    
    url(r'^display_monitor$',display_monitor,name="display_monitor"),
    url(r'^display_CPU$',display_CPU,name="display_CPU"),
    url(r'^display_keyboard$',display_keyboard,name="display_keyboard"),
    url(r'^display_mouse$',display_mouse,name="display_mouse"),
    url(r'^add_monitor$',add_monitor,name="add_monitor"),
    url(r'^add_cpu$',add_cpu,name="add_cpu"),
    url(r'^add_keyboard$',add_keyboard,name="add_keyboard"),
    url(r'^add_mouse$',add_mouse,name="add_mouse"),
    
    url(r'^edit_monitor/(?P<pk>\d+)$',edit_monitor,name="edit_monitor"),
    url(r'^edit_keyboard/(?P<pk>\d+)$',edit_keyboard,name="edit_keyboard"),
    url(r'^edit_cpu/(?P<pk>\d+)$',edit_cpu,name="edit_cpu"),
    url(r'^edit_mouse/(?P<pk>\d+)$',edit_mouse,name="edit_mouse"),
    url(r'^delete_monitor/(?P<pk>\d+)$',delete_monitor,name="delete_monitor"),
    url(r'^delete_cpu/(?P<pk>\d+)$',delete_cpu,name="delete_cpu"),
    url(r'^delete_keyboard/(?P<pk>\d+)$',delete_keyboard,name="delete_keyboard"),
    url(r'^delete_mouse/(?P<pk>\d+)$',delete_mouse,name="delete_mouse")
]