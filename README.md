# App

This project was generated with Django version=4 and sqlite database as requirements for Una health
interview task

## Steps to run for development 

- cd into app directory and run this command:
    ```
    docker-compose up
    ```

## Available Endpoints:
1) list Glucose levels: GET /api/v1/levels 
    
    ```
    api/v1/levels/?start=2021-02-18 11:19:00&stop=2021-02-18 11:19:00&user_id=<user_id>&ordering=gerate_zeitstempel
    ```
    
    Params:

        start: datetime (2021-02-18 11:19:00)

        stop: datetime (2021-02-18 11:19:00)

        ordering: gerate_zeitstempel(asc) or -gerate_zeitstempel (dsc)

        user_id: str (user_id)
        


2) get Glucose level by ID: GET /api/v1/levels/:id

    ```
    /api/v1/levels/:id
    ```