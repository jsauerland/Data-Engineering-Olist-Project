#### To Do List

This is a list of tasks that will be performed in the future as part of this project. The tasks reflected here are the same that I track on my Trello board in the incomplete tasks section. 

1. Integrate Salesforce for extra flavor

First, obtain Salesforce, and import data there.

Second, export whichever database table I need into a bunch of csv files and store them on a shared folder called SFTP. Since it’s a shared folder, multiple accounts can access it. The Salesforce marketing cloud (SFMC) application is the configured to connect to and read these files regularly from this shared folder

Lastly, schedule to run a python script once a day to read the table we want to export and then send those rows of data to whichever third party requires it. The scheduling is done using the Airflow python library. The third parties receive the data over the internet to a special page on their website that allows us to upload data programmatically.