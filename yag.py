import os
import random
import yagmail

from datetime import datetime

yag = yagmail.SMTP(
    os.environ['NOTIFY_GMAIL_UNAME'],
    os.environ['NOTIFY_GMAIL_APP_PASS']
)

path = os.path.dirname(__file__)

with open(os.path.join(path, 'aphorisms.txt'), 'r') as aph:
    aphorisms = [line.rstrip() for line in aph.readlines()]

with open(os.path.join(path, 'leonardo.txt'), 'r') as leo:
    leonardos = [line.rstrip() for line in leo.readlines()]

# The author recommends reading no more than four aphorisms in one sitting.
# It is also preferable to select these randomly.
random.shuffle(aphorisms)
random.shuffle(leonardos)

contents = [
    'Your daily dose of aphorisms, courtesy of Nassim Nicholas Taleb:',
    '\n',
    f'1. {aphorisms[0]}',
    f'2. {aphorisms[1]}',
    f'3. {aphorisms[2]}',
    f'4. {aphorisms[3]}',
    '\n',
    'And another three, courtesy of Leonardo da Vinci:',
    '\n',
    f'1. {leonardos[0]}',
    f'2. {leonardos[1]}',
    f'3. {leonardos[2]}',
]

date = datetime.today().strftime('%d/%b/%Y')
subject = f'Aphorisms. {date}'

with open(os.path.join(path, 'emails.txt'), 'r') as adrs:
    emails = [line.strip() for line in adrs.readlines()]

yag.send(emails, subject, contents)
