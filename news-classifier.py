from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
import string
from nltk.stem import PorterStemmer
from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
#nltk.download('punkt')
#nltk.download('stopwords')

news = fetch_20newsgroups(subset='all')


def stemming_tokenizer(text):
    stemmer = PorterStemmer()
    return [stemmer.stem(w) for w in word_tokenize(text)]


def train(classifier, X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
    print("world")
    print("hello")
    print(y_test)

    print("hello1")
    print(y_train)


    print("hello2")
    print(y)

    classifier.fit(X_train, y_train)
    print("Accuracy: %s" % classifier.score(X_test, y_test))
    return classifier


from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer

trial1 = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', MultinomialNB()),
])

trial5 = Pipeline([
    ('vectorizer', TfidfVectorizer(tokenizer=stemming_tokenizer,
                                   stop_words=stopwords.words('english') + list(string.punctuation))),
    ('classifier', MultinomialNB(alpha=0.05)),
])
print("hai")
print(news.target)

testingStr = 'this is gugan'
train(trial5, testingStr, news.target)
# Accuracy: 0.846349745331
