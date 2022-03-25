from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session, news_api, jobs_api, user_api, news_resources, users_resource

app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
    api.add_resource(users_resource.UserListResource, '/api/v2/users')
    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
    app.run()


if __name__ == '__main__':
    main()
