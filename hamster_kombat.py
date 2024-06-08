import time
import requests


# constant/base headers
HEADERS = {
    "accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en,en-US;q=0.9",
    "Connection": "keep-alive",
    "Host": "api.hamsterkombat.io",
    "Origin": "https://hamsterkombat.io",
    "Referer": "https://hamsterkombat.io/",
    "sec-ch-ua": '"Android WebView";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; G011A Build/PI; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6422.72 Mobile Safari/537.36",
    "X-Requested-With": "org.telegram.messenger",
}

BASE_URL = "https://api.hamsterkombat.io/"


class HamsterKombat:
    def __init__(self, access_token: str) -> None:
        self.access_token = access_token
        self.headers = dict(HEADERS)
        self.headers["Authorization"] = f"Bearer {access_token}"
        self.s = requests.Session()  # requests session to re-use connection pool
        self.auth_status()
        self.config()
        self.sync()
        self.list_tasks()

    def auth_status(self) -> None:
        path = "auth/me-telegram"

        res = self.s.post(BASE_URL + path, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            res_json = res.json()
            if res_json["status"] != "Ok":
                raise Exception("Auth status is not ok", res_json)

            self.tg_user_info = res_json["telegramUser"]

        except Exception as e:
            raise Exception("Auth Status failed, Error", e, "resp: ", res.text)

    def config(self) -> None:
        path = "clicker/config"

        res = self.s.post(BASE_URL + path, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.click_config = res.json()["clickerConfig"]
            self.daily_cipher = res.json()["dailyCipher"]

        except Exception as e:
            raise Exception("Config failed,", e, "resp: ", res.text)

    def sync(self) -> None:
        path = "clicker/sync"

        res = self.s.post(BASE_URL + path, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.click_user = res.json()["clickerUser"]

        except Exception as e:
            raise Exception("Sync failed,", e, "resp: ", res.text)

    def tap(self, tap_count: int = 1) -> dict:
        path = "clicker/tap"

        data = {
            "count": tap_count,
            "availableTaps": self.click_user["availableTaps"] - tap_count,
            "timestamp": int(time.time()),
        }

        res = self.s.post(BASE_URL + path, headers=self.headers, json=data)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.click_user = res.json()["clickerUser"]

        except Exception as e:
            raise Exception("Tap failed,", e, "resp: ", res.text)

    def list_tasks(self) -> None:
        path = "clicker/list-tasks"

        res = self.s.post(BASE_URL + path, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.tasks = res.json()["tasks"]

        except Exception as e:
            raise Exception("List tasks failed,", e, "resp: ", res.text)

    def boosts_for_buy(self) -> None:
        path = "clicker/boosts-for-buy"

        res = self.s.post(BASE_URL + path, headers=self.headers)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.boosts_for_buy = res.json()["boostsForBuy"]

        except Exception as e:
            raise Exception("Boosts for buy failed,", e, "resp: ", res.text)

    def buy_boost(self, id: str) -> None:
        path = "clicker/buy-boost"

        data = {"boostId": id, "timestamp": int(time.time())}

        res = self.s.post(BASE_URL + path, headers=self.headers, json=data)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.click_user = res.json()["clickerUser"]

        except Exception as e:
            raise Exception("Buying boost failed,", e, "resp: ", res.text)

    def check_task(self, task_id: str) -> dict:
        path = "clicker/check-task"

        data = {"taskId": task_id}

        res = self.s.post(BASE_URL + path, headers=self.headers, json=data)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            return res.json()["task"]

        except Exception as e:
            raise Exception("Check task failed,", e, "resp: ", res.text)

    def claim_daily_cipher(self, cipher_text: str) -> None:
        path = "clicker/claim-daily-cipher"

        data = {"cipher": cipher_text.upper()}

        res = self.s.post(BASE_URL + path, headers=self.headers, json=data)
        if res.status_code != 200:
            raise Exception("Request status is not OK", res.status_code, res.text)

        try:
            self.click_user = res.json()["clickerUser"]
            return res.json()["dailyCipher"]

        except Exception as e:
            raise Exception("Claiming daily cipher failed,", e)

    def __str__(self) -> str:
        tg_usr = self.tg_user_info
        return f"""\tTG ID: {tg_usr.get('id')}, fName: {tg_usr.get('firstName')}
        Total coins: {format(int(self.click_user.get('balanceCoins')), ',')}
        """
