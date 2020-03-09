# HaloTwitterBot
A twitter bot I made on my Raspberry Pi that will tweet out dialog from the Halo games every few hours. Automated via a CRON job.


# To Run
python twitter.py

# To Automate
CRON JOB DETAILS
crontab -e
*/60 * * * * python twitter.py 

This will run this once every hour.
