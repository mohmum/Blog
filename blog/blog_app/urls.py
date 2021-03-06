from django.conf.urls import url,include
from blog_app.models import Post
from django.views.generic import ListView,DetailView

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog_app/blog.html")),
    url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,template_name="blog_app/post.html")),

]
