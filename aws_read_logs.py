import gzip
import json
import glob


import argparse

def print_logs():

    files = glob.glob('**', recursive = True)


    if args.eventID.upper() == "":
        print("NN;eventTime;awsRegion;sourceIPAddress;user;arn;eventCategory;"\
              "eventSource;eventType;eventName;eventID")

    count=0
    for f in files:
        if f.endswith(".gz"):
            with gzip.open(f) as j:
                data = json.loads( j.read() )
            if "Records" in data:
                for i in data['Records']:
                    count=count+1

                    user = "--no user--"
                    arn = "--no arn--"
                    if "userIdentity" in i:
                        if "userName" in i['userIdentity']:
                            user = i['userIdentity']['userName']
                        if "arn" in i['userIdentity']:
                            arn = i['userIdentity']['arn']

                    match = True
                    if not args.user in user:
                        match = False

                    if  not args.ip.upper() in  i['sourceIPAddress'].upper():
                        match = False

                    if  not args.service.upper() in i['eventSource'].upper():
                        match = False

                    if  not args.region.upper() in i['awsRegion'].upper():
                        match = False

                    if  not args.event.upper() in i['eventName'].upper():
                        match = False                        

                    if args.eventID.upper() == i['eventID'].upper():
                        print(json.dumps(i, indent=4, sort_keys=True))
                        exit(0)

                    if match and args.eventID == "":
                        print(f"{count};{i['eventTime']};{i['awsRegion']};"\
                              f"{i['sourceIPAddress']};{user};{arn};{i['eventCategory']};"\
                              f"{i['eventSource']};{i['eventType']};{i['eventName']};"\
                              f"{i['eventID']}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Read aws logs from .json.gz files')
    parser.add_argument('--user',  default="", type=str, dest='user', help = "Filter by USER contains value")
    parser.add_argument('--region',  default="", type=str, dest='region', help = "Filter by region contains value")
    parser.add_argument('--ip', default="", type=str, dest='ip', help = "Filter by IP contains value")
    parser.add_argument('--service',  default="", type=str, dest='service', help = "Filter by aws service contains value")
    parser.add_argument('--event',  default="", type=str, dest='event', help = "Filter by event name contains value")
    parser.add_argument('--id',  default="", type=str, dest='eventID', help = "Filter by exact eventID and show log json")
    
    args = parser.parse_args()

    print_logs()


