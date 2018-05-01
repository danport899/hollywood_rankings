from dict_convert import convert_to_dict
from flask import Flask, render_template
import random
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import Required
from ast import literal_eval


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '2WraDkNytf/M@GE'
Bootstrap(app)

director_list = convert_to_dict("director_data.csv")
production_list = convert_to_dict('production_company_data.csv')
class SearchForm(FlaskForm):
    category = RadioField('Choose a Category', validators=[Required()],choices=[('Production Company',"Production Company"),("Director","Director")])
    name = StringField('Name:', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchForm()
    company_options_list = []
    director_options_list = []
    if form.validate_on_submit():
        category = form.category.data
        name = form.name.data
        message = ''
        if category == "Production Company":
            for company in production_list:
                if name in company["Company Name"]:
                    company_options_list.append(company)
            if len(company_options_list) == 0:
                message = 'Name not found'
                return render_template('production_search.html',message=message)
            elif len(company_options_list) == 1:
                return render_template('production.html', company=company_options_list[0])
            else:
             return render_template('production_search.html',name_list=company_options_list, search = name)
        elif category == "Director":
            for director in director_list:
                if name in director['Director Name']:
                    director_options_list.append(director)
            if len(director_options_list) == 0:
                message = 'Name not found'
                return render_template('director_search.html',message=message)
            elif len(director_options_list) == 1:
                director_info_list = convert_to_dict('movie_data.csv')
                movie_list = []
                director = director_options_list[0]
                try:
                    for info in director_info_list:
                            if director["Director Name"] in info['Director']:
                                rating_list = literal_eval(info['Ratings'])
                                imdb = "N/A"
                                rotten = "N/A"
                                metacritic = "N/A"
                                for rating in rating_list:
                                    if rating['Source'] == 'Internet Movie Database':
                                        imdb = rating['Value']
                                    elif rating['Source'] == 'Rotten Tomatoes':
                                        rotten = rating['Value']
                                    elif rating['Source'] == 'Metacritic':
                                        metacritic = rating['Value']
                                movie = {'title':info['Title'],'imdb':imdb,"rotten tomatoes":rotten,"metacritic": metacritic}
                                movie_list.append(movie)
                except SyntaxError:
                    pass
                return render_template('director.html', director=director_options_list[0], movies = movie_list)
            else:
                return     render_template('director_search.html',name_list=director_options_list, search = name)


    random_number_list = []
    for x in range(10):
        number = random.randint(1,2186)
        random_number_list.append(number)
    random_number_list2 = []
    for x in range(10):
        number = random.randint(1,564)
        random_number_list2.append(number)
    return render_template('index.html', form=form, company_options=company_options_list,director_options=director_options_list,number_list=random_number_list, number_list2=random_number_list2, directors=director_list,company=production_list, the_title="Hollywood Ranker")


@app.route('/director/<num>.html')
def director_detail(num):
    form = SearchForm()
    director_info_list = convert_to_dict('movie_data.csv')
    movie_list = []
    for director in director_list:
        if director['ID'] == num:
            director_dict = director
            break
    try:
        for info in director_info_list:
                if director_dict['Director Name'] in info['Director']:
                    rating_list = literal_eval(info['Ratings'])
                    imdb = "N/A"
                    rotten = "N/A"
                    metacritic = "N/A"
                    for rating in rating_list:
                        if rating['Source'] == 'Internet Movie Database':
                            imdb = rating['Value']
                        elif rating['Source'] == 'Rotten Tomatoes':
                            rotten = rating['Value']
                        elif rating['Source'] == 'Metacritic':
                            metacritic = rating['Value']
                    movie = {'title':info['Title'],'imdb':imdb,"rotten tomatoes":rotten,"metacritic": metacritic,'release year':info['Year'],'rated':info['Rated'],'runtime':info["Runtime"],'genre':info['Genre'],'release date':info['Released'],'website':info["Website"]}
                    movie_list.append(movie)
    except SyntaxError:
        pass
    return render_template('director.html', director=director_dict, the_title=director_dict['Director Name'], movies = movie_list, form = form )



@app.route('/production/<num>.html')
def production_detail(num):
    form = SearchForm()
    productions_info_list = convert_to_dict('production_companies.csv')
    movie_info_list = convert_to_dict('movie_data.csv')
    director_info_list = convert_to_dict('director_data.csv')
    movie_list = []
    for company in production_list:
        if company['ID'] == num:
            company_dict = company
            break
    try:
        for production in productions_info_list:
            director_list = []
            for business in literal_eval(production['Production']):
                    if business == company_dict['Company Name']:
                        film = production['Title']
                        for film_info in movie_info_list:
                            if film == film_info['Title']:
                                directors = film_info['Director']
                                break
                        for director in director_info_list:
                            if director['Director Name'] in directors:
                                director_list.append(director['Director Name'])
                        rating_list = literal_eval(production['Ratings'])
                        imdb = "N/A"
                        rotten = "N/A"
                        metacritic = "N/A"
                        for rating in rating_list:
                            if rating['Source'] == 'Internet Movie Database':
                                imdb = rating['Value']
                            elif rating['Source'] == 'Rotten Tomatoes':
                                rotten = rating['Value']
                            elif rating['Source'] == 'Metacritic':
                                metacritic = rating['Value']
                        for film in movie_info_list:
                            if production['Title'] == film['Title']:
                                info = film
                                if info["Website"] != 'N/A':
                                    website = info["Website"]
                                else:
                                    website = 'N/A'
                                break
                        movie = {'title':production['Title'],'imdb':imdb,"rotten tomatoes":rotten,"metacritic": metacritic,'release year':info['Year'],'release date':info['Released'],'rated':info['Rated'],'runtime':info["Runtime"],'genre':info['Genre'],'directors':director_list, 'website':website}
                        movie_list.append(movie)
    except SyntaxError:
        pass

    return render_template('production.html', company=company_dict, the_title=company_dict['Company Name'], movies = movie_list)



if __name__ == '__main__':
    app.run(debug=True)
