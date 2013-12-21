#!/usr/bin/env python

import os
import shutil
import subprocess
import sys
import time
import urllib2


PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DEMO_DIR = os.path.join(PROJECT_DIR, 'demo')


def _start_sentry(bindir, sitepackages, envname):
    # prepare test config
    shutil.copy(os.path.join(DEMO_DIR, 'sentry.conf.py'),
                os.path.join(DEMO_DIR, 'sentry_test.conf.py'))
    config = os.path.join(DEMO_DIR, 'sentry_test.conf.py')
    with open(config, 'a') as f:
        f.write('\n')
        f.write("EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'\n")
        f.write("EMAIL_FILE_PATH = '/tmp/test-mails-{}'\n".format(envname))
    conf_arg = '--config={}'.format(config)
    # setup DB
    sentry = os.path.join(bindir, 'sentry')
    if os.path.exists(os.path.join(DEMO_DIR, 'sentry.db')):
        os.remove(os.path.join(DEMO_DIR, 'sentry.db'))
    subprocess.check_call([sentry, conf_arg, 'syncdb', '-v', '0',
                           '--all', '--noinput'])
    subprocess.check_call([sentry, conf_arg, 'migrate', '--fake', '-v', '0'])
    if envname in ('sentry60', 'sentry61', 'sentry62', 'sentry63'):
        fname = 'demo_user.json'
    else:
        fname = 'demo_user64.json'
    subprocess.check_call([
        sentry, conf_arg, 'loaddata',
        os.path.join(PROJECT_DIR, 'tests', fname)]
    )
    coverage = os.path.join(bindir, 'coverage')
    p_sentry = subprocess.Popen(
        [coverage, 'run', '--source={}/sentry_comments'.format(sitepackages),
         sentry, conf_arg, 'start', '-v', '0'])
    # wait for Sentry to come up
    start = time.time()
    timeout = start + 10
    while time.time() < timeout:
        try:
            urllib2.urlopen('http://localhost:9000')
            return p_sentry
        except urllib2.URLError:
            time.sleep(.1)
    else:
        sys.stderr.write('Could not connect to Sentry :(\n')
        return None


def _start_pybot(bindir, envname):
    results_dir = os.path.join(PROJECT_DIR, 'test_results')
    output_dir = os.path.join(results_dir, envname)
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    pybot = os.path.join(bindir, 'pybot')
    return subprocess.Popen([
        pybot, '--outputdir={}'.format(output_dir),
        '--variable', 'INBOX:/tmp/test-mails-{}'.format(envname),
        os.path.join(PROJECT_DIR, 'tests')
    ])


def main(bindir, envname, sitepackages):
    p_sentry = None
    try:
        p_sentry = _start_sentry(bindir, sitepackages, envname)
        if p_sentry is None:
            return 1
        p_pybot = _start_pybot(bindir, envname)
        if p_pybot is None:
            return 1
        return p_pybot.wait()
    finally:
        if p_sentry is not None:
            p_sentry.terminate()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3]))
