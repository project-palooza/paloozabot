## Paloozabot

### purpose

bot to automate notifications and generally make life easier for the people in the Data Palooza Discord server.

### current state

current state - May 22 24

we've been working on some data engineering aspects of the project.

specifically, we want to organize bot logs for analysis.

last week we tested out the idea of using GPT to extract logs. It works fine but we're not done.

### next steps

our GPT prompt can decompose a single log into DB fields. but we have many logs. if we pass the log file into GPT line by line, we'll get bad outputs, since logs can be multi-line. to work around this we'll use regular expressions to isolate logs. 

- put logs in a queue
- tag them as being System, Message or Command based on the presence of certain fields peculiar to each type of log.
- pass them through gpt to get JSON output
- post JSON to the database

feature requests:

- welcome new users with a picture of a cute dog
- provide updates about updated repos
- post reminders for upcoming code-alongs
- match project leaders to project followers

