# coding=utf-8
import random
from PyQt5.QtCore import QObject

from qutebrowser.commands import cmdutils


class HelloQute(QObject):
    from qutebrowser.utils import message
    from qutebrowser.utils import objreg
    message = message  # Makes IDE / linter happy.
    objreg = objreg

    @cmdutils.register(instance='hello')
    def hello(self, name=None):
        """Hello!"""
        if not name:
            name = 'World'
        name = name.capitalize()
        dispatcher = self.objreg.get('command-dispatcher', scope='window', window='current')
        dispatcher.openurl('http://example.com')
        self.message.info('Hello, {}!'.format(name))

    @cmdutils.register(instance='hi')
    def hi(self, name=None):
        """Hi!"""
        return self.hello(name)


Plugin = HelloQute
commands = ['hello', 'hi']
