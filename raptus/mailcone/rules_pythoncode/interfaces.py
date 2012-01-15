from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules_pythoncode import _
from raptus.mailcone.rules import interfaces





class IPythonCodeItem(interfaces.IConditionItem):
    """ Interface for simple match filter
    """

    code = schema.Text(title=_('Code'),
                       required=True,
                       description=_('python Code'))
