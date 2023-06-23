# Movie Recommendation System using Spacy

This project provides a movie recommendation system based on semantic similarity using the Spacy natural language processing library. It takes movie descriptions as input and suggests the most relevant movie title to watch next.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Installation

To use this project locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/SegunAdenaike/finalCapstone.git
   ```

2. Change to the project directory:

   ```shell
   cd finalCapstone
   ```

3. Install the required dependencies. It is recommended to use a virtual environment:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. Prepare the movie data file:

   - Create a file named `movies.txt` in the project directory.
   - Each line should contain a movie title followed by a colon ':' and the movie description.
   - Example format:
     ```
     Movie Title 1: Movie description 1
     Movie Title 2: Movie description 2
     ...
     ```

5. Run the movie recommendation script:

   ```shell
   python watch_next.py
   ```

## Usage

1. Open the `watch_next.py` file.

2. Edit the file to modify the `description` variable with your own movie description.

   ```python
   description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
   ```

3. Save the file and run it:

   ```shell
   python watch_next.py
   ```

4. The script will display the recommended movie title based on the provided description.

   ```
   We strongly recommend that you watch [Recommended Movie Title] next.
   ```

5. Repeat steps 2-4 with different movie descriptions to get new recommendations.

## Credits

This project was created by [Olusegun Adenaike](https://github.com/SegunAdenaike).

If you have any questions or suggestions, please feel free to contact me.# finalCapstone
