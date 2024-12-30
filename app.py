
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify
from flask import current_app
from l23_full_stack_app import ice_break_with

load_dotenv()
import os


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():

    name = request.form["name"]
    location = request.form["location"]
    keywords = request.form["keywords"]
    mock = True if request.form.get('mock') else False #to return a bool....else you get a string of 'on' or 'off'

    current_app.logger.debug(f"Received name: {name}, location: {location}, keywords: {keywords}, mock: {mock}")

    summary, profile_pic_url = ice_break_with(
        name=name,
        location=location,
        keywords=keywords,
        mock=mock
    )

    current_app.logger.debug(f"summary: {summary}, profile_pic_url: {profile_pic_url}")
    
    res = jsonify(
        {
            "summary_and_facts": summary.to_dict(),
            "picture_url": profile_pic_url,
        }
    )



    return res





if __name__ == "__main__":

    app.run(host="0.0.0.0", debug=True)