from flask import Flask, render_template, request, redirect, url_for
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait
import concurrent
import csv
import os
from util import send_email

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/send-emails", methods=["POST"])
def send_emails():
    csv_file = request.files["csv_file"]
    try:
        attachment = request.files["attachment"]
    except:
        attachment = None
    template = request.form["template"]
    file_path = os.path.join(os.getcwd(), "temp", csv_file.filename)
    attachment_path = os.path.join(os.getcwd(), "temp", attachment.filename)
    csv_file.save(file_path)
    attachment.save(attachment_path)
    subject = request.form["subject"]
    password = request.form["password"]
    if password == "shubh":
        with open(file_path) as f:
            reader = csv.reader(f)
            headers = next(reader)
            email_index = headers.index("email")
            results = []
            with ThreadPoolExecutor() as executor:
                data = []
                for row in reader:
                    if attachment:
                        data.append((row[email_index], executor.submit(send_email, row[email_index], subject, attachment_path,template,**dict(zip(headers, row)))))
                    else:
                        data.append((row[email_index], executor.submit(send_email, row[email_index], subject, None,template,**dict(zip(headers, row)))))
                for future in concurrent.futures.as_completed([f[1] for f in data]):
                    print(future.result())
                    results.append({'to':next((x[0] for x in data if x[1] == future), None), 'status':future.result()})


                print(results)
        os.remove(file_path)
        os.remove(attachment_path)
        return render_template("status.html", results=results)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
