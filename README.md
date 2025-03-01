# FastAPI Water Tank API

## Project Overview
This FastAPI-based RESTful API is designed to manage IoT-enabled water tanks by allowing CRUD (Create, Read, Update, Delete) operations. The API enables users to store, retrieve, update, and delete information about tanks, including their location and GPS coordinates.

This project was created for an assignment, demonstrating an understanding of API design using FastAPI.

## API Endpoints & Expected Behavior

### GET `/tank`
- Retrieves a list of all tanks.
- Returns an empty list `[]` if no tanks exist.

### GET `/tank/{id}`
- Retrieves a specific tank by its unique `id`.
- Returns `404 Not Found` if the tank does not exist.

### POST `/tank`
- Creates a new tank entry.
- The `id` is automatically generated.
- Requires `location`, `lat`, and `long` in the request body.
- Returns **201 Created** with the newly added tank.

### PATCH `/tank/{id}`
- Updates one or more attributes (`location`, `lat`, `long`) of an existing tank.
- If no matching `id` is found, returns `404 Not Found`.
- Returns **200 OK** with the updated object.

### DELETE `/tank/{id}`
- Deletes a specific tank entry.
- If the tank exists, it is removed and a **204 No Content** response is returned.
- If the tank does not exist, returns **404 Not Found**.

## Purpose
This API was developed as part of an assignment to practice building RESTful APIs using FastAPI. The focus was on:
- Understanding HTTP methods (`GET`, `POST`, `PATCH`, `DELETE`).
- Handling UUID-based IDs.
- Implementing error handling (e.g., `404 Not Found`).
- Managing an in-memory database for prototyping.

## Two Truths and a Lie  
Guess which one is the lie.

1. I raise goats and pigs.  
2. I previously attended UTECH.  
3. I've watched every episode of Spongebob.  

Which one do you think is the lie?