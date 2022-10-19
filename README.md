# Nollywood Movies Recommendation System
A Content-based recommendation system that recommends Nollywood movies based on user's preference

Check out the live application: [Nolly Recommends](https://nolly-recommends.herokuapp.com/)

Built with
* Python 
* Streamlit

Some of the images may not reflect the title of the movie as movie with similar names may get the poster image of more popular or ones available on the TMDB database
____
### Data Collection
Data was extracting from Wikipedia using Pandas web scraping, then data was cleaning and useful features were collected

* [List of Nigerian movies in 2016](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2016)
* [List of Nigerian movies in 2017](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2017)
* [List of Nigerian movies in 2018](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2018)
* [List of Nigerian movies in 2019](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2019)
* [List of Nigerian movies in 2020](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2020)
* [List of Nigerian movies in 2021](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2021)
* [List of Nigerian movies in 2022](https://en.wikipedia.org/wiki/List_of_Nigerian_films_of_2022)
___
### Model Building

To obtain an API key, Create an account at https://www.themoviedb.org/, then go to the account settings and click on the API tab link to fill out all of the details to apply for an API key. If you are asked for your website's URL, simply enter None because you do not have one. 
___
### Run the project
* Run `pip install -r requirements.txt` command to install necessary libraries

* Input your API key in the `app.py` or `Recommender.ipynb`

* Run `streamlit run app.py` on your terminal
