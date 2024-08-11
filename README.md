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
* Spotify

### Installing

* Download `urspotify` directory 

### Executing program
* Obtain Spotify client id and client password from https://developer.spotify.com/
  ```
  1. Login to account
  
  2. Click on name in top right and click on dashboard
  
  3. Click on Create app on the top right
  
  4. Create name
  
  5. Make the Redirect URI to http://localhost:8080/callback
  
  6. Click on save
  
  7. Press the settings buttion on the top right in the project you just created
  
  8. Client ID is now visible
  
  9. Press View client secret to also obtain the client secret
  
  10. Copy and paste this information into the right location in the .env file
  ```
  


* Create .env file in root directory
  ```
  pg_user= # Make own username for Postgreql database
  pg_password= # Make own password for Postgreql database
  DB= spotify
  pg_host= # Postgresql database name(container name)
  URI= http://localhost:8080/callback
  client_id= # Spotify client id
  client_secret= # Spotify client secret 
  ```

* Run this command in root directory
```
docker-compose up --build
```
* In search bar type in `localhost:80`

## Contact
Zachary Buchan - zacharyjbuchan@gmail.com
LinkedIn - www.linkedin.com/in/zach-buchan





