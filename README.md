# Gmail Auto-replier bot
This script replies any gmail that contains the keywords specified in `temp.tm`.

Note: this only works in Gmail, but you are free to give support to others emails providers.

## How to use
1. Install the dependencies using:

`pip install -r requirements.txt` or

`pip3 install -r requirements.txt`

2. Then you need to configure the script:

In `temp.tm`:

- `email` put your full email.

- `password` put your password.

- `keywords` put the keywords, the script will evaluate if all of these are in the email, the default are "worried" and "mother".

- `white_list` put the emails that only will replied.

- `data_emails` put the content of the replies.

- Then go to https://myaccount.google.com/lesssecureapps and click at yes, otherwise this script won't work.

3. Run the script with:

`python main.py` or

`python3 main.py`

## How to contribute
Have an idea? Please use a branch and create a Pull Request. If you not sure how to do this, ask us.

Haven't time to code it? Please open an issue.

## License
Licensed under a MIT license.