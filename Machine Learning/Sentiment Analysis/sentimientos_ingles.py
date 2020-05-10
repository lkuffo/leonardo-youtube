from nltk.sentiment.vader import SentimentIntensityAnalyzer

x = "It is a charming and beautiful product"
y = "It was a horrible experience!"
z = "I have nothing to say. Normal so far"

sid = SentimentIntensityAnalyzer()
resultados = sid.polarity_scores(z)
print (resultados)

import pandas as pd
df = pd.read_csv("sentimientos_ingles.csv")
df["sentimiento"] = df["mensaje"].apply(lambda i: sid.polarity_scores(i)['compound'])
df.to_csv('mensajes_con_sentimientos.csv')

