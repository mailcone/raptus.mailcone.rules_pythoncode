import grok

from raptus.mailcone.core import utils

from raptus.mailcone.rules import interfaces
from raptus.mailcone.rules.factories import BaseFactoryCondition


from raptus.mailcone.rules_pythoncode import _
from raptus.mailcone.rules_pythoncode.interfaces import IPythonCodeItem
from raptus.mailcone.rules_pythoncode.contents import PythonCodeItem



class PythonCodeFactory(BaseFactoryCondition):
    grok.name('raptus.mailcone.rules.pythoncode')
    grok.implements(interfaces.IConditionItemFactory)
    
    
    title = _('Python code')
    description = _('The rule is defined via a specific python code.')
    form_display = grok.AutoFields(IPythonCodeItem).omit('code')
    form_fields = grok.AutoFields(IPythonCodeItem)
    ruleitem_class = PythonCodeItem

    def box_edit(self):
        return grok.url(utils.getRequest(), self.context, 'wireit_edit_raptus_mailcone_pythoncode')