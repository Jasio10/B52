print( "Hi Jasio")
# import the necessary packages
import argparse
import requests
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--url", required=True,
	help="Short or long URL required")
args = vars(ap.parse_args())

print(args["url"])
response = requests.get(args["url"])
print(response)