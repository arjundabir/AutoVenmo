# Send a Venmo Request

Send a request or payment to your on Venmo using "venmo-api" (from https://github.com/mmohades/venmo)

## Installation

1. You can install or upgrade using:

```bash
$ pip3 install venmo-api --upgrade
```

2. Set up environment variables

```bash
$ python3 -m venv env
```

3. Set up environments variables

## Environment Variables

```bash
$ export VENMO_USERNAME=<enter_your_venmo_username_here@example.com>
$ export VENMO_PASSWORD=<enter_your_venmo_password_here>
$ export VENMO_CLIENT=<enter_your_venmo_client's_user>
```

Check if Environment Variables are set up correctly

```bash
$ echo $VENMO_USERNAME
$ echo $VENMO_PASSWORD
$ echo $VENMO_CLIENT
```

## Usage

1. Run in the virtual environment

```bash
$ source env/bin/activate
```

2. Run python script

```bash
$ python app.py
```

If you want to automate:

## Set up Automation (on Mac/Linux)

We will be using cron to run automatic scripts

1. Make script executable by users

(in directory of your python file)

```bash
$ chmod +x venmo_script.sh
```

2. In terminal (from ~ directory), access your crontab (cron table). We will be using vim text editor do this

```bash
$ crontab -e
```

3. Using the guide below or crontab.guru enter this in your VIM editor on terminal.
   Notes: Start by pressing "I" on your keyboard to go on insert mode.

┌───────────── minute (0 - 59)

│ ┌───────────── hour (0 - 23)

│ │ ┌───────────── day of month (1 - 31)

│ │ │ ┌───────────── month (1 - 12)

│ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;

│ │ │ │ │ 7 is also Sunday on some systems)

│ │ │ │ │

│ │ │ │ │

\* \* \* \* \* command_to_execute

```vim
* * * * * /bin/bash ~/path/to/venmo_script.sh
```

4. Press <kbd>esc</kbd> on your keyboard and then <kbd>:</kbd> + <kbd>W</kbd> + <kbd>Q</kbd> and finally hit <kbd>Enter</kbd>

5. Good job, you're done!
