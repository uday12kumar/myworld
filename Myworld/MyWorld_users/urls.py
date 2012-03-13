from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('MyWorld_users.views',
    # Examples:
    url(r'^user_authentication', 'user_authentication', name='user_authentication'),
    url(r'^register', 'add_user', name='add_user'),
)
