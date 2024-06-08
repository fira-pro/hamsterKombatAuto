# Hamster Kombat Bot Automation Tool

## A tool to automate the Hamster Kombat Telegram bot, enabling the collection of coins and other tasks without manually interacting with the bot.

Collects coins🪙 generated passively every 3 hours, claims daily streak, Morse code cipher daily bonus and send notification to Telegram bot🤖

![image](https://github.com/fira-pro/hamsterKombatAuto/assets/85739903/ef2bfd5c-4f93-4d1c-86eb-155b0dcb9297)

## What This Code Can Do

- **Collect passive coins**: Automatically collects passively generated coins every 3 hours based on the _profit per hour_ rate⏲️.
- **Claim daily streak📆**: Automatically claims the daily streak bonus. The streak resets to day 1 after 10 days and a 5M coin bonus.
- **Daily cipher**: Automatically solves and claims the daily Morse code cipher bonus, using the code available in the API response.
- **Notifications**: Sends notifications to a specified Telegram bot with details of the collected coins.
- **Multiple accounts**: Supports multiple Telegram accounts. See the [access_tokens.json](access_tokens.json) file for setup.

## TODO

- [ ] Implement feature to receive the daily combo card list and claim a 5M coin bonus🔥.

## How to use

- **_To use this code_**:

  - Obtain the **Authorization token** used by the Hamster Kombat API. This requires performing a **Man In The Middle (MITM)** attack on the Telegram app while interacting with the Hamster Kombat bot miniApp.
  You can achieve this using any Android emulator with ADB enabled and root access in conjunction with HTTP Toolkit. Follow HTTP Toolkit's guide [here](https://httptoolkit.com/docs/guides/android/). (A detailed tutorial will be added soon😄)

    <img width="760" alt="image" src="https://github.com/fira-pro/hamsterKombatAuto/assets/85739903/7d858eb1-fdae-493f-9b3a-d26a92e1f5f7">

  - **[Optional]** Obtain your Telegram Bot Token via [@BotFather](https://t.me/botfather). If you prefer not to use this feature, comment out all calls to the `notify(args*)` function in main.py.

- ### Installation

  - Clone this repo: `git clone https://github.com/fira-pro/hamsterKombatAuto.git` and `cd hamsterKombatAuto`
  - Install required packages: `pip install -r requirements.txt`
  - Add your access tokens to the file access_tokens.json array

  ```json
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

  - Add your Telegram bot token to a .env file

  ```shell
  BOT_TOKEN=bot12345678:123abcd
  ```

  - Run `python3 main.py`.
  - To keep the script running continuously, consider using a VPS with [tmux](https://github.com/tmux/tmux/wiki)

> [!NOTE]
> This project was developed in a short period and may contain bugs or incomplete features. Please use with caution and report any issues you encounter.

## Contributing

Want to help? I'd love to have you! Feel free to fix bugs or add new features. Just fork the repository, make your changes, and send me a pull request. Thanks for contributing!

## Contact

**Telegram**: [fira_pro](https://t.me/fira_pro)
