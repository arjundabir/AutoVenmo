# import Venmo API from https://github.com/mmohades/venmo

from venmo_api import Client
import os

venmo_client = os.environ.get("VENMO_CLIENT")

access_token = Client.get_access_token(username=os.environ.get("VENMO_USERNAME"),
                                       password=os.environ.get("VENMO_PASSWORD"))

# initialize client
client = Client(access_token=access_token)

# find your friend's id. Look for extra docuementation from link above
users = client.user.search_for_users(query=venmo_client)
user = users[0].id

# find your approved payment methods. Look for extra docuementation from link above
payment_methods = client.payment.get_payment_methods()
bank_id = payment_methods[1].id

# complete transaction. Look for extra docuementation from link above. You can request or send.
client.payment.send_money(0.01, "testing code", user)

client.log_out("Bearer " + access_token)
