import os

from raven import Client


def generate_event(msg, dsn):
    client = Client(dsn)
    client.captureMessage(msg)


def clear_inbox(maildir):
    print('Clearing inbox at {}'.format(maildir))
    if not os.path.isdir(maildir):
        return
    for fname in os.listdir(maildir):
        os.remove(os.path.join(maildir, fname))


def inbox_should_contain_num_mails(maildir, count):
    print('Testing if inbox at {} has {} items.'.format(maildir, count))
    count = int(count)
    nmails = len(os.listdir(maildir))
    if nmails != count:
        raise AssertionError(
            'Inbox should contain {} messages, but has {}.'.format(
                count, nmails)
        )


def mail_should_contain_text(maildir, num, text):
    print('Testing if mail {} in {} contains text {}.'.format(
        num, maildir, text))
    mails = os.listdir(maildir)
    num = int(num)
    if len(mails) < num:
        raise AssertionError('Not enough mails in inbox (found {}).'.format(len(mails)))
    fname = mails[num - 1]
    with open(os.path.join(maildir, fname)) as f:
        content = f.read()
    if not text in content:
        raise AssertionError('Mail does not contain text.')
