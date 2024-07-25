import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Chatbot:
  def żegnam_sie():
    return "Witaj! Jestem czatbot!"

  def odpowiedz(wiadomosc):
    # Tokenizacja i niereprezentowanie wiadomosci
    tokeny = word_tokenize(wiadomosc.lower())
    tokeny = [token for token in tokeny if token not in stopwords()]

    # Generowanie odpowiedzi
    if "witaj" in tokeny:
      return "Witaj! Miło mę porozmawiać."
    elif "cześć" in tokeny:
      return "Jak mogę Ci pomóc?"
    else:
      return "Nie jestem pewien, jak mam to zrozumieć."


chatbot = Chatbot()
wiadomosc = input("Wpisz wiadomość:")
print(chatbot.odpowiedz(wiadomosc))