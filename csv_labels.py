from __future__ import print_function
import time
import csv
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        #print('Labels:')
        master_list = [["name",
                        "id",
                        "type",
                        "messagesTotal",
                        "messagesUnread",
                        "threadsTotal",
                        "threadsUnread",
                        "messageListVisibility",
                        "labelListVisibility"]]

        total = len(labels)
        count = 1
        print(total, ' labels found, getting details for each...')

        for label in labels:
            try:
                details = service.users().labels().get(userId='me',id=label["id"]).execute()
                
                detail_row = [details.get('name', ''), 
                          details.get('id', ''),
                          details.get('type', ''),
                          details.get('messagesTotal', ''),
                          details.get('messagesUnread', ''),
                          details.get('threadsTotal', ''),
                          details.get('threadsUnread', ''),
                          details.get('messageListVisibility', ''),
                          details.get('labelListVisibility', '')]
                master_list.append(detail_row)
                print("Processed details for label ", count, " of ", total)
                count+=1
                #print(label['name'])
            except errors.HttpError as error:
                print("an error occurred with label ", label["id"])

        print("Creating CSV for ", len(master_list) - 1, " labels...")
        t = time.localtime()
        current_time = time.strftime("%Y-%b-%d_%H:%M:%S", t)
        with open('label_details_' + current_time + '.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(master_list)
            file.close()
        print('done!')

if __name__ == '__main__':
    main()
