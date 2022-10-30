import os


# Using OS library to call CLI commands in Python
#os.system("snscrape --jsonl --max-results 5000 --since 2022-10-01 twitter-search 'vote until:2022-10-29' > text-query-tweets.json")
os.system("snscrape --jsonl --max-results 5000 --since 2022-10-01 twitter-search \"vote midterm until:2022-10-29\" > text-query-tweets.json")
print("scrapping complete")

os.system("snscrape --jsonl --max-results 5000 --since 2022-10-01 twitter-search \"election2022 until:2022-10-29\" > election2022.json")
print("scrapping complete")