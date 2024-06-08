import time
from hamster_kombat import HamsterKombat
import requests
from util import Morse

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
BOT_TOKEN = value = os.getenv("BOT_TOKEN")

access_tokens = [
    {
        "name": "fira",
        "value": "1716824639522uPRG0keQZZX58Xcg68z0iSZOGzJh6KdZFubkMOy8fYgksOYXOFJLPjkIkgbGuY7M1042334802",
    },
    {
        "name": "0xd",
        "value": "1716892134086wWcCyoCqFjUmksKOASmc4BzT6EkwfMta0ar6IVH330zDVyew7tJEuc0Tcpao4xDC6482218185",
    },
]


def notify(chat_id: str = "1042334802", msg: str = "hi") -> None:
    url = f"https://api.telegram.org/{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "disable_notification": True,
        "parse_mode": "HTML",
        "text": "up",
    }
    requests.post(url, data=data)


while True:
    for token in access_tokens:
        # Login and claim the coins the bot worked

        try:
            hamster = HamsterKombat(token["value"])
            msg = f"<i>{hamster.tg_user_info['firstName']}</i>"
            msg += f"\n<b>Passively Earned</b>: {format(hamster.click_user['lastPassiveEarn'], ',')}"

            # Claim daily streak if available
            if streak_days := next(
                (item for item in hamster.tasks if item["id"] == "streak_days"), None
            ):
                if not streak_days["isCompleted"]:
                    task = hamster.check_task("streak_days")
                    reward_by_days = next(
                        (
                            item
                            for item in task["rewardsByDays"]
                            if item["days"] == task["days"]
                        ),
                        None,
                    )

                    if reward_by_days:
                        msg += f"\n<b>Daily Streak claimed</b>: {format(reward_by_days['rewardCoins'], ',')}, day {task['days']}"
                    else:
                        msg += (
                            f"\n<b>Daily Streak</b>: var reward_by_days returned None"
                        )

                else:
                    msg += f"\n<b>Daily Streak</b>: Already completed"

            else:
                msg += (
                    f"\n<b>Daily Streak</b>: var streak_day is not found in task list"
                )

            # Claim daily cipher if available
            # And replicate the bot activities performed while deciphering for better disguise

            if not hamster.daily_cipher["isClaimed"]:
                cipher = hamster.daily_cipher["cipher"]
                decoded_cipher = Morse.decode_cipher(cipher).upper()

                for mCodes in Morse.encrypt(decoded_cipher).strip().split():
                    hamster.tap(len(mCodes))

                daily_cipher = hamster.claim_daily_cipher(decoded_cipher)

                msg += f"\n<b>Daily cipher claimed</b>: {format(daily_cipher['bonusCoins'], ',')}"

            else:
                msg += f"\n<b>Daily cipher</b>: Already Claimed"

            msg += f"\nTime: {time.asctime()}"
            notify(msg=msg)
            print(msg)

        except Exception as e:
            error_msg = f"{time.asctime()}: Error occurred for {token['name']} token, Error: {str(e)}"
            print(error_msg)
            notify(error_msg)

    time.sleep(60 * 60 * 3)
