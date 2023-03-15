# Import spacy a module for Natural Processing Language
import spacy

# Declaration of spacy object that call a method that load "en_core_web_md"
nlp = spacy.load("en_core_web_md")
#nlp = spacy.load("en_core_web_sm")

# Function that take a string whith words as parameter and print the similarity between them 
def check_similarity(words_string):
    tokens = nlp(words_string)
    for token1 in tokens:
        for token2 in tokens:
            if token1!= token2:
                print(token1.text, token2.text, token1.similarity(token2)) 



check_similarity("cat monkey banana")
# cat and monkey have quite high similarity I supose because both of them are animal
# banana and monkey have higher similarity than banana and cat because the monkeys eat bananas  
# cat and banana have the smallest similarity between the words

check_similarity("car bike petrol")
# car and bike have the highest similarity, I think beacause are both means of trasportation
# petrol has higher similarity with car that bike, because petrol is one of car's fuel
# Petrol and bikes have low similarity, but this may be because using bikes reduces the need for petrol

# Between the two models, I notice that "en_core_web_md" is more accurate than "en_core_web_sm",
# when I run the same program sometime the similarity difference between them is quite big