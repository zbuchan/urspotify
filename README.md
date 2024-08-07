## URSpotifyData

URSpotifyData is a project that utilizes the Spotipy Python library to access the Spotify API. The application performs the following tasks:

1. **Accessing Spotify Data**: Using Spotipy, URSpotifyData authenticates users and retrieves their Spotify data in JSON format.
2. **Storing Data in PostgreSQL**: The retrieved data is inserted into a PostgreSQL database named `spotify` using the `psycopg2` library.
3. **Backend Data Handling**: The Flask framework is used to create a backend that accesses the database with `psycopg2` and prepares the data for the frontend.
4. **Frontend Data Retrieval**: The frontend accesses the data through a RESTful GET request.
5. **Displaying Data on the Website**: The frontend is built with Node.js, Vue.js, CSS, and Bootstrap 5, displaying the user's Spotify data on the website.

## Key Technologies

- **Backend**:
  - Python
  - Flask
  - Spotipy (Spotify API)
  - psycopg2 (PostgreSQL connection)
- **Database**:
  - PostgreSQL
- **Frontend**:
  - Node.js
  - Vue.js
  - RESTful API
  - CSS
  - Bootstrap 5

## Getting Started

### Dependencies

* Docker
* Linux

### Installing

* Download `urspotify` directory 

### Executing program

* Run this command in root directory
```
docker-compose up --build
```
* In search bar type in `localhost:80`

## Contact
Zachary Buchan - zacharyjbuchan@gmail.com
LinkedIn - www.linkedin.com/in/zach-buchan





