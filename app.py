from flask import Flask, render_template, request, jsonify
from logger import App_Logger
from flask_cors import CORS, cross_origin
from scraper import Image_scrapper
import mail
from datetime import datetime
from connect_database import cassandra

logger = App_Logger("static/imagescrapper.log")  # creating App_Logger object
logger.log("info", "Start")  # logging
app = Flask(__name__)


@app.route("/", methods=["GET"])  # route to display the home page
@cross_origin()
def homePage():
    """
    Render index page of app

    :return: homp page
    """
    logger.log("info", "Application Launched")
    return render_template("index.html")


@app.route("/submit", methods=["POST"])  # for calling the API from Postman/SOAPUI
@cross_origin()
def submit():
    """
    Submit user request and insert it in db
    :return: show submission status
    """
    logger.log("info", "Data Submiting")
    try:
        if request.method == "POST":
            name = request.form["name"]
            count = request.form["count"]
            time = request.form["time"]
            email = request.form["email"]
            ob = cassandra("user_data")
            now = datetime.now()

            try:
                ob.insert(
                    "user",
                    "time_stamp,name,count,time,email",
                    f"'{now}','{name}',{count},'{time}','{email}'"
                )
                logger.log("info", f"Submitted DB-inserted")
            except Exception as e:
                self.logger.log("error", f"Submission DB-insert error--{str(e)}")

            return render_template(
                "submit.html",
                message=f"Thanks for your Submission, Job Scheduled for scraping {count} images of {name}.",
            )
    except Exception as e:
        logger.log("error", f"Submition error--{str(e)}")
        return render_template(
            "submit.html", link=link, message="Try again, Request submision error "+str(e)
        )


@app.route("/scrap_images", methods=["POST"])  # for calling the API from Postman/SOAPUI
@cross_origin()
def scrap_images():
    """
    Scrap images and send mail
    :return: confirmation message
    """
    logger.log("info", "Starting image Scraping")
    try:
        if request.method == "POST":
            name = request.json["name"]
            count = int(request.json["count"])
            email = request.json["email"]

            # scraping images
            logger.log("info", "Starting Search and Download")
            ob = Image_scrapper()
            ob.search_and_download(name, count, email)
            # sending mail
            logger.log("info", "Sending Mail")
            ob = mail.mailer()
            mail_confirmation = ob.mail(
                email,
                text=f"{count} images of {name} has been scrapped on your scheduled Time. Click on below link to download your images. Thanks for using our service!",
                link=request.url[
                    : request.url.index(
                        "/",
                        request.url.index(
                            "/",
                        )
                        + 3,
                    )
                ]
                + f"/download?d={name}_{count}_"
                + email[: email.index("@")].lower(),
            )
            if mail_confirmation:
                logger.log("info", "Mail sent")
                return "True"
            else:
                logger.log("info", "Mail not sent")
                return "False_Mail"
    except Exception as e:
        logger.log("error", f"Image scraping error--{str(e)}")
        return "False_ALl"


@app.route(
    "/download", methods=["GET", "POST"]
)  # for calling the API from Postman/SOAPUI
@cross_origin()
def download():
    """
    To download zip files of scrapped images
    :return: Download page
    """
    if request.method == "GET":
        link = (
            request.url[
                : request.url.index(
                    "/",
                    request.url.index(
                        "/",
                    )
                    + 3,
                )
            ]
            + "/static/download/"
            + request.args.get("d")
            + ".zip"
        )
        return render_template("download.html", link=link)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
