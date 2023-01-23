# Email Sending Application

This application is a simple utility that allows you to send emails to multiple recipients using a CSV file and an HTML template. It uses the Mailgun API to send emails and the Flask framework to handle the web application.

## Requirements

-   Python 3
-   Flask
-   requests
-   Mailgun account and API key

## Usage

1.  Clone the repository and navigate to the project directory.
2.  Install the required packages by running `pip install -r requirements.txt`.
3.  Create a `config.py` file in the project root and add your Mailgun API key and domain.
4.  Run the application by executing `python app.py`.
5.  In your browser, go to `http://localhost:5000/` to access the application.
6.  Select a CSV file containing the email addresses and an HTML template file.
7.  The default password is "shubh".
8.  Fill in the subject and password fields, and select an attachment file (if any).
9.  Click on the "Send Emails" button to start sending emails.
10. A table will appear on the page showing the status of each email sent (success or failure).

## CSV format

The CSV file should contain at least one column named "to" with the email addresses of the recipients.

## Email format

The email format should be "Designation<emailid@{}>"

## Note

-   Make sure that the "to" field in the csv file is in the format `Designation<emailid@{}>`.
-   Make sure that "to" field is present in the csv file.
-   Placeholder fields in the HTML template should be in the format `{{field_name}}`
## Built With

-   [Flask](https://flask.palletsprojects.com/en/2.1.x/) - The web framework used
-   [requests](https://requests.readthedocs.io/en/master/) - Used to send HTTP requests
-   [Mailgun](https://www.mailgun.com/) - Email sending API
-   [Bootstrap](https://getbootstrap.com/) - CSS framework used for styling


## Project Website

You can find the project website at [Replit](https://GoodnaturedGiddyFormulas.shubhtoy.repl.co)


## Authors

-   [Shubh](https://github.com/shubhtoy)

