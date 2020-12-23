
from django.urls import path
from .views import PostList, PostDetail, contact_form, signup



urlpatterns = [
    path('', PostList.as_view(), name="home"),
    path('detail/<slug:slug>/', PostDetail.as_view(), name="post_detail"),
    path('contact', contact_form, name="contact" ),
    path('signup', signup, name="signup" )
    
]
