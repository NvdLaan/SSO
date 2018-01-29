import validators
url = "https://unifi.oscarr.nl:8443"
if validators.url(url):
    print("Valid URL")
else:
    print("No Valid URL")
