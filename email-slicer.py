# Modules.
import socket as s
from colorama import Fore, Style

# Prompts you to enter an email address.
email = input("Enter Email Address: ").strip()

# Slices string to grab the username of the email address.
username = email[:email.index('@')]

# Slices string to grab the domain name of the email address.
domain = email[email.index('@') + 1:]

# The value of the variable url is domain; which would be the domain name after the @ symbol in the email address.
url = domain

# Format message.
# The triple double quotes allows the string to print to multiple lines in a single statement.
# The variable url now acts as an argument for the gethostbyname() function.
# The gethostname() function uses the domain name as an argument to get the IP address of the host.
results = (f"""
Email Address: {email}
Username: {username}
Domain: {domain}
Domain IP Address: {s.gethostbyname(url)}
""")

# Prints the results in a bright green font, then resets the color and brightness on program exit.
print(Fore.GREEN + Style.BRIGHT + results + Fore.RESET + Style.RESET_ALL)
