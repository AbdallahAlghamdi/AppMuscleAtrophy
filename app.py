from flask import Flask
from flask_restful import Resource, Api, reqparse
import requests
#-----
app = Flask(__name__)
api = Api(app)
#-----

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("Name", type = str, help="Error, expecting String for name of video")
video_put_args.add_argument("Views", type = int, help="Error, expecting Int for Views of video")
video_put_args.add_argument("Likes", type = int, help="Error, expecting Int for Likes of video")

#----
videos = {}

class Video(Resource):
    def get(self, video_id):
        if video_id in videos:
            return videos[video_id]
        return {"Error": "No video found"}
    def put(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == '__main__':
    app.run(debug=True)