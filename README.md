# Reddit-To-YouTube

Reddit-To-YouTube scrapes a subreddit for vreddit videos, combines them into
one monolithic video, and uploads them to YouTube.

## Setting up YouTube uploading
1. Grab a copy of the Python 3 variant of Google's `upload_video.py`, available [here](https://gist.github.com/Cal-B/2d98f3beab74e958e35be7c1a747d472) and place it in the project directory 
2. Install the Google APIs Client Library for Python with `pip install google-api-python-client`
3. [Generate OAuth2.0 credentials](https://developers.google.com/youtube/registering_an_application) and plug your Client ID and Client Secret into `client_secrets.json`.
3. Set the subreddit, video quantity, and video post time in [`modules/reddit_api.py`](https://github.com/FriendosClub/Reddit-To-YouTube/blob/38ec8ab51305a7fd85c3d766837d1e659eb4dd7b/modules/reddit_api.py#L6)
4. Set the upload info (Video title, descriprion, tags, etc) in [`reddit-to-youtube.py`](https://github.com/FriendosClub/Reddit-To-YouTube/blob/db494a9dc0d9a6be5ab4edc780295f394ddbc052/reddit-to-youtube.py#L41)
5. Run the program with `python3 reddit-to-youtube.py`

