from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules import interfaces
from raptus.mailcone.layout.formlib import CodeField

from raptus.mailcone.rules_pythoncode import _





class IPythonCodeItem(interfaces.IConditionItem):
    """ Interface for simple match filter
    """

    code = CodeField(title=_('Code'),
                     required=True,
                     description=_('python Code'),
                     mode='python')
