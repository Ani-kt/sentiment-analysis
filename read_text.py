#Date-4th Jan,2020
#Syntax : maketrans(str1, str2, str3)
# str1 : Specifies the list of characters that need to be replaced.
# str2 : Specifies the list of characters with which the characters need to be replaced.
# str3 : Specifies the list of characters that needs to be deleted.
# Returns : Returns the translation table which specifies the conversions that can be used by translate()
# Syntax : translate(table, delstr)
# table : Translate mapping specified to perform translations.
# delstr : The delete string can be specified as optional argument is not mentioned in table.
# Returns : Returns the argument string after performing the translations using the translation table.
import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import matplotlib.pyplot as plt
text=open("file.text",encoding="utf-8").read()
lower_case=text.lower()
cleaned_text=lower_case.translate(lower_case.maketrans("","",string.punctuation))
#tokenized_word=cleaned_text.split()
tokenized_word=word_tokenize(cleaned_text,"english")
# stop_words=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
#               "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
#               "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
#               "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
#               "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
#               "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
#               "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
#               "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
#               "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
#               "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_word=[]
for word in tokenized_word:
    if word not in stopwords.words("english"):
        final_word.append(word)
emotion_list=[]          
with open("emotion.txt","r") as file:
    for line in file:
        clear_line=line.replace("\n","").replace(",","").replace("'","").strip()  
        word,emotion=clear_line.split(":")
        if word in final_word:
            emotion_list.append(emotion) 
final_dict=Counter(emotion_list)                        
print(final_dict)
def sentiment_analysis(cleaned_text):
    score=SentimentIntensityAnalyzer().polarity_scores(cleaned_text)
    print(score)
    neg=score["neg"]
    pos=score["pos"]
    if pos>neg:
        print("Positive Vibe")
    elif neg>pos:
        print("Negative Vibe")
    else:
        print("Neutral")
sentiment_analysis(cleaned_text)                 
# fig,axl=plt.subplots()
# axl.bar(final_dict.keys,final_dict.values)
# fig.autofmt_xdate()
# plt.savefig("graph.png")
# plt.show() 
