# -*- coding: utf-8 -*-
# try something like
def index(): 
    
  response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('Unit'), False, URL('unit','index'),[]),
    (T('Tenant'), False, URL('tenant','index'),[]),
    (T('Contract'),False,None,[
        (T('Workorder'), False, URL('workorder','index'),[]),
        (T('Lease'), False, URL('lease','index'),[]),
        (T('Vendor'), False, URL('vendor','index'),[]),
        (T('ToDo'), False, URL('todo','index'),[]),
        ]),
    (T('Report'),False,None,[
        (T('Invoice'),False,URL('invoice','index'),[]),
        (T('Receipt'),False,URL('receipt','index'),[]),
        (T('Accounting'),False,URL('accounting','index'),[]),
    ]),
    ]

  return dict(message="hello from admin.py")
