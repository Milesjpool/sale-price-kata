# Backlog
## Done
- Status endpoint
  
 > As an API consumer     
 > I want a simple health-check endpoint at `/status`    
 > So that I know the API service is running
---
- Data-dump endpoint
  
 > As a front-end developer     
 > I want a structured dump of all known data    
 > So that I can begin building a suitable UI

>> All data available at `/sale-prices`
---
- Add price sort endpoint

> As a property developer   
> I want to see sorted property prices within the selected region   
> So that I can evaluate an area's desirability

>> Sorted data available at `/sale-prices?sort-by={key}`   
>> Direction may be specified (asc/desc) e.g. `sort-by=long-desc`

## Doing


## To do
- Paginate data-dump
- Latitude filter (query vs resource)
- Longitude filter (query vs resource)
- Lat/long and/or filter (point vs cross)
- Filter context (+- n rows/cols)
- Handle resales.
- Create UI.
- Add docker healthcheck to Functional tests.
- Calculate percentiles at write-time.