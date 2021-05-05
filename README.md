# Youtube_promotion_on_twitter

<p align="left">
<a href="https://github.com/DivyaKumarBaid/Youtube_promotion_on_twitter/blob/main/LICENSE" alt="Lisence"><img src="https://img.shields.io/github/license/DivyaKumarBaid/Youtube_promotion_on_twitter"></a> <a href="https://github.com/DivyaKumarBaid/Youtube_promotion_on_twitter/issues" alt="Issues"><img src="https://img.shields.io/github/issues/DivyaKumarBaid/Youtube_promotion_on_twitter"></a> <a href="https://twitter.com/DivyakumarBaid1?s=09" alt="Twiter-Follow"><img src="https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FDivyaKumarBaid%2FYoutube_promotion_on_twitter"></a>
</p>

This is a simple automation that tweets the title and the link of a channels latest video when uploaded along with tags.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) \
To install google-api-python-client

```bash
python3 -m pip install -U google-api-python-client
```
To install tweepy
```bash
pip install tweepy
```

## Pre-Text:


This is a simple autmation that helps to understand how API works and how to use them on a real life example.

## How to Install

1. Create a ```python``` virtual environment.
2. Clone the repo ```git clone https://github.com/DivyaKumarBaid/Youtube_promotion_on_twitter.git``` or download the repository.
3. Go to the cloned/downloaded directory ``` cd Youtube_promotion_on_twitter ``` 
4. Create a project on [google cloud console](https://console.cloud.google.com/) and enable youtube API V3
5. Copy the ``API Acess Key`` of the API and paste it in the ``api_key`` under youtube api in main.py file
6. If you have a developer account in twitter then create or generate the api keys (consumer_key,consumer_key_secert,access_key,access_key_secret)
      
      *If you dont have the developers account then you have to apply for it, it will take a day or two to be approved*
      
7. You have to get the youtube channel Id you want to promote (you will get it from the https link e.g.https://www.youtube.com/channel/CHANNEL_ID )
8. Run it.

## Note 

To minimise the calling to youtube API as it has low quota, I have set the interval between any call of youtube api to be 1hr. However you can change it as you like.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
