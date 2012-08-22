Python code Rule
================

Description
-----------

This Rule allow to define a rule with a python code snippet. Defined Python code
will first compiled with local variables and than executed.

The code runs like a python module. Its means you can use directly expressions
(if, for, while) or methods. Classes are also accepted and compiled.

Take care, this is not restricted python while using executed python code you
have full access on the whole application!
Never use pdb, is not working!

Usage
-----
Use the instance variable "mail" to get access on the actual processed mail. You are
free to use every import include in this application.
At the end you should use the method "**match**" to define the rest of the workflow. True
is default. e.g. "**match()**" "**match(False)**"

Example
-------
    
python snippet to check a email address of validity::

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
