import requests
from bs4 import BeautifulSoup

def get_video_comments(video_url, max_comments=5):
    try:
        response = requests.get(video_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            comment_divs = soup.find_all('yt-formatted-string', class_='style-scope ytd-comment-renderer')
            comments = [comment.text.strip() for comment in comment_divs]
            print(comments)
            return response.text
            # return comments[:max_comments]
        else:
            print("Failed to fetch HTML content.")
            return []
    except Exception as e:
        print(f"Error fetching comments: {e}")
        return []

# video_url = 'https://realpython.com/python-web-scraping-practical-introduction/'
video_url = 'https://www.youtube.com/watch?v=Keck4iVUUdE'
comments = get_video_comments(video_url)
if comments:
    # Write HTML content to a file
    with open('youtube_video_page.html', 'w', encoding='utf-8') as f:
        f.write(comments)
    print("HTML content saved to 'youtube_video_page.html' file.")
# for i, comment in enumerate(comments, start=1):
#     print(f"Comment {i}: {comment}")
