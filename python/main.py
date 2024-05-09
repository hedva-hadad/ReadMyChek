# flask is he server that running our api
# flask is a micro web framework for pythyon

# imports
from flask import Flask, request, jsonify

# create flask app
app =Flask (__name__)

@app.route("/") #app is the name of our flask app,/ is the default route
def home():
  return "home"

# run the app=run the flask server
if __name__=="__main__":
    app.run(debug=True)

# GET
# POST
# PUT  # WHEN UPDATING DATA
# DELETE
