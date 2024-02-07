# greatwave-ai

[client.jpg](https://gamein-vitation.herokuapp.com/)

## Technologies

- External API

  - openweathermap

- Frontend

  - svelte kit

- Backend

  - fastAPI

## Installation & Usage

### Installation

- Clone or download the repo. `git clone https://github.com/msvalen/greatwave-ai.git`

- Open terminal and navigate to the project folder.
- On the server folder
  - Run `pipenv shell` to enter virtual environment (or virtual environment of your choice)
  - Run `pipenv install` to install dependencies
- On the client folder
  - Run `npm i`

~ please note that for this app to work you will need an openweathermap api key in a .env file in server with the constant `OPENWEATHERMAP_KEY` ~

### Usage

- On the server folder

  - Run `pipenv shell` to enter virtual environment (or virtual environment of your choice)
  - Run in the pipenv shell terminal `pipenv run dev` to launch
  - Go to [localhost:8000](http://localhost:8000/) to view the server app

- On the client folder
  - Run in the terminal `npm run dev`
  - Go to [localhost:5173](http://localhost:5173/) to view the client app

## Endpoint routes Client app

| Route | Description                                          |
| ----- | ---------------------------------------------------- |
| /     | homepage that shows the weather in london as default |

## REST endpoint routes server API

| Route           | Data Required from front end | Description                          | Type |
| --------------- | ---------------------------- | ------------------------------------ | ---- |
| /               | not aplicable                | Homepage with description of the app | GET  |
| /location/:name | name of the location         | Return current weather information   | GET  |

### List of places with known latitude and longitude

- London
- Paris
- New York
- Newport (Wales)
- Murcia (Spain)
