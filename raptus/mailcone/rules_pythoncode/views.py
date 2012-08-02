import os
import grok

from zope import component
from zope import interface
from zope import schema

from grokcore.view.interfaces import ITemplateFileFactory

from raptus.mailcone.layout.views import AddForm
from raptus.mailcone.rules.wireit import RuleBoxEditForm
from raptus.mailcone.mails.interfaces import IMail, IAttachment, ITag

from raptus.mailcone.rules_pythoncode import _
from raptus.mailcone.rules_pythoncode import interfaces


grok.templatedir('templatess')



class CodeEditForm(AddForm):
    grok.baseclass()
    prefix = 'properties'
    form_fields = grok.AutoFields(interfaces.IPythonCodeItem).select('code')


class DocInterface(grok.View):
    grok.baseclass()
    
    def __init__(self, interface, request):
        super(DocInterface, self).__init__(interface, request)
        self.interface = interface
        self.request = request
        filepath = os.path.join(os.path.dirname(__file__),'templates','docinterface.cpt')
        self.template = component.getUtility(ITemplateFileFactory, name='cpt')(filename=filepath)
    
    @property
    def name(self):
        return self.interface.getName()
    
    @property 
    def doc(self):
        return self.interface.getDoc()
    
    @property
    def fields(self):
        for name in self.interface:
            field = self.interface[name]
            if schema.interfaces.IField.providedBy(field):
                value_type = ''
                if hasattr(field, 'value_type'):
                    if field.value_type._type is not None:
                        value_type = field.value_type._type.__name__
                    if getattr(field.value_type, 'schema', None) is not None:
                        value_type = field.value_type.schema.getName()
                if isinstance(field._type, (tuple, list,)):
                    type = '/'.join([i.__name__ for i in field._type])
                else:
                    type = field._type.__name__
                yield dict(name=field.getName(),
                           type=type,
                           description=field.description,
                           value_type=value_type)
                continue

            if callable(field):
                yield dict(name=name,
                           type='function',
                           description=field.__doc__,
                           value_type=value_type)
                continue

            if isinstance(field, interface.Attribute):
                yield dict(name=name,
                           type='attribute',
                           description='zope.interface.Attribute',
                           value_type='')
                continue




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
        tabs.append(dict(id='ui-tabs-desc',
                    title=_('Desc'),
                    html=DocInterface(IMail, self.request)() +
                         DocInterface(IAttachment, self.request)() +
                         DocInterface(ITag, self.request)()))
        return tabs




