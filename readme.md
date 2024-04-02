# 使用方法
1. 将文件解压后使`config.py`,`instance.json`,`nitter.py`,`tweets.py`在同一目录下
2. 根据需要修改`config.py`文件
3. 运行`tweets.py`文件即可

# config.py参数说明
- term: 关键词
- mode: `'term'`根据关键词查找    `'user'`根据用户名查找
- number: 爬取推文个数
- since: 起始日期，格式为`YYYY-MM-DD`.
- until: 终止日期`YYYY-MM-DD`. 
- near: 推文地区，默认为任何地方
- language:语言(e.g. 'en' for English, 'es' for Spanish, 'fr' for French ...)
- to: 引用，如果引用@github，将其设置为`to = 'github'`
- filters: 筛选，例如：'nativeretweets', 'media', 'videos', 'news', 'verified', 'native_video', 'replies', 'links', 'images', 'safe', 'quote', 'pro_video'
- exclude: 反向筛选，不包括哪些关键词
- max_retries: （爬取失败时会重试）最大尝试次数，默认为5

- 例如
````python
search_term = 'openai'
mode = 'term'
number = 10
since = None
until = None
near = None
language = None
to = None
filters = None
exclude = None
max_retries = 10
````


- valid log_levels
`None = no logs`
`0 = only warning and error logs`
`1 = previous + informational logs (default)`

- skip_instance_check: 是否跳过选择实例，默认为跳过，建议跳过，否则会很慢

- 例如
````python
log_level = 1
skip_instance_check = True
````

# 输出结果
`'link'` 推文链接
`'text'` 推文内容
`'user'`用户信息，包含用户名、账户、id、头像
`'date'` 推文日期，包括年月日，具体到分钟
`'is-retweet'` 是否转发
`'is-pinned'` 是否置顶
`'external-link'` 外部链接
`'replying-to'` 回复
`'quoted-post'` 引用推文
`'stats'` 推文状态，包括评论、转发，喜欢
`'pictures'`图片（如果推文内容有图）
`'videos'`视频（如果推文内容有视频）
`'gifs'`动态图（如果推文内容有动态图）