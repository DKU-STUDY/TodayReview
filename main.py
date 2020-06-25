import os
from datetime import datetime, timedelta
from pytz import timezone
from crawling_yes24 import parsing_beautifulsoup, extract_book_data
from github_utils import get_github_repo, upload_github_issue


if __name__ == "__main__":
    access_token = os.environ['MY_GITHUB_TOKEN']
    repository_name = "TodayReview"

    seoul_timezone = timezone('Asia/Seoul')
    today = datetime.now(seoul_timezone)

    close = today + timedelta(days=-1)
    open = today + timedelta(days=1)
    
    closeDate = close.strftime('%Y-%m-%d');
    openDate = open.strftime('%Y-%m-%d');
    
    repo = get_github_repo(access_token, repository_name)
    upload_github_issue(repo, openDate, "")
    print("Upload Github Issue Success!")
