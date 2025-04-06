#Gabe Jasso
#This program parses a csv file containing movie stats data and creates a backend API to host online.

from flask import Flask, request, json
import csv

filename = 'imdb-movie-data.csv'
#filename2 = ww.txt
def movie_filter(genre):
    result = []
    with open(filename, mode ='r')as file:
        csvFile = csv.DictReader(file)
    
        for movie in csvFile:
            genres = movie['Genre'].split(",")
            if genre in genres:
                result.append(movie)
                
    return result

#def plop():
 #   with open(filename2, mode ='r')as file:
  #      mycsv = csv.DictReader(file)
   # return mycsv


app = Flask(__name__)

@app.route("/") #home page
def root():
    #print("rt") 
    genre = request.args.get('genre') 
     
    # curl these to return the functions
    if genre == "drama":
        return drama()
    elif genre == "romance":
        return romance()
    elif genre == "action":
        return action()
    elif genre == "adventure":
        return adventure()
    elif genre == "comedy":
        return comedy()
    elif genre == "biography":
        return biography()
    elif genre == "horror":
        return horror()
    elif genre == "history":
        return history()
    elif genre == "western":
        return western()
    
        
        #request.args.get(genre)
        #rt = movie_filter("Genre")
        #return json.dumps(rt)
        #return "Genre"
   

@app.route("/drama")
def drama():
    drama = request.args.get('drama')
    d = movie_filter("Drama")
    #print(len(d))
    return json.dumps(d) #return JSON

@app.route("/romance")
def romance():
    request.args.get('romance')
    r = movie_filter("Romance")
    return json.dumps(r)


@app.route("/action")
def action():
    request.args.get('action')
    ac = movie_filter("Action")
    return json.dumps(ac)

@app.route("/adventure")
def adventure():
    request.args.get('adventure')
    ad = movie_filter("Adventure")
    return json.dumps(ad)

@app.route("/comedy")
def comedy():
    request.args.get('comedy')
    c = movie_filter("Comedy")
    return json.dumps(c)

@app.route("/biography")
def biography():
    request.args.get('biography')
    bio = movie_filter("Biography")
    return json.dumps(bio)

@app.route("/horror")
def horror():
    request.args.get('horror')
    horr = movie_filter("Horror")
    return json.dumps(horr)

@app.route("/history")
def history():
    request.args.get('history')
    his = movie_filter("History")
    return json.dumps(his)

@app.route("/western")
def western():
    request.args.get('western')
    west = movie_filter("Western")
    return json.dumps(west, sort_keys = False)


#app.debug = True

app.run(host='0.0.0.0', port=8080)
