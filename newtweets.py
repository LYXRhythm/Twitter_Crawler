import pandas as pd
from nitter import Nitter
from config import search_term, mode, number, since, until, near, language
from config import to, filters, exclude, max_retries

scraper = Nitter(log_level=1, skip_instance_check=True)

is_return = True
lastSince = since
countScrapedNum = 0

while True:
    instance = scraper.get_random_instance()
    print('Scraping...')
    print('instance:', instance)
    print('lastSince:', lastSince)
    try:
        tweets_info = scraper.get_tweets(search_term, mode, number, lastSince, until, near, language,
                                     to, filters, exclude, max_retries, instance)
    except Exception as e:
        # 如果发生其他类型的异常，则执行此块
        print(f"发生了异常：{e}")

    df = pd.DataFrame(tweets_info['tweets'])
    if len(df) != 0:
        countScrapedNum = countScrapedNum + len(df)
        df.to_excel(f'{search_term}+{countScrapedNum}.xlsx', index=False)
        print('Successfully scraping!', countScrapedNum)
        print('Successfully scraping!', countScrapedNum)
        print('Successfully scraping!', countScrapedNum)
        # 更新lastSince
        last_tweet_date = tweets_info['tweets'][-1]['date']
        print("last_tweet_date 1:", last_tweet_date)
        from datetime import datetime

        last_tweet_date = datetime.strptime(last_tweet_date, "%b %d, %Y · %I:%M %p UTC").strftime("%Y-%m-%d")
        lastSince = last_tweet_date
        print("last_tweet_date 2:", last_tweet_date)

    if countScrapedNum == number:
        break

print("Scraping Finished!!!")
print("Scraping Finished!!!")
print("Scraping Finished!!!")
