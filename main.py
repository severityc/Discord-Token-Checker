import requests
import base64
import json

class DiscordTokenChecker:
    def __init__(self):
        self.cookies = self.get_cookies()
        self.props = self.get_super_properties()

    def get_cookies(self):
        cookies = requests.get("https://discord.com").cookies.get_dict()
        cookies_str = "; ".join([f"{key}={value}" for key, value in cookies.items()])
        return cookies_str

    def get_super_properties(self):
        properties = {
            "os": "Windows",
            "browser": "Chrome",
            "device": "",
            "system_locale": "en-US",
            "browser_user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9030 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
            "browser_version": "1.0.9030",
            "os_version": "10",
            "referrer": "",
            "referring_domain": "",
            "referrer_current": "",
            "referring_domain_current": "",
            "release_channel": "stable",
            "client_build_number": 108776,
            "client_event_source": None
        }
        return base64.b64encode(json.dumps(properties).encode()).decode()

    def token_checker(self, token):
        headers = {
            "authority": "discord.com",
            "accept": "*/*",
            "accept-language": "en",
            "authorization": token,
            "cookie": self.cookies,
            "content-type": "application/json",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9030 Chrome/108.0.5359.215 Electron/22.3.26 Safari/537.36",
            "x-discord-locale": "en-US",
            'x-debug-options': 'bugReporterEnabled',
            "x-super-properties": self.props,
        }

        response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)

        if response.status_code == 200:
            print('token is valid')
            with open('data/valid.txt', 'a') as f:
                f.write(token + '\n')
        else:
            print('token is invalid')

    def main(self):
        with open('data/tokens.txt', 'r') as f:
            tokens = f.read().splitlines()

        for token in tokens:
            self.token_checker(token)


if __name__ == "__main__":
    checker = DiscordTokenChecker()
    checker.main()
