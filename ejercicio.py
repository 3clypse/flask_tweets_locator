#!/usr/bin/python2
# -*- coding: utf-8 -*

__author__ = 'David Ureba'

from flask            import Flask, render_template
from flask_googlemaps import GoogleMaps, Map
import twitterAPI

twitter_api = twitterAPI.oauth_login() 
app         = Flask(__name__)
GoogleMaps(app)

@app.route("/")
def map():
    sndmap = Map(
        identifier="sndmap", 
        lat=40.45,
        lng=3.75,  
        style="height:100%;width:50%;top:0;left:0;position:absolute;z-index:200;", 
        zoom=4
    )
    return render_template('view.html', sndmap=sndmap, tweets='')

@app.route("/<query>/<coord1>/<coord2>")
def mapview(query,coord1,coord2):

    coordList = {}
    tweets    = []

    container = twitter_api.search.tweets(q=query,count=10,geocode="" + coord1 + ',' + coord2 + ',100km' + "")

    for result in container["statuses"]:
        if result['user'] and result['text'] and result['geo'] and result['entities']['urls']:
            img  = result['user']['profile_image_url_https']
            url  = result['entities']['urls'][0]['url']
            item = dict(img=img, text=result['text'], url=url)
            tweets.append( item )

            lat   = result["geo"]["coordinates"][0]
            lon   = result["geo"]["coordinates"][1]
            coordList[img] = [(lat, lon)]

    sndmap = Map(
        identifier="sndmap", 
        lat=coord1, 
        lng=coord2,
        markers=coordList,
        style="height:100%;width:50%;top:0;left:0;position:absolute;z-index:200;", 
        zoom=8
    )
    return render_template('view.html', sndmap=sndmap, tweets=tweets)

if __name__ == "__main__":
    app.run(debug=False)
