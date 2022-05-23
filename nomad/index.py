
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_page = extract_indeed_pages()

extract_indeed_jobs(last_indeed_page)


# for n in range(max_page):
#     print(f"start={n*50}")
