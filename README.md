# Spotfiy Data Pipeline - End To End Data Engineering Project
## Overview
Implement End to End Data Pipeline using Spotify API. The project aims to integrate into a Spotify API and use AWS services to extract the messed up data, transform and 
load the data into the serverless analytics platform, AWS Athena for analysis. This pipeline should then be automated in 1 day interval.    
The link to the Spotify playlist : https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF

## Objective   
* Integrating with Spotify API and extracting Data
* Deploying code on AWS Lambda for Data Extraction
* Adding trigger to run the extraction automatically 
* Writing transformation function for the extracted data
* Building automated trigger on transformation function 
* Store files on S3
* Building Analytics Tables on data files using AWS Glue and Athena

## AWS Services Used
1. Amazon S3: Amazon S3 is an object storage service that provides manufacturing scalability, data availability, security, and performance.
2. AWS Lambda: Lambda is a computing service that allows programmers to run code without creating or managing servers.
3. AWS Athena: Athena is an interactive query service for S3 in which there is no need to load data it stays in S3.
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
import json   
import os   
import boto3   
import datetime   
import io.StringIO   

## 🚀 About Me
I'm **Saheen AHZAN**   
An aspiring Big Data Engineer. Steering to transition my career from retail to Big Data.   
**GitHub id :** saheen619    
**LinkedIn Profile :** https://www.linkedin.com/in/saheenahzan/
