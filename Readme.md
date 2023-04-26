# Telegram Group Message Sender

This script allows you to send a message to all the groups and channels your Telegram account is a member of, with a specified time delay between each message. The script uses the Telethon library to interact with the Telegram API.

## Setup

1. Clone this repository and navigate to the project directory.

2. Create a virtual environment and activate it:

```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:

```sh
pip install -r requirements.txt
```

4. Obtain your Telegram API ID, API hash, and phone number. Sign up for a new developer account on Telegram's official website: https://my.telegram.org/auth. After signing in, create a new application to obtain your API ID and API hash.

5. Create a `config.py` file in the `root` directory and add the following content:

```python
YOUR_API_ID = "your_api_id_here"
YOUR_API_HASH = "your_api_hash_here"
YOUR_PHONE_NUMBER = "your_phone_number_here"  # with country code, e.g., '+1234567890'
MESSAGE = "your_message_here"
GROUPS = "groups listed here with '\n' separator"
```

Replace `your_api_id_here`, `your_api_hash_here`, `your_phone_number_here`, and `your_message_here` with your own credentials and the message you want to send. Adjust the `DELAY` variable to set the time delay between messages (in seconds).

## Usage

To run the script, simply execute the following command in the terminal:

```sh
python main.py
```

The script will send the specified message to all the groups and channels your Telegram account is a member of, with the specified time delay between each message.

## Disclaimer

Please note that sending too many messages in a short period may result in temporary restrictions or account limitations imposed by Telegram. Be cautious and make sure you respect the platform's rules and guidelines.
```
