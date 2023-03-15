# Import "spacy" module for natural processing language
import spacy

# Declaration and assignment of variable "nlp" as spacy object, it will process the similarity between two text
nlp = spacy.load("en_core_web_md")

# Function that take a description of a movie (as a parameter) and return back the most similar movie from a list of movies
# The list of the movies is a text file that contains movies and descriptions
def watch_next(description):
    # Declaration of dictionary it will contain the title of the movies as a key and the descriptions as a value
    movies_dict = {}
    
    # Open the "movies.txt" file for only read 
    movies_file = open("movies.txt", "r")    
    # For loop that for each line in the file strip "\n" and split by ":" and assignment the keys and values to the "movies_dict" dictionary 
    for line in movies_file:
        split_line = line.strip().split(":")
        # Infinity loop that join extra split description whether the description contains ":"
        while len(split_line)> 2:
            split_line[1] = split_line[1] + ":" + split_line[2]
            split_line.pop(2)        
        movies_dict[split_line[0]] = split_line[1]
    movies_file.close()
    
    # Declaration of dictionary it will contain the title of the movies as a key and the similarity as a value
    similarity_dict = {} 
    # For loop that assigns the values to "movies_dict" dictionary
    for movie in movies_dict:
        movie_nlp = nlp(movies_dict[movie])        
        similarity_dict[movie] = description.similarity(movie_nlp)
    
    # Declaration of string variable, it will contain the title of next movie
    next_movie =''
    # Declaration of float variable, it will contain the similarity's max value
    max_simil_movie = 0.0
    # For loop that checks each value in the dictioary and finds the movie with the highest similarity
    for movie in similarity_dict:
        if similarity_dict[movie] > max_simil_movie:
            max_simil_movie = similarity_dict[movie]
            next_movie = movie    
        
    return next_movie

# Declaration and assignment of spacy object
description_movie = nlp("Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator")
# Print the movie with the highest similarity by calling the fuction "watch_next", it send one argument
print(watch_next(description_movie))