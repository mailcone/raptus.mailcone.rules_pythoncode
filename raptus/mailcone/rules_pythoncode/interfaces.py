from zope import schema
from zope import interface
from zope import component

from raptus.mailcone.rules import interfaces
from raptus.mailcone.layout.formlib import CodeField

from raptus.mailcone.rules_pythoncode import _


example = u"""
import re

class ValidateEmail(object):

    p = r'^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$'
    pattern = re.compile(p)

    def __init__(self, mail):
        self.mail = mail

    def valid(self):
        if self.mail.mail_from:
            if self.pattern.match(self.mail.mail_from):
                mail.result = True
                return
        mail.result = False

ve = ValidateEmail(mail)
ve.valid()
"""


class IPythonCodeItem(interfaces.IConditionItem):
    """ Interface for simple match filter
    """

    code = CodeField(title=_('Code'),
                     required=True,
                     description=_('python Code'),
                     mode='python',
                     default=example)






