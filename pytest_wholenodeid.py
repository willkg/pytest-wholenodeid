import sys

from _pytest.terminal import TerminalReporter
import pytest


__version__ = '0.1'
__releasedate__ = '20150826'


class WholeNodeIDTerminalReporter(TerminalReporter):
    def _getfailureheadline(self, rep):
        if hasattr(rep, 'location'):
            fspath, lineno, domain = rep.location
            # Use the whole nodeid so you can copy/paste it to run the test
            return '::'.join([fspath, domain.replace('.', '::')])
        else:
            return "test session"


def pytest_addoption(parser):
    group = parser.getgroup("terminal reporting", "reporting", after="general")
    group._addoption(
        '--nowholenodeid', action="store_false", dest="wholenodeid", default=True,
        help=(
            "disable pytest-wholenodeid"
        )
    )


@pytest.mark.trylast
def pytest_configure(config):
    if config.option.wholenodeid:
        # Get the standard terminal reporter plugin and replace it with our
        standard_reporter = config.pluginmanager.getplugin('terminalreporter')
        wholenodeid_reporter = WholeNodeIDTerminalReporter(config, sys.stdout)
        config.pluginmanager.unregister(standard_reporter)
        config.pluginmanager.register(wholenodeid_reporter, 'terminalreporter')
