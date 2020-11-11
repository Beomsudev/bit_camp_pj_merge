import logging
from flask import Blueprint
from flask_restful import Api
from com_dayoung_api.usr.resource.user import User, Users, Delete
from com_dayoung_api.usr.resource.auth import Auth
from com_dayoung_api.usr.resource.access import Access

from com_dayoung_api.cop.act.resource.actor import Actor, Actors, AddActor

from com_dayoung_api.cop.mov.resource.movie import Movie, Movies
from com_dayoung_api.cop.mov.resource.search import MovieSearch
from com_dayoung_api.cop.mov.resource.movie_del import MovieDel
from com_dayoung_api.cop.mov.resource.recommendation import MovieRecommendation

from com_dayoung_api.cop.rat.resource.rating import Rating, Ratings
from com_dayoung_api.cop.rat.resource.search import RatingSearch
from com_dayoung_api.cop.rat.resource.rating_del import RatingDel

from com_dayoung_api.cop.rev.resource.review import Review, Reviews
from com_dayoung_api.cop.rev.resource.my_review import MyReview
from com_dayoung_api.cop.rev.resource.score import ReviewScore
from com_dayoung_api.cop.rev.resource.search import ReviewSearch
from com_dayoung_api.cop.rev.resource.emotion import ReviewEmotion

############################## HOME ##############################
from com_dayoung_api.cop.hom.resource.home import Home
home = Blueprint('home', __name__, url_prefix='/api')
api = Api(home)
api.add_resource(Home, '/api')
############################## HOME ##############################

############################## USER ##############################
user = Blueprint('user', __name__, url_prefix='/api/user')
users = Blueprint('users', __name__, url_prefix='/api/users')
auth = Blueprint('auth', __name__, url_prefix='/api/auth')
access = Blueprint('access', __name__, url_prefix='/api/access')

api = Api(user)
api = Api(users)
api = Api(auth)
api = Api(access)
############################## USER ##############################

############################## ACTOR ##############################
actor = Blueprint('actor', __name__, url_prefix='/api/actor')
actors = Blueprint('actors', __name__, url_prefix='/api/actors')
delete = Blueprint('delete', __name__, url_prefix='/api/delete')
addActor = Blueprint('addActor', __name__, url_prefix='/api/addActor')

api = Api(actor)
api = Api(actors)
api = Api(delete)
api = Api(addActor)
############################## ACTOR ##############################

############################## MOVIE ##############################
movie = Blueprint('movie', __name__, url_prefix='/api/movie')
movies = Blueprint('movies', __name__, url_prefix='/api/movies')
movie_search = Blueprint('movie_search', __name__, url_prefix='/api/movie-search')
movie_del = Blueprint('movie_del', __name__, url_prefix='/api/movie-del')
movie_recommendation = Blueprint('movie_recommendation', __name__, url_prefix='/api/movie-recommendation')

api = Api(movie)
api = Api(movies)
api = Api(movie_search)
api = Api(movie_del)
api = Api(movie_recommendation)
############################## MOVIE ##############################

############################## RATING ##############################
rating = Blueprint('rating', __name__, url_prefix='/api/rating')
ratings = Blueprint('ratings', __name__, url_prefix='/api/ratings')
rating_search = Blueprint('rating_search', __name__, url_prefix='/api/rating-search')
rating_del = Blueprint('rating_del', __name__, url_prefix='/api/rating-del')

api = Api(rating)
api = Api(ratings)
api = Api(rating_search)
api = Api(rating_del)
############################## RATING ##############################

############################## REVIEW ##############################
review = Blueprint('review', __name__, url_prefix='/api/review')
reviews = Blueprint('reviews', __name__, url_prefix='/api/reviews')
myreview = Blueprint('myreview', __name__, url_prefix='/api/myreview')
reviewscore = Blueprint('reviewscore', __name__, url_prefix='/api/reviewscore')
reviewsearch = Blueprint('reviewsearch', __name__, url_prefix='/api/reviewsearch')
reviewemotion = Blueprint('reviewemotion', __name__, url_prefix='/api/reviewemotion')

api = Api(review)
api = Api(reviews)
api = Api(myreview)
api = Api(reviewscore)
api = Api(reviewsearch)
api = Api(reviewemotion)
############################## REVIEW ##############################

def initialize_routes(api):
    api.add_resource(Home, '/api')
############################## USER ##############################
    api.add_resource(User, '/api/user/<string:id>')
    api.add_resource(Users, '/api/users')
    api.add_resource(Auth, '/api/auth')
    api.add_resource(Access, '/api/access')
############################## USER ##############################

############################## ACTOR ##############################
    api.add_resource(Actor, '/api/actor/<string:id>')
    api.add_resource(AddActor, '/api/addActor/<string:name>')
    api.add_resource(Delete, '/api/delete/<string:id>')
    api.add_resource(Actors, '/api/actors')    
############################## ACTOR ##############################

############################## MOVIE ##############################
    api.add_resource(Movie, '/api/movie')
    api.add_resource(Movies, '/api/movies')
    api.add_resource(MovieSearch, '/api/movie-search/<string:title>')
    api.add_resource(MovieDel, '/api/movie-del')
    api.add_resource(MovieRecommendation, '/api/movie-recommendation/<string:title_naver_eng>')
############################## MOVIE ##############################

############################## RATING ##############################
    api.add_resource(Rating, '/api/rating')
    api.add_resource(Ratings, '/api/ratings')
    api.add_resource(RatingSearch, '/api/rating-search/<string:ratingid>')
    api.add_resource(RatingDel, '/api/rating-del')
############################## RATING ##############################

############################## REVIEW ##############################
    api.add_resource(Review, '/api/review', '/api/review/<string:id>')
    api.add_resource(Reviews, '/api/reviews')
    api.add_resource(MyReview, '/api/myreview/<string:user_id>')
    api.add_resource(ReviewScore, '/api/reviewscore')
    api.add_resource(ReviewSearch, '/api/reviewsearch<string:movie_title>')
    api.add_resource(ReviewEmotion, '/api/reviewemotion/<string:content>')
############################## REVIEW ##############################