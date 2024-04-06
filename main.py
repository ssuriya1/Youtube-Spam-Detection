import os
import re
from flask import Flask, render_template, request, send_file
from joblib import load
from fetch_comments import get_video_comments
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Function to check if a URL is from YouTube
def is_youtube_url(url):
    youtube_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.match(youtube_pattern, url)
    return bool(match)

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
            if is_youtube_url(youtube_url):  # Check if the URL is from YouTube
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

                    # Generate PDF report
                    generate_pdf(spam_results, total_comments)

                    # Provide download link for the PDF
                    return render_template("final.html", comments=spam_results, total_comments=total_comments, pdf_generated=True)
                else:
                    return render_template("final.html", result="No comments available on the YouTube video")
            else:
                return render_template("final.html", result="Please provide a valid YouTube URL")
        else:
            return render_template("final.html", result="Please provide a YouTube URL")
    
    return render_template("final.html")

@app.route("/download_pdf")
def download_pdf():
    # Provide download link for the PDF
    return send_file("output.pdf", as_attachment=True)

def generate_pdf(comments, total_comments):
    # Create a PDF document
    doc = SimpleDocTemplate("output.pdf", pagesize=letter)

    # Define content for the PDF
    content = []

    # Add paragraphs to the content
    content.append(Paragraph("YouTube Spam Detection Report", style=None))
    content.append(Paragraph(f"Total Comments Analyzed: {total_comments}", style=None))
    content.append(Paragraph("\n", style=None))
    content.append(Paragraph("Comments Analysis:", style=None))
    for i, (comment, prediction, accuracy) in enumerate(comments):
        content.append(Paragraph(f"Comment {i+1}: {comment}", style=None))
        content.append(Paragraph(f"Prediction: {prediction}", style=None))
        content.append(Paragraph(f"Accuracy: {accuracy:.2f}%", style=None))
        content.append(Paragraph("\n", style=None))

    # Build the PDF document
    doc.build(content)

if __name__ == "__main__":
    app.run(debug=True, port=560)
