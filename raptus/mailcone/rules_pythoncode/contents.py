import sys
import grok
import traceback

from zope import component
from zope.schema.fieldproperty import FieldProperty

from codeop import Compile

from raptus.mailcone.rules import contents
from raptus.mailcone.rules import exceptions
from raptus.mailcone.rules_pythoncode import interfaces


class Functions(object):
    namespace = None

    def match(self, r=True):
        self.namespace['result'] = r


class PythonCodeItem(contents.BaseConditionItem):
    grok.implements(interfaces.IPythonCodeItem)
    code = FieldProperty(interfaces.IPythonCodeItem['code'])

    def before_check(self):
        try:
            self._v_compile = Compile()(self.code, '<python code rule>', 'exec')
        except Exception, e:
            self.raise_ex(e)
    
    def check(self, mail):
        
        namespace = dict(result=False)

        functions = Functions()
        functions.namespace = namespace
        
        locals = dict(mail=mail,
                      match=functions.match,
                      __python_code_rule_ns__ = namespace,
                      __name__= '__python_code_rule__',
                      __doc__ = None)
        try:
            exec self._v_compile in locals
        except Exception, e:
            self.raise_ex(e)
        return namespace['result']

    def raise_ex(self, e):
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tblist = traceback.extract_tb(exc_traceback)
        # We remove the first stack item because it is our own code.
        filename, line_number, function, text =tblist.pop(1)
        msg = '\nlineno: %s\n%s' % (line_number, str(e),)
        raise exceptions.RuleItemException(msg, self)

