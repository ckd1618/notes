This is a Note Posting App   
  
This application uses websockets, along with bootstrap, django, and react frameworks.  
For a list of commands used to install the app, see myDoc.txt  
  
You need three terminal windows open to get this started  
1.) Get redis working (I used Docker)  
docker run -p 6379:6379 -d redis:2.8  
  
2.) Get django running in its environment  
cd notes  
pipenv shell  
python manage.py runserver  

3.) Get react running  
cd notes/frontend  
npm start  
  
project is now up and running at:  
localhost:3000  

