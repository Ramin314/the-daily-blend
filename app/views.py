from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

import feedparser

from .forms import FeedForm
from .models import Article, Feed, Topic
from .tasks import parse_rss_feed


def index(request):
    return render(request, 'app/index.html')


@login_required
def feeds(request):
    search_query = request.GET.get('search', '')

    feeds = Feed.objects.filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) | 
        Q(url__icontains=search_query)
    ).order_by('-created_at')

    paginator = Paginator(feeds, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            try:
                feed_url = form.cleaned_data['url']
                parsed_feed = feedparser.parse(feed_url)

                feed = Feed(
                    url=feed_url,
                    title=parsed_feed.feed.title,
                    description=parsed_feed.feed.description,
                    thumbnail_url=parsed_feed.feed.image.href if 'image' in parsed_feed.feed else None,
                    created_by=request.user,
                )
                feed.save()
                parse_rss_feed.delay(feed_url)

                messages.success(request, 'Feed added successfully!')
            except Exception as e:
                messages.error(request, f'Error adding feed. Please check the URL provided is a valid RSS feed.')

            return redirect('feeds')
    else:
        form = FeedForm()

    context = {
        'form': form,
        'page_obj': page_obj,
        'search_query': search_query
    }
    return render(request, 'app/feeds.html', context)


@login_required
def feed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    return render(request, 'app/feed.html', {'feed': feed})


@login_required
def stories(request):
    search_query = request.GET.get('search', '')

    articles = Article.objects.filter(
        Q(title__icontains=search_query) | 
        Q(description__icontains=search_query) | 
        Q(url__icontains=search_query)
    ).order_by('-published_at')

    paginator = Paginator(articles, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'app/stories.html', context)


@login_required
def story(request, story_id):
    return


@login_required
def topics(request):
    return


@login_required
def topic(request, topic_id):
    return
