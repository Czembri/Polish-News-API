# Polish-News-API

<b>Polish-News-API</b> is a free JSON API for hand scraped news.

This project is connected to News-Analysis project:
https://github.com/Czembri/News-Analysis

Script <b>scrap.py</b> gets data from sites that contains news and save this data to MySQL database.

## Usage

> Main site is located at /polish-news/api/v1/news

> Get data by ID:
  /polish-news/api/v1/news/id/<int:id>
  
> Get data by source
  /polish-news/api/v1/news/source/<string:source>
  
 > Get data by date
  /polish-news/api/v1/news/bydate/<string:dates>
  
  ### Date format: 'YYYY-MM-DD'
  
 ## Download
 
 > Clone this repo: https://github.com/Czembri/Polish-News-API.git 
 
 > install vrtual environment 
 
 > install requirements by using requirements.txt
 
 > run code - run.py
 
 > <b>default port</b> is :5000
