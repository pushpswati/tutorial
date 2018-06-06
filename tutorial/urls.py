from django.conf.urls import url
from snippets import views
from django.conf.urls import url, include

urlpatterns = [
    
     url(r'^', include('snippets.urls')),
]
