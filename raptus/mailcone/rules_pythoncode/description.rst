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

Usage
-----
Use the instance variable "mail" to get access on the actual processed mail. You are
free to use every import include in this application.
At the end you should set "mail.result" which False or True to define the output flow.

Variable
--------

mail
    mail.
    mail
