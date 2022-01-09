# Program use command line arguments ( URL parameter in long (--url) or short (-l) )

# import the necessary packages
import argparse
import requests
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-l", "--url", required=True,
	help="Short or long URL required")

args, unknown = ap.parse_known_args()
ref_args =vars(args)



print("\nTrying to reach : ", ref_args['url'])
response = requests.get(ref_args['url'])

resp_code=response.status_code
if resp_code != 200:
	print("Web page can not be reach, check your URL address.  ",response )
else:print("\nFrom a server ",response)

size = len(unknown)
if size > 0:
	print("\nList of ignored parameters : ",  unknown)