import pyrebase
import veritabani
import idefix
config={
    "apiKey": "AIzaSyAxr4pDOSD8VwnOCLTQK5Jot0g3qrgIu0Y",
    "authDomain": "bitirme-tezi-bc9e4.firebaseapp.com",
    "databaseURL": "https://bitirme-tezi-bc9e4.firebaseio.com",
    "projectId": "bitirme-tezi-bc9e4",
    "storageBucket": "bitirme-tezi-bc9e4.appspot.com",
    "messagingSenderId": "224562754547",
    "appId": "1:224562754547:web:dc18c65469394d8766d886",
    "measurementId": "G-05W4YMCPDS",
}
firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
email="kubraayses1905@gmail.com"
password="kayse1905"
user=auth.sign_in_with_email_and_password(email,password)
#auth.send_email_verification(user['idToken'])
db=firebase.database()
data=[]
data=veritabani.read_data()
db.child("books").child("book_link").push(data)
db.child("books").child("book_name").push(data)
db.child("books").child("book_author").push(data)
db.child("books").child("book_price").push(data)

