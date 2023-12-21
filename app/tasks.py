import feedparser
from celery import shared_task
from django.utils import timezone
from .models import Article, Feed, Topic

@shared_task
def parse_rss_feed(feed_url):
    feed = Feed.objects.get(url=feed_url)
    parsed_feed = feedparser.parse(feed_url)

    for entry in parsed_feed.entries:
        article, created = Article.objects.get_or_create(
            url=entry.link,
            defaults={
                'feed': feed,
                'title': entry.title,
                'description': entry.description,
                # Assume entry.published_parsed is a struct_time
                'published_at': timezone.make_aware(timezone.datetime(*entry.published_parsed[:6])),
                'thumbnail_url': entry.media_thumbnail[0]['url'] if 'media_thumbnail' in entry else None
            }
        )

        # If topics are included in the feed, add them to the article
        if created and 'tags' in entry:
            for tag in entry.tags:
                topic, _ = Topic.objects.get_or_create(name=tag.term)
                article.topics.add(topic)
