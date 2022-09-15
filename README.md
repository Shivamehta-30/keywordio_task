# keywordio_task
Backend Code Explanation : 

1.	  First I used normal Django rest framework and for crud functionality I used restframework generics import ListcreatAPIView, RetriveUpdateDestoryAPIView
      Apart form this this method easily return the data from the database and I can perform all the operations.
      After that I need to create one Book Serailzer class in that class I have to get all the necessary fields
      Moreover in views.py I created one ListCreateAPIView class and second is RetriveUpdateDestoryAPIView class 
      in that class I need authenticate user while GET,POST,PUT or DELETE
2.	  In the model of Booklist there is foreignkey is given and its directly relation to individual and get data from database.
3.	  For authentication I used JWT concept for basic authentication for the login it is in backends.py 
      I created one JWTAuthentication class that contains all the JWT login also there is two exceptions is for invalid login and expired token login
NOTE :     Additionally, I used MySQL for the database in accordance with the requirement. Furthemore, I included the user-exists condition and all endpoints         functioned successfully in Postman, but I did not develop the front end, so kindly check it.
