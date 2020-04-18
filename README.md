# ppt_beauty-crawler
Homework of data science. Implement a crawler of ppt beauty with beautyfulSoup package.


First run:

```
python 0510713.py crawl
```
to crawl all the titles and url in 2018


Then, add different args depend on different porposes.

## Push

  ```
  python 0510713.py push {start_date} {end_date}
  ```
 output all likes and boo commands, and user id of leaving top-10 like and boo commands among the period.
  
## Popular

  ```
  python 0510713.py popular {start_date} {end_date}
  ```
  output numbers and image url of poular articles among the period.

## Keyword

  ```
  python 0510713.py keyword {keyword} {start_date} {end_date}
  ```
  output image url of articles which contains keywords among the period.
