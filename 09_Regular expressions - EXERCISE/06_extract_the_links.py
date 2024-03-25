import re

command = input()

import re

pattern = r"\bw{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
emails = []

while command:
    current_emails = [el.group() for el in re.finditer(pattern, command)]
    emails.extend(current_emails)
    command = input()

for email in emails:
    print(email)