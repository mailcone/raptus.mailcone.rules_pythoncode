import grok

from zope import component
from zope.schema.fieldproperty import FieldProperty
from raptus.mailcone.rules import contents
from raptus.mailcone.rules_pythoncode import interfaces





class PythonCodeItem(contents.BaseConditionItem):
    grok.implements(interfaces.IPythonCodeItem)
    code = FieldProperty(interfaces.IPythonCodeItem['code'])


    def check(self, mail):
        setattr(mail, 'result', False)
        locals = dict(mail=mail)
        globals = dict()

        exec (self.code, locals, globals)

        return mail.result
