import webapp2

class Index(webapp2.RequestHandler):

    def getRandomMovie(self):
        import random
        # TODO: make a list with at least 5 movie titles
        list=["Terminator2","The Grudge","Judgement Day","The Croods","Expendables","Happy Gilmore","Gravity"]
        # TODO: randomly choose one of the movies, and return it

        b=len(list)
        random=random.randint(0,b-1)
        return list[random]



    def get(self):
        # choose a movie by invoking our new function
        movie = self.getRandomMovie()
        movie1 = self.getRandomMovie()
        # build the response string
        content = "<h1>Movie of the Day</h1>"
        content += "<p>" + movie + "</p>"

        # TODO: pick a different random movie, and display it under
        # the heading "<h1>Tommorrow's Movie</h1>"

        content1 = "<h1>Tomorrow's Movie</h1>"
        content1 += "<p>" + movie1 + "</p>"
        self.response.write(content)
        self.response.write(content1)
app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
