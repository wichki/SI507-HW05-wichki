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

#Code for Part 1:Get Tweets

# def getTweets():
#     baseURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
#     params_d = {"screen_name": username, "count": num_tweets}
#     response = requests.get(baseURL, params_d, auth=auth)
#     tweets = json.loads(response.text)
#
#     total_string = ""
#     for i in list_of_tweets:
#         total_string += i["text"]
#     return total_string

# baseURL = "https://api.twitter.com/1.1/statuses/user_timeline.json"
# params_d = {"screen_name": username, "count": num_tweets}
#
# response = requests.get(baseURL, params_d, auth=auth)
#
# print(response.text)
# tweets = json.loads(response.text)
#
# f = open("tweet.json", "w")
# f.write(json.dumps(tweets, indent=1))
# f.close()


# for i in tweets:
    # print(i)

# total_string = ""
# for i in tweets:
#     total_string += i["text"]
#
# print (total_string)

string1 = "RT @umichTECH: Videos are now available from Privacy@Michigan @umsi on Jan. 30. Check them out to hear multidisciplinary conversations abou…RT @save4use: Anyone remember who the visiting prof was that taught history of the book @umsi in Winter 2006? He was really good, but I can…RT @umichTECH: ⚡️ Did you miss the Privacy@Michigan event Jan. 30? Check out the highlights and key messages from panelists in our coverage…RT @CaitlinGeier: Good article about living with and designing for colorblindness from a @umsi alum! He made some excellent points about em…Thanks to everyone who followed our live tweets today in support of #PrivacyAware! A special thank you to… https://t.co/JC06LV7Ku3RT @umichTECH: Continue the conversation about privacy by contacting privacy-interest@umich.edu and participating in the #TeachOut, Privacy…RT @umichTECH: Moderator: “What, if anything, gives you hope for privacy?” Panel: Public awareness and the fact there were 150 RSVPs for th…RT @umichTECH: Sandvig on the public good of privacy: “It’s interesting to note that privacy as a ‘setting’ or ‘preference’ [of a technolog…RT @umichTECH: Ensafi: “Privacy is very different for us [in the U.S.] than it is for people in an oppressive regime.” #UMichTalks #Privacy…RT @umichTECH: Sandvig: What worries me is that it’s hugely demobilizing and dispiriting to say ‘In a few years, there will be no privacy,…RT @umichTECH: Hans: “What really needs to happen is less policing and identification, and more public awareness. Education [about privacy…RT @umichTECH: Sandvig: “The ideal privacy policy is one I would never have to read. Ever. It’s horribly inefficient for everyone to read t…RT @umichTECH: Gautam Hans (@dispositive), Clinical Fellow @UMichLaw: “Privacy policies are more important than ever. Conventional wisdom s…RT @umichTECH: Ensafi: “We want to observe the behavior of intermediaries over time. We are designing new tools and measurements to collect…RT @umichTECH: Roya Ensafi, Research Assistant Prof. of Electrical Engineering and Computer Science @UMengineering: “Intermediaries can vio…RT @umichTECH: Christian Sandvig, Prof. of Information, Comm Studies &amp; Art and Design, @umsi: “We have pervasive leakage of data about our…RT @umichTECH: Cheney-Lippold: “The right to be left alone in order TO BE can be understood through Samuel Warren, Louis Brandeis, &amp; Thomas…RT @umichTECH: John Cheney-Lippold, Assistant Professor of American Culture, @UMichLSA: “The most terrifying page on the internet is the Fa…RT @umichTECH: @floschaub (Moderator), Assistant Professor of Information and Electrical Engineering and Computer Science @umsi: “This sess…We're back with our next panel discussion: Privacy is Freedom: Censorship, Power Asymmetries &amp; Politics featuring… https://t.co/1zRbJJ5HV2We're taking a short break but will be back with more exciting #PrivacyAware discussion at the Privacy@Michigan sym… https://t.co/dlPuLZAGwkSchaub: In the United States, we’re allowing these big tech companies to decide how your data is used on the internet.Q: Why aren’t these privacy issues getting attention here in the United States?Schaub: “In the United States we don’t have specific laws that protect privacy. You look to Europe, you have one ge… https://t.co/OsvwE0Mc7nHalderman: “We currently have very poor practices IoT but I think there’s a lot of room for the government to provi… https://t.co/nDjYNB7GAS"

word_tokens = nltk.word_tokenize(string1)
# print(word_tokens)

# word_freq = nltk.FreqDist(word_tokens)
# print(word_freq.most_common(5))
# for i in word_freq:
#     print(i)


# Stopwords
stop_words = set(stopwords.words("hw5"))
# print(stop_words)

for i in word_tokens:
    if i in stop_words:
        word_tokens.remove(i)

word_freq = nltk.FreqDist(word_tokens)

print(word_freq.most_common(5))


filtered_words = [word for word in stop_words if word not in stopwords.words('hw5')]
# print(filtered_words)


# tokenizer = word_tokens.RegexpTokenizer('[a-zA-Z]\w')
# print(tokenizer)

# print(nltk.FreqDist(total_string))
# print(total_string)
# print(tokenizer.tokenize(total_string))
# print(tokenizer)

# stopWords = set(stopwords.words("english"))
#
# print(stopwords)
# print(response.text)

#Code for Part 2:Analyze Tweets



if __name__ == "__main__":
    if not consumer_key or not consumer_secret:
        print("You need to fill in client_key and client_secret in the secret_data.py file.")
        exit()
    if not access_token or not access_secret:
        print("You need to fill in this API's specific OAuth URLs in this file.")
        exit()
