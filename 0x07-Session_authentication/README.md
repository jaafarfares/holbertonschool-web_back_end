# 0x07-Session_authentication

The project involves the implementation of a session authentication mechanism for a REST API. The API has endpoints for managing users, which were previously protected by basic authentication. The implementation will be done from scratch, without the use of any external modules or frameworks, for educational purposes. The code from the previous basic authentication project will be used as a starting point, and the functionality will be expanded to include a new endpoint for retrieving the authenticated user. The endpoint will require basic authentication, and the authentication information will be passed along with each request in the form of an HTTP header. The new endpoint will retrieve the user information if the user is authenticated, and return an error if the user is not authenticated. The updated code will be tested using a series of curl commands in a terminal.


## Usage 

#### Simple example for a method that returns a User instance based on a cookie value


#### In the first terminal:


```

Jaafar@Fares:~$
Jaafar@Fares:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id ./main_4.py
User with ID: cf3ddee1-ff24-49e4-a40b-2540333fe992 has a Session ID: 9d1648aa-da79-4692-8236-5f9d7f9e9485
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....


```

#### In a second terminal:

```

Jaafar@Fares:~$ curl "http://0.0.0.0:5000/"
No user found
Jaafar@Fares:~$
Jaafar@Fares:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=Holberton"
No user found
Jaafar@Fares:~$
Jaafar@Fares:~$ curl "http://0.0.0.0:5000/" --cookie "_my_session_id=9d1648aa-da79-4692-8236-5f9d7f9e9485"
User found: cf3ddee1-ff24-49e4-a40b-2540333fe992
Jaafar@Fares:~$

```


## Made by [Jaafar Fares](https://github.com/jaafarfares) for [Holberton School](https://www.holbertonschool.com/)
