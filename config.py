'''
term: search term
mode: modality to scrape the tweets. Default is 'term' which will look for tweets containing the search term. Other modes are 'hashtag' to search for a hashtag and 'user' to scrape tweets from a user profile
number: number of tweets to scrape. Default is -1 (no limit).
since: date to start scraping from, formatted as YYYY-MM-DD. Default is None
until: date to stop scraping at, formatted as YYYY-MM-DD. Default is None
near: location to search tweets from. Default is None (anywhere)
language: language of the tweets to search. Default is None (any language). The language must be specified as a 2-letter ISO 639-1 code (e.g. 'en' for English, 'es' for Spanish, 'fr' for French ...)
to: user to which the tweets are directed. Default is None (any user). For example, if you want to search for tweets directed to @github, you would set this parameter to 'github'
filters: list of filters to apply to the search. Default is None. Valid filters are: 'nativeretweets', 'media', 'videos', 'news', 'verified', 'native_video', 'replies', 'links', 'images', 'safe', 'quote', 'pro_video'
exclude: list of filters to exclude from the search. Default is None. Valid filters are the same as above
max_retries: max retries to scrape a page. Default is 5
'''
# search_term = 'jordanbpeterson'
# search_term = 'PDChinese'
search_term = 'KP_Taiwan'
mode = 'user'
number = 300
# since = None
since = '2022-03-21'
until = None
near = None
language = None
to = None
filters = None
exclude = None
max_retries = 3



'''
The valid log_levels are:
None = no logs
0 = only warning and error logs
1 = previous + informational logs (default)

The skip_instance_check parameter is used to skip the check of the Nitter instances altogether during the execution of the script. 
If you use your own instance or trust the instance you are relying on, then you can skip set it to 'True', otherwise it's better to leave it to false.
'''

log_level = 1
skip_instance_check = True