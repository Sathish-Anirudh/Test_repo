from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "")

    # Test: Unsafe template rendering
    html = f"""
    <html>
        <body>
            <h2>Welcome {name}</h2>
        </body>
    </html>
    """

    return render_template_string(html)


@app.route("/comment")
def comment():

    comment = request.args.get("comment", "")

    # Test: Directly embedding user input
    return f"""
    <html>
        <body>
            {comment}
        </body>
    </html>
    """


@app.route("/profile")
def profile():

    username = request.args.get("username", "")

    page = f"""
    <div>
        Username: {username}
    </div>
    """

    return page


if __name__ == "__main__":
    app.run(debug=True)
