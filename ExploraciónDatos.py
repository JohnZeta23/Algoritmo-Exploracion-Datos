import pandas as pd
import matplotlib.pyplot as plt

#1. Cargar el archivo 'netflix_title.csv'
data = pd.read_csv("netflix-titles.csv")
print(data)

#2. Visualizar los primeros 10 registros del conjunto de datos
print(data.head(10))

#3. Visualizar los últimos 15 registros del conjunto de datos
print(data.tail(15))

#4. Generar los estadísticos básicos
print(data.describe())

#5. Completar todos los datos vacíos (na) con ceros (0)
data = data.fillna(0)
print(data.isna())

#6. Generar un gráfico de tipo barras que compare películas vs series desde el 2010 hasta el 2021.

pelicula = [data['release_year'][data['release_year'] == 2010][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2011][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2012][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2013][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2014][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2015][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2016][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2017][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2018][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2019][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2020][data['type'] == 'Movie'].count(),
            data['release_year'][data['release_year'] == 2021][data['type'] == 'Movie'].count()]

serie = [data['release_year'][data['release_year'] == 2010][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2011][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2012][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2013][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2014][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2015][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2016][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2017][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2018][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2019][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2020][data['type'] == 'TV Show'].count(),
         data['release_year'][data['release_year'] == 2021][data['type'] == 'TV Show'].count()]

index = ['2010', '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

df = pd.DataFrame({'Peliculas': pelicula,
                   'Series de TV': serie}, index=index)

ax = df.plot.bar(rot=0)
plt.show()