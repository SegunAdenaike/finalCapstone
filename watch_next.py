import spacy

# Load the spacy English model
nlp = spacy.load("en_core_web_md")

# Read movie titles and their descriptions from the file
movie_titles = []
movie_descriptions = []
with open("movies.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            movie_title = line.split(":")[0].strip()
            movie_titles.append(movie_title)                    # Append titles to the movie_titles list
            movie_description = line.split(":")[1].strip()
            movie_descriptions.append(movie_description)        # Append descriptions to the movie_descriptions list


def watch_next(movie_description):
    
    # Calculate semantic similarity with movie descriptions
    similarities = []
    query_doc = nlp(movie_description)
    for description in movie_descriptions:
        description_doc = nlp(description)
        similarity = query_doc.similarity(description_doc)
        similarities.append(similarity)

    # Sort the movie descriptions based on similarity
    sorted_description = [description for score, description in sorted(zip(similarities, movie_descriptions), reverse=True)]

    # Match most similar description to title and return title
    movie_index = movie_descriptions.index(sorted_description[0])
    next_movie = movie_titles[movie_index]
    return next_movie


description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
recommendation = watch_next(description)

print(f"We strongly recommend that you watch {recommendation} next")
