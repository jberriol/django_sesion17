from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
class BlogListView(ListView):
    model = Post
    template_name = "home.html"