# flask is he server that running our api
# flask is a micro web framework for pythyon

# imports
from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
# create flask app
app =Flask (__name__)

# @app.route("/get-user/<user_id>") #app is the name of our flask app,/ is the default route
@app.route("/") #app is the name of our flask app,/ is the default route

def home():
  return "home"
# run the app=run the flask server
if __name__=="__main__":
    app.run(debug=True)


# הורד את התמונה והעביר אותה לפורמט PIL
image = Image.open('images/pic1.png')

# השתמש בספריית pytesseract כדי לקרוא את הטקסט מהתמונה
text = pytesseract.image_to_string(image)

# הדפס את הטקסט שנקרא מהתמונה
print(text)

