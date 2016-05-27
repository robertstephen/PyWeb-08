from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from myblog.models import Post

class PostFeed(Feed):
    title = "Post_RSS"
    link = "/postrss/"
    description = "Post RSS View"

    def items(self):
        return Post.objects.order_by(self.created_date)
# [:5]

    def item_title(self):
        return self.title

    def item_description(self):
        return self.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self):
        return reverse('blog_detail', kwargs={'post_id': self.id})  