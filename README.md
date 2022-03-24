# Sample

## Getting started to run the application

## build with no cache
docker-compose build --no-cache

## start the services
docker-compose up

## frontend service URL
React:            
http://localhost:3000

## backend services URL
Django:            
http://localhost:8000
POST BOARD
http://localhost:8000/api/boardpost

## (troubleshooting) list the services
docker-compose ps

## (troubleshooting) if out of memory prune
docker system prune -af

# (troubleshooting) list the containers
docker ps

## stop services
docker compose stop

## down services
docker compose down

## backend
Backend is serviced by Django (Python) with libraries such as Pandas and Django Rest Framework
Post your board results to this end point
http://localhost:8000/api/boardpost

##Front end
Front end is serviced by React JS with libraries such as react-select-2 and bootstrap table, and calling the backend above.
http://localhost:3000/

##to install an npm package
docker-compose exec frontend npm install --save react-json-view

## unit test can be run

docker compose exec backend python manage.py test main_api

## Sample JsonResponse

{
    "type": "resistor",
    "description": "abc",
    "tolerance" : 5,
    "stability": 6,
    "reliability": 5,
    "voltage_coefficient": 8,
    "noise": 10,
    "temperature_rating" : 9,
    "thermal_resistance": 7,
    "temperature_coefficient_of_resistance": 9
}

{
    "type": "capacitor",
    "nominal_capacitance": 0.02,
    "working_voltage": 200.0,
    "tolerance": 0.05,
    "working_temperature": 0.0,
    "temperature_coefficient": 0.8
}

{
    "type": "transistor",
    "current_gain": 0.02,
    "collector_emitter_voltage": 200.0,
    "emitter_base_voltage": 0.05,
    "collector_current": 0.0
}


## Screen Shots of Results (UI)

![Alt text](sample_pics/UI4.png?raw=true "List")

![Alt text](sample_pics/UI5.png?raw=true "List")

## Screen Shots of Results (BackEnd)

![Alt text](sample_pics/PM1.png?raw=true "List")

![Alt text](sample_pics/PM2.png?raw=true "List")

![Alt text](sample_pics/PM3.png?raw=true "List")
