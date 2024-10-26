# Movie Recommendation System

This is a web application connected to database (mongodb) based on python as a development language to recommend movies based on custom algorithm.  

## Algorithm Overview  

The recommendation system utilizes a hybrid approach combining content-based filtering with elements of a weighted rating system

### Content-Based

The system processes the genres field of movies, which is a key characteristic in content-based filtering. By utilizing genre information to filter and recommend movies, the system narrows down  choices based on user preferences for specific genres.

### Weighted Rating Formula  

 The formula used (weighted_rating) is reminiscent of the TMDB Weighted Rating formula. It calculates a score using both the average vote (vote_average) and the number of votes (vote_count) a movie has received. The formula incorporates a constant c (the mean vote across the whole report) and m (a threshold for minimum votes required to be listed, set at the 95th percentile of the vote counts). This weighted rating is used to score movies more fairly, giving a higher weight to movies with more votes to avoid highly rated movies with very few votes skewing the results.

## API Documentation  

### Status Endpoint  

> **GET** `/`

To check the health of the app is it running or not  

Response: 'Hello World'  

### Recommend Based on Bookmarks Endpoint  

> **POST** `/genre`  

To get recommendation based on user favourite genres

**Payload**:  

```json
// Payload Example
{
  "genres": ["Horror"]
}
```

**Response**:  

```json
// Response Example
[
  {
    "id": 5462,
    "title": "It",
    "vote_count": 18568,
//...
  }
]
```  
