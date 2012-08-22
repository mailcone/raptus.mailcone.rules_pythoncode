from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules import interfaces
from raptus.mailcone.layout.formlib import CodeField

from raptus.mailcone.rules_pythoncode import _


example = u"""
import re
PATTERN = re.compile('^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$')

class ValidateEmail(object):

    def __init__(self, mail):
        self.mail = mail

    def validate(self):
        address = (self.mail.mail_from.split(' ') + [None]).pop(0)
        if address and PATTERN.match(address):
            match()

ve = ValidateEmail(mail)
ve.validate()
"""


class IPythonCodeItem(interfaces.IConditionItem):
    """ Interface for simple match filter
    """

    code = CodeField(title=_('Code'),
                     required=True,
                     description=_('python Code'),
                     mode='python',
                     default=example)






