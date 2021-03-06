# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *
# from django.conf import settings

urlpatterns = patterns('crims.auction.views',
                       url(r'^$', 'index', name='auction', kwargs={'tab': 'auction', 'page_no': 1}),
                       url(r'^(?P<page_no>\d+)/$', 'index', name='auction', kwargs={'tab': 'auction'}),
                       url(r'^bidding/$', 'index', name='auction_bidding', kwargs={'tab': 'bidding', 'page_no': 1}),
                       url(r'^bidding/(?P<page_no>\d+)/$', 'index', name='auction_bidding', kwargs={'tab': 'bidding'}),
                       url(r'^bidded/$', 'index', name='auction_bidded', kwargs={'tab': 'bidded', 'page_no': 1}),
                       url(r'^bidded/(?P<page_no>\d+)/$', 'index', name='auction_bidded', kwargs={'tab': 'bidded'}),
                       url(r'^watch/$', 'index', name='auction_watch', kwargs={'tab': 'watch', 'page_no': 1}),
                       url(r'^watch/(?P<page_no>\d+)/$', 'index', name='auction_watch', kwargs={'tab': 'watch'}),

                       url(r'^show/(?P<auction_id>\d+)/$', 'details', name='auction_details'),
                       url(r'^bid/$', 'bid', name='auction_bid'),
                       url(r'^sell/(?P<item_type>\w+)/(?P<item_id>\d+)/$', 'sell', name='auction_sell'),
                       )
