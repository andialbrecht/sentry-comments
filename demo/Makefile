install: bin/sentry
	@echo "Next steps:"
	@echo " 1. Run 'bin/sentry --config=sentry.conf.py start' to start sentry"
	@echo " 2. Open another shell and"
	@echo "    - Run 'bin/sentry --config=sentry.conf.py send_fake_data'"
	@echo "    - Hint: Hit Ctrl-C to stop populating the database with fake data."
	@echo " 3. Open http://localhost:9000"


bin/sentry: bin/pip
	bin/pip install ../

bin/pip:
	virtualenv .


clean:
	rm -rf bin/ include/ lib/ local/ share/
	rm -f sentry.db
