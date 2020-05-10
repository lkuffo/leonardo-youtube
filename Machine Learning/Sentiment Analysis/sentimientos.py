from classifier import SentimentClassifier

clf = SentimentClassifier()

x = "Esta muy buena esa pelicula"

y = "Que horrible comida!!!"

z = "Tuve una experiencia netural"

#sentimiento = clf.predict(x)
#sentimiento = clf.predict(y)
sentimiento = clf.predict(z)

print(sentimiento)