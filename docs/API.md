## Game of "Rock Paper Scissors"
___
+ ***URL:***    
    /rps
+ ***Method:***   
    GET    
    POST    
+ ***URL-params:***   
choice = [string]
+ ***Body-params:***    
choice = [string]
+ ***Data Params:***   
None
+ ***Success Response:***   
**Code**: 200   
**Content**: {"choice": "paper","winner": "You Lose, i have scissors"}
+ ***Error Response:***   
**Code**: 400   
**Content**: {detail: "You have incorrect choice"}
+ ***Sample Call:***   
```
curl -XPOST "http://localhost:8000/game" -d '{"path":"/rps","httpMethod":"GET","version":"1.0","requestContext":{"protocol":"HTTP/1.1"}, "queryStringParameters": {"choice": "paper"}, "body": null}'
