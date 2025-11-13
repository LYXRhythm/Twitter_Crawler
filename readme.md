# Twitter Crawler

1. After extracting the files, make sure `config.py`, `instance.json`, `nitter.py`, and `tweets.py` are in the same directory.
2. Modify the `config.py` file according to your needs.
3. Run `tweets.py` to start crawling.

--------------------------------------------------------------------------------
## config.py Parameter Description

term           : Keyword to search for 
mode           : 'term' to search by keyword, 'user' to search by username
number         : Number of tweets to crawl
since          : Start date in 'YYYY-MM-DD' format
until          : End date in 'YYYY-MM-DD' format
near           : Geographical location of tweets, default is anywhere
language       : Language of tweets (e.g., 'en' for English, 'es' for Spanish, 'fr' for French, etc.)
to             : Filter tweets replying to a specific user, e.g., to='github'
filters        : Additional filters (e.g., 'nativeretweets', 'media', 'videos', 'news', 'verified',
                 'native_video', 'replies', 'links', 'images', 'safe', 'quote', 'pro_video')
exclude        : Keywords to exclude
max_retries    : Maximum retry attempts if crawling fails, default=5

Example configuration:
search_term = 'openai'
mode        = 'term'
number      = 10
since       = None
until       = None
near        = None
language    = None
to          = None
filters     = None
exclude     = None
max_retries = 10

--------------------------------------------------------------------------------
## Logging Parameters

log_level          : None=no logs, 0=warning & error only, 1=info + warnings/errors (default)
skip_instance_check: Whether to skip instance selection, default=True (recommended)

Example:
log_level = 1
skip_instance_check = True

--------------------------------------------------------------------------------
## Output Fields

'link'           : Tweet URL
'text'           : Tweet content
'user'           : User info (username, account, id, avatar)
'date'           : Tweet datetime (YYYY-MM-DD HH:MM)
'is-retweet'     : Whether the tweet is a retweet
'is-pinned'      : Whether the tweet is pinned
'external-link'  : External links in the tweet
'replying-to'    : Reply target
'quoted-post'    : Quoted tweet
'stats'          : Tweet statistics (comments, retweets, likes)
'pictures'       : Images in the tweet
'videos'         : Videos in the tweet
'gifs'           : GIFs in the tweet
"""
