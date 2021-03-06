import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class wordCloudservice(Resource):
    def post(self):
        ip_json = request.get_json()
        wordFile = ip_json["Filename"]
        picFile = ip_json["ResultFilename"]
        dataset = open(wordFile, "r").read()
        def create_word_cloud(string):
            cloud = WordCloud(background_color = "white", max_words = 200, stopwords = set(STOPWORDS))
            cloud.generate(string)
            cloud.to_file(picFile)
        dataset = dataset.lower()
        create_word_cloud(dataset)
        #change path to see word cloud generated
        return "Wordcloud can be found at /path"+picFile,200

api.add_resource(wordCloudservice, '/wordCloudService')

if __name__=='__main__':
    app.run(debug=True)