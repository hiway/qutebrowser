# coding=utf-8
from qutebrowser.commands import cmdutils
from qutebrowser.plugins import Plugin


class EchoPlugin(Plugin):
    _name = 'echo_plugin'

    @cmdutils.register(instance=_name, name='echo')
    def echo(self, *text_words):
        """
        Example of a trivial qutebrowser plugin.
        - Expects: text words: each argument is
            a tokenized word from qutebrowser command.
        - Returns: echoes the text, as command
        """
        text = ' '.join(text_words)  # Get a string from list.
        self.message.info(text)
