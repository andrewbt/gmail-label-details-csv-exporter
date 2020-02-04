# gmail-label-details-csv-exporter
Exactly what it says; uses the Gmail API to export your account's labels w/details and generate a CSV

# Origin story (or, why this?)
I'm trying to organize and clean up my Gmail inbox, and I got frustrated that seemingly the only ways to view labels were in the little side pane, or in the Settings section. Only in the Settings section do you get readouts for the number of messages tagged with each label (useful for determining if that aspirational label I created years ago actually got used or not; if not maybe I should delete or recategorize). And neither of these existing views in Gmail give a screen-compact way to see the "big picture", or drag/drop and re-order the labels in a list to reorganize, etc. Much like a spreadsheet could. I wanted a spreadsheet of my labels and their details. So I discovered the Gmail API and coded up a way to get it :)

## How this?
I was surprised how easy and quick this was, thanks to the [Google Developer Docs on the Gmail API](https://developers.google.com/gmail/api) - specifically the Users.labels [list](https://developers.google.com/gmail/api/v1/reference/users/labels/list) and [get](https://developers.google.com/gmail/api/v1/reference/users/labels/get) methods. I found the Google [Python Quickstart](https://developers.google.com/gmail/api/quickstart/python) already came pretty close to what I wanted to do, so I copied it and Google's `quickstart.py` is the 90% foundational basis for my `csv_labels.py` file. My additions are basically all at the last step - instead of printing out the label names, I get the additional details I wanted for each label, create a huge "list of label detail lists", and write each label detail list of this "list of lists" to a new row in a CSV file that's timestamped (helped when debugging, but could also help if you want to run this multiple times). I then open the CSV in my favorite spreadsheet program and get to work!

# How can you use it?
1. Install Python, I recommend virtualenv too (and creating and activating one before step 2). Here's [a decent guide on that I found.](https://dont-be-afraid-to-commit.readthedocs.io/en/latest/virtualenv.html)
2. Git clone and/or download the files in this repo.
3. Follow step 1 and step 2 of the [Google Gmail API Python quickstart](https://developers.google.com/gmail/api/quickstart/python). Save the credentials.json file it makes for you; or substitute the values in my included `credentials.example.json` and rename it to `credentials.json`. Either way is fine.
4. Run my `csv_labels.py` file: `python csv_labels.py`. Your browser should open to authenticate your Google account and then progress updates will print to the terminal as it goes! A CSV file with the current time will be generated and saved in the directory you ran the script. Hope it works for you!

# Future improvement ideas
- What happens when a label name has a comma in it, will that "break" the CSV and do we need to add quoting?
- Could we alphabetize the CSV? Would help too with keeping nested labels on rows close to each other, right now they're all over the place (I fix this manually in Google Sheets by hand later)
- Could we automagically upload the CSV to Google Drive? (I do this by hand now)

# Like this? Did it help you?
I would _LOVE LOVE LOVE it_ if you would simply [Tweet me a quick thank you!](http://twitter.com/andrewbt)
