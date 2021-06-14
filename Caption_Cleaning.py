import pandas as pd
import re
from nltk.corpus import stopwords
s

df1=pd.read_csv('C:\\Users\\Dhruvik\\Desktop\\mastermediacollection_sample.csv')

#Removing Images from the Caption
def remove_emoji(caption):
    caption1 = []
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)

    caption1 = emoji_pattern.sub(r'', caption)
    return caption1


#Removing Hashtag and Mension from the caption
def remove_hashtag_mension(caption):
    flag = False
    caption1 = []
    for word in caption.split():
        if word[0] == '#' or word[0] == '@':
            continue
        else:
            for ch in word:
                if ch == '#' or ch == '@':
                    flag = True
                    break
                else:
                    flag = False

            if flag != True:
                caption1.append(word)
    return caption1  # return list


#Removing StopWords from the caption
def remove_stopwords(caption):
    caption1 = []
    en_stop = set(stopwords.words('english'))
    for word in caption:
        if word in en_stop:
            continue
        else:
            caption1.append(word)
    return caption1  # return list


#remove punctuation
def remove_punct(caption12):
    punc = '''!()-[]{};:'⏳"\, <>./?$%^&*_~'''

    for ele in caption12:
        if ele in punc:
            caption12 = caption12.replace(ele, " ")
    return caption12

# final code
def final():
    caption1 = []
    all_caption_list = []
    word_frequency = {}

    for ind, cap in df1.iterrows():
        try:
            caption = cap['caption']

            caption = remove_emoji(caption)

            caption = caption.lower()

            caption = remove_punct(caption)

            caption1 = remove_hashtag_mension(caption)

            caption1 = remove_stopwords(caption1)

            for word in caption1:
                if word in word_frequency:
                    word_frequency[word] = word_frequency[word] + 1
                else:
                    word_frequency[word] = 1

            all_caption_list.append(caption1)

           # print()
           # print(ind, all_caption_list[ind])
           # print()
           # print(ind, word_frequency)
           #S print('------------------------------------')

        except Exception as e:
            print(ind, e)

if __name__ == "__main__":
    final()








