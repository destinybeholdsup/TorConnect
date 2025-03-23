import requests
from tor_request import start_tor, get_tor_session, renew_tor_identity

tor_location = 'tor.exe expert bundle location here'

def main():
    if start_tor(tor_location):
        session = get_tor_session()
        try:
            print("Making request through Tor network...")
            response = session.get("https://api.ipify.org")
            print(f"Success! Response: {response.text}")
        except requests.RequestException as e:
            print(f"Request failed: {e}")
        finally:
            renew_tor_identity()

if __name__ == "__main__":
    main()
