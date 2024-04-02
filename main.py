import os
from flask import Flask, render_template, request
from joblib import load
from fetch_comments import get_video_comments

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Define the error handler route
@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/spam", methods=["GET","POST"])
def spam():
    if request.method == "POST":
        youtube_url = request.form["youtube_url"]
        if youtube_url:
            comments, total_comments = get_video_comments(youtube_url)
            if comments:
                # Load spam detection model
                loaded_model, loaded_vect = load('best_model.pkl')
                spam_results = []
                for comment in comments:
                    # Transform comment and predict spam
                    new_comment = [comment]
                    new_comment_transformed = loaded_vect.transform(new_comment).toarray()
                    prediction = loaded_model.predict(new_comment_transformed)[0]
                    accuracy = loaded_model.predict_proba(new_comment_transformed)[0][1] * 100
                    if prediction == 1:
                        spam_results.append((comment, "Spam", accuracy))
                    else:
                        spam_results.append((comment, "Not Spam", accuracy))
                
                # Process comments for spam detection or any other task
                return render_template("final.html", comments=spam_results, total_comments=total_comments)
            else:
                return render_template("final.html", result="No comments available on the YouTube video")
        else:
            return render_template("final.html", result="Please provide a valid YouTube URL")
    
    return render_template("final.html")

if __name__ == "__main__":
    app.run(debug=False, port=560)
