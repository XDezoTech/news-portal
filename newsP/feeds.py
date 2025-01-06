from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy,reverse
from .models import Post

class LatestPostsFeed(Feed):
    title = "Latest Posts"
    link = reverse_lazy('home-page')
    description = "Updates on the latest posts."
    


    def items(self):
        return Post.objects.filter(status=1).order_by('-date_created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


    def item_link(self, item):
        return reverse('view-post', args=[item.id]) 
