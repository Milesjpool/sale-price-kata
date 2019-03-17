# Sale Price Kata

A backend solution to a sale-price API kata.

Objective - given a listing of property sale prices, and their coordinates,
provide an application which serves this data in a visual manner.

## Features

## Environment setup
- Install any missing requirements (see below)
- Install python test dependencies    
`make installTestRequirements`
- Run tests (unit + functional)
`make test`
- Full build (includes full test)
`make build`
- Start app (includes full build)  
`make start`

## API
- Service status available at `http://localhost:5000/status`
- Data available at `http://localhost:5000/sale-prices`
    - Optional query parameters:
        - `sort-by={key}[-{asc|desc}]` e.g. `.../sale-prices?sort-by=price-asc`
    

## Dependencies
- Python 2.7(.6)
- Docker 1.9+ 
- Python PIP   
`sudo apt-get install python-pip`
- Make