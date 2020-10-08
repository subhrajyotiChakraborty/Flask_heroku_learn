from flask import make_response, render_template
from flask_restful import Resource


class Artest(Resource):
    @classmethod
    def get(cls):

        headers = {"Content-Type": "text/html"}

        return make_response(
            render_template("ar.html"),
            200,
            headers
        )
