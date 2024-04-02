import pandas as pd
from nitter import Nitter
from config import search_term, mode, number, since, until, near, language
from config import to, filters, exclude, max_retries

scraper = Nitter(log_level=1, skip_instance_check=True)

is_return = True

while is_return:
    instance = scraper.get_random_instance()
    print('Scraping...')
    print('instance:', instance)
    tweets_info = scraper.get_tweets(search_term, mode, number, since, until, near, language,
                                     to, filters, exclude, max_retries, instance)

    '''
    todo: 
        如果爬取scraper.get_tweets中断重新根据爬取到的since进行装载，
        根据第四列 date列
        Mar 14, 2024 · 6:29 AM UTC
        Mar 6, 2024 · 10:42 PM UTC
        Mar 6, 2024 · 10:32 PM UTC
        将第四列 date列的最后的date作为scraper.get_tweets的since中
        :param since: date to start scraping from.
        修改excel为追加加入,每次都爬取到的数据append到excel中
    '''

    df = pd.DataFrame(tweets_info['tweets'])
    
    # todo：结束标注应该为多次累加爬取数量df的行数和number行数相等
    if len(df) != 0:
        df.to_excel(f'{search_term}.xlsx', index=False)
        is_return = False
        print('Successfully scraping!')

print("Scraping Finished!!!")
print("Scraping Finished!!!")
print("Scraping Finished!!!")