# coding=utf-8
from PyQt5.QtCore import QObject
from qutebrowser.commands import runners


class Plugin(QObject):
    from qutebrowser.utils import message
    from qutebrowser.utils import objreg
    from qutebrowser.commands import cmdutils
    message = message  # Makes IDE / linter happy.
    objreg = objreg
    cmdutils = cmdutils

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _register(self):
        self.objreg.register(self._name, self)

    @property
    def dispatcher(self, scope='window', window='current', tab=None):
        return self.objreg.get('command-dispatcher', scope=scope, window=window, tab=tab)

    @staticmethod
    def run_command(text):
        commandrunner = runners.CommandRunner(0)
        commandrunner.run(text)
