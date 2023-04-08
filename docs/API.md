## Game of "Rock Paper Scissors"
___
+ ***URL:***    
    /rps
+ ***Method:***   
    GET    
    POST    
+ ***URL-params(GET):***   
choice = [string]
+ ***Body-params(POST):***    
choice = [string]
+ ***Data Params:***   
None
+ ***Success Response:***   
**Code**: 200   
**Content**: {"your_choice": "paper", "pc_choice": "scissors", "message": "You Win"}
+ ***Error Response:***   
**Code**: 400   
**Content**: {"detail": "You have incorrect choice"}
+ ***Sample Call:***  

GET
```
curl -X 'GET' \
  'http://127.0.0.1:8000/game/rps?choice=paper' \
  -H 'accept: application/json' 
  ```
POST

```
curl -X 'POST' \
  'http://127.0.0.1:8000/game/rps' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "your_choice": "paper",
}'
```