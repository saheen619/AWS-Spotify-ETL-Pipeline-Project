# Spotfiy Data Pipeline - End To End Data Engineering Project
## Overview:
Implement End to End Data Pipeline using Spotify API. The project aims to integrate into a Spotify API and use AWS services to extract the messed up data, transform and 
load the data, to be query'd by the serverless analytics platform, AWS Athena for analysis. This pipeline should be automated in 1 day interval.    
The link to the Spotify playlist : [Spotify Playlist](https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF)

## Objective:

* Integrating with Spotify API and extracting Data
* Deploying code on AWS Lambda for Data Extraction
* Adding trigger to run the extraction automatically 
* Writing transformation function for the extracted data
* Building automated trigger on transformation function 
* Store files on S3
* Building Analytics Tables on data files using AWS Glue and Athena

### API Used:
This API contains information about music artist, albums and songs - [Spotify API](https://developer.spotify.com/documentation/web-api)

## AWS Services Used:
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.    

2. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.    

3. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3. Glue Crawler is a fully managed service that automatically crawls your data sources, identifies data and infer schemas to create an Glue Data Catalog.   

4. AWS Glue: A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics and application development.    

5. AWS IAM: This is an identity and access management service which enables us to manage access to AWS services and resources securely.   

6. AWS Clowdwatch Events/Event Bridge : It helps in creating a CloudWatch Events Rule That Triggers on an Event or a particular set interval of time.

## ETL Pipeline - Architectural Diagram
<img src="ETL Architecture Diagram.jpg">

## Requirements
Python 3 & Above   
AWS Services
#### Python Packages - 
import spotipy   
import pandas   
import numpy
import json   
import os   
import boto3   
import datetime   
import io.StringIO   

## Authors

[Saheen Ahzan](https://github.com/saheen619)


## Feedback

If you have any feedback, please reach out at saheen619.klm@gmail.com
