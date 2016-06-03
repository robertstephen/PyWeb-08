from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from myblog.models import Post

"""
# Guessing

class feed():

    def __call__(self, *args, **kwargs):
        request = args[1]
        response_body = ""
        # puytting a bunch of meta information into the response body

        item = self.items()

        foreach item as item:

           title = self.item_title(item)
           description = self.item_)description(item)
           link = self.item_link(item)

           #put together rss data for that item and append it to the response body
        #turn the responses body into a full response
        #return the response
           
"""

class PostFeed(Feed):
    title = "Post_RSS"
    link = "/post/feed/"
    description = "Post RSS View"

    def items(self):
        return Post.objects.order_by('-created_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('blog_detail', kwargs={'post_id': item.id})
