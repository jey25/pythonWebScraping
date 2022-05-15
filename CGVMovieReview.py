from selenium import webdriver
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


# 브라우저를 띄우지 않는 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


def get_movie_reviews(url, page_num=10):

    wd = webdriver.Chrome(
        'C:\chromedriver\chromedriver', options=chrome_options)
    wd.get(url)

    writer_list = []
    review_list = []
    date_list = []

    for page_no in range(1, page_num+1):
        try:
            page_ul = wd.find_element_by_id('paging_point')
            page_a = page_ul.find_element_by_link_text(str(page_no))
            page_a.click()
            time.sleep(1)

            writers = wd.find_elements_by_class_name('writer-name')
            writer_list += [writer.text for writer in writers]

            reviews = wd.find_elements_by_class_name('box-comment')
            review_list += [review.text for review in reviews]

            dates = wd.find_elements_by_class_name('day')
            date_list += [date.text for date in dates]

            if page_no % 10 == 0:
                next_btn = page_ul.find_element_by_class_name(
                    'btn-paging next')
                next_btn.click()
                time.sleep(1)

        except NoSuchElementException:
            break

    movie_review_df = pd.DataFrame(
        {"Writer": writer_list, "Review": review_list, "Date": date_list})

    return movie_review_df


movie_review_df = get_movie_reviews(
    'http://www.cgv.co.kr/movies/detail-view/?midx=85715#1', 12)
movie_review_df
