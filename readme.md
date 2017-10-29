## Twitter link scraper

A small script written in python to fetch links of specific domain from latest tweets. This script was created for educational purposes at a two hour MLIndia workshop. As an example, we fetch all links that belong to domain "sarahah.com" from latest tweets. 

### Running the script

1. For this script, we use bear/python-twitter from [source](https://github.com/bear/python-twitter) which is an open source wrapper around the Twitter API. Follow the instructions from source, or simply run this command :
```
pip install python-twitter
```

2. Fill the twitter_sarahah_links.py with access tokens from [twitter developers account](https://developer.twitter.com/)
```
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
```

3. run command
```
python twitter_sarahah_links.py
```