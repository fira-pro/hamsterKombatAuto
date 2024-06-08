# Hamster Kombat Bot Automator

## An automation for Hamster Kombat Telegram bot to collect coins without the need to open the bot

Collects coins🪙 generated passively every 3 hours, claims daily streak, Morse code cipher daily bonus and send notification to Telegram bot🤖

![image](https://github.com/fira-pro/hamsterKombatAuto/assets/85739903/ef2bfd5c-4f93-4d1c-86eb-155b0dcb9297)

## What This Code Can Do

- **Collect passive coins**: collect passively generated coins by _profit per hour_ every 3 hours⏲️
- **Claim daily📆 streak**: claim daily streak bonus of the day. After 10 days and 5M coin bonus, resets back to day 1.
- **Daily cipher**: solve and claim the daily morse cipher. Because the cipher code is available inside the API response, it can be decoded easily
- **Notification**: send notification about the result using Telegram bot
- **Multiple account**: support multiple telegram account. see [access_tokens](access_tokens.json) file

## TODO

- [ ] Add the ability to receive list of daily combo cards and claim 5M coins🔥

## How to use

- To use this code:

  - you need to get **Authorization** token used by Hamster Kombat API by doing **MITM**(Man In The Middle) on telegram app while opening the Hamster Kombat bot miniApp.
    For this, You can use an any android emulator with adb enabled and root access with HTTP Toolkit. refer HTTP Toolkit's guide [here](https://httptoolkit.com/docs/guides/android/). (I will include tutorial soon😄)
    <img width="760" alt="image" src="https://github.com/fira-pro/hamsterKombatAuto/assets/85739903/7d858eb1-fdae-493f-9b3a-d26a92e1f5f7">

  - **[Optional]** Obtain Your Telegram Bot Token via [@BotFather](https://t.me/botfather). I you don't want this feature comment out all calls to `notify(args*)` function inside main.py.

- ### Installation

  - Clone this repo
  - Install required packages `pip install -r requirements.txt`
  - Add your access tokens to the file access_tokens.json array

````json
[
    {
    "name": "user1",
    "value": "accessTokenForThe1stUser"
    },
    {
    "name": "user2",
    "value": "accessTokenForThe2ndUser"
    }
]
    ```

  - Add your Telegram bot token to .env file
  - Run `python3 main.py`.
  - (Optional) To keep the code running without interruption you can use a VPS and [tmux](https://github.com/tmux/tmux/wiki)
````
