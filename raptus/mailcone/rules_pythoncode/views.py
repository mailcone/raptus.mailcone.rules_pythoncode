import grok

from raptus.mailcone.layout.views import AddForm
from raptus.mailcone.rules.wireit import RuleBoxEditForm

from raptus.mailcone.rules_pythoncode import _
from raptus.mailcone.rules_pythoncode import interfaces





class CodeEditForm(AddForm):
    grok.baseclass()
    prefix = 'properties'
    form_fields = grok.AutoFields(interfaces.IPythonCodeItem).select('code')



class RuleBoxEditForm(RuleBoxEditForm):
    grok.name('wireit_edit_raptus_mailcone_pythoncode')
    
    @property
    def tabs(self):
        tabs = super(RuleBoxEditForm, self).tabs
        for tab in tabs:
            if tab.get('id') == 'ui-tabs-overrides':
                tab['id'] = 'ui-tabs-code'
                tab['title'] = _('Code')
                tab['html'] = CodeEditForm(self.context, self.request)()
        return tabs