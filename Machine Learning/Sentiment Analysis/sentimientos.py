# pip install scikit-learn
# pip install sentiment-analysis-spanish

# Importar la libreria
from sentiment_analysis_spanish import sentiment_analysis

# Instanciar el clasificador, esto puede demorar un poco
clf = sentiment_analysis.SentimentAnalysisSpanish()

x = "Esta muy buena esa pelicula"

y = "Que horrible comida!!!"

z = "Tuve una experiencia netural"

#sentimiento = clf.predict(x)
#sentimiento = clf.predict(y)
sentimiento = clf.predict(z)

print(sentimiento)