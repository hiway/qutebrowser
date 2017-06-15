# coding=utf-8
from qutebrowser.commands import cmdutils
from qutebrowser.plugins import Plugin


class MetaSearch(Plugin):
    _name = 'meta_search'

    @cmdutils.register(instance=_name, name='ms')
    def meta_search(self, *text_words):
        """
        An example plugin.
        Searches query in multiple search engines.
        """
        dispatcher = self.dispatcher
        text = ' '.join(text_words)  # Get a string from list.
        dispatcher.openurl('https://duckduckgo.com/?q={}'.format(text), tab=True)
        dispatcher.openurl('https://google.com/?q={}'.format(text), tab=True)
