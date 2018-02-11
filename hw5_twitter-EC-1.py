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

username1 = sys.argv[1]
username2 = sys.argv[2]
num_tweets = sys.argv[3]

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

    unique_id = base_url + "_".join(lst) # combine the baseurl and the formatted pairs of keys and values
    return unique_id # return a unique id of the request

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

search1 = getTweets(username1, num_tweets)
search2 = getTweets(username2, num_tweets)

# print(search1)
# print(search2)

results_file = "tweets.json"
f = open(results_file, "w")
json_data1 = json.dumps(search1, indent=2)
json_data2 = json.dumps(search2, indent=2)
f.write(json_data1)
f.write(json_data2)
f.close()

total_string1 = ""
for i in search1:
    total_string1 += i["text"]

total_string2 = ""
for i in search2:
    total_string2 += i["text"]


token_words1 = nltk.word_tokenize(total_string1)
token_words2 = nltk.word_tokenize(total_string2)

words_we_want1 = []
words_we_want2 = []
ignore_list = ["http", "https", "RT"]

for i in token_words1:
    if i[0].isalpha() and i not in ignore_list:
        words_we_want1.append(i)

for i in token_words2:
    if i[0].isalpha() and i not in ignore_list:
        words_we_want2.append(i)

word_freq1 = nltk.FreqDist(words_we_want1)
word_freq2 = nltk.FreqDist(words_we_want2)
# print(word_freq.most_common(5))

print(word_freq1.most_common(5))
print(word_freq2.most_common(5))

comp1 = {}
comp2 = {}

print("\nHere are the five most common words for {}: ".format(username1))
for k,v in word_freq1.most_common(5):
    comp1[k] = v
    print("'{}' appears {} times".format(k,v))

print("\nHere are the five most common words for {}: ".format(username2))
for k,v in word_freq2.most_common(5):
    comp2[k] = v
    print("'{}' appears {} times".format(k,v))

print("\nHere are the more frequent unique words: \n")

# holder = {}
# for a,b in word_freq1.most_common(5):
#     if holder[a] == b:
#         del holder[a]
#     else:
#         holder[a] = b

print(comp1.keys())
print(comp2)

# print(comp1.keys()-comp2.keys())
# print(comp1 == comp2)

sortedd = {}

for k in comp1:
    if comp1[k] >= comp2[k]:
        sortedd[k] = v
    else:
        pass

# print(sortedd)
# print("\nHere are the five most common words shared by {} and {}: ".format(username1, username2))
# for k,v in word_freq2.most_common(5):
#     print("'{}' appears {} times".format(k,v))
# print("\n")

shared_words = {}

for k,v in word_freq1.most_common(10):
    try:
        shared_words[k] += v
    except:
        shared_words[k] = v

for k,v in word_freq2.most_common(10):
    try:
        shared_words[k] += v
    except:
        shared_words[k] = v

# print(shared_words)
sorted_shared_words = sorted(shared_words.items(), key=lambda x: x[1], reverse=True)
# print(sorted_shared_words)

# print("\nHere is a list of sorted shared words: ")
# for k,v in sorted_shared_words[:5]:
#     print("'{}' appears {} times".format(k,v))

# Code for Part 2:Analyze Tweets

if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
