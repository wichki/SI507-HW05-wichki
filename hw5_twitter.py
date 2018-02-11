from requests_oauthlib import OAuth1
import json
import sys
import requests
import secret_data # file that contains OAuth credentials
import nltk # uncomment line after you install nltk
import requests
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
# nltk.download('punkt')

## SI 507 - HW
## COMMENT WITH:
## Your section day/time: Mondays, 1-2:30 pm (Deahan, 5)
## Any names of people you worked with on this assignment:

#usage should be python3 hw5_twitter.py <username> <num_tweets>

username = sys.argv[1]
num_tweets = sys.argv[2]

consumer_key = secret_data.CONSUMER_KEY
consumer_secret = secret_data.CONSUMER_SECRET
access_token = secret_data.ACCESS_KEY
access_secret = secret_data.ACCESS_SECRET

#Code for OAuth starts
url = "https://api.twitter.com/1.1/account/verify_credentials.json"
auth = OAuth1(consumer_key, consumer_secret, access_token, access_secret)
requests.get(url, auth=auth)
#Code for OAuth ends

#Write your code below:
#Code for Part 3:Caching
#Finish parts 1 and 2 and then come back to this
cache_name = "twitter_cache.json"
try:
    cache_file = open(cache_name, "r")
    cache_content = cache_file.read()
    cache_diction = json.loads(cache_content)
    cache_file.close()
except:
    cache_diction = {}

def unique_id_generator(base_url, params_diction):
    alphabetized_keys = sorted(params_diction.keys())

    lst = []
    for key in alphabetized_keys:
        lst.append("{}-{}".format(key, params_diction[key]))

    unique_id = base_url + "_".join(lst)
    return unique_id

#Code for Part 1:Get Tweets

def getTweets(username, num_tweets):
    baseURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    params_d = {"screen_name": username, "count": num_tweets}

    unique_id = unique_id_generator(baseURL, params_d)

    # Check cache
    if unique_id in cache_diction:
        print("Getting cached data...")
        return cache_diction[unique_id]
    else:
        print("Making a new request to the Twitter API...")
        response = requests.get(baseURL, params_d, auth=auth)
        cache_diction[unique_id] = json.loads(response.text)
        temporary_cache = json.dumps(cache_diction, indent=1)
        f = open(cache_name,"w")
        f.write(temporary_cache)
        f.close() # Close the open file
        return cache_diction[unique_id]

search = getTweets(username, num_tweets)

results_file = "tweets.json"
f = open(results_file, "w")
json_data = json.dumps(search, indent=2)
f.write(json_data)
f.close()

#Code for Part 2:Analyze Tweets

total_string = ""
for i in search:
    total_string += i["text"]
# print("Combined string: ", total_string)

token_words = nltk.word_tokenize(total_string)
# print(token_words)

words_we_want = []
ignore_list = ["http", "https", "RT"]

for i in token_words:
    if i[0].isalpha() and i not in ignore_list:
        words_we_want.append(i)

# print(words_we_want)

word_freq = nltk.FreqDist(words_we_want)
# print(word_freq.most_common(5))

print("\nUser: {}".format(username))
print("Tweets analyzed: {}".format(num_tweets))
print("Five most frequent/common words: ")
for k,v in word_freq.most_common(5):
    print("'{}' appears {} times".format(k,v))


if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
