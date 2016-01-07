# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.title = ' '.join(word.capitalize() for word in request.application.split('_'))
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'IRZA PULUNGAN <irzaip@gmail.com>'
response.meta.description = 'App for Landlords'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'
response.meta.copyright = 'Copyright 2011'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default','index'), []),
    (T('Todo'), False, URL('default','index'), []),
    (T('Unit'), False, URL('unit','index'),[]),
    (T('Tenant'), False, URL('tenant','index'),[])
    ]
    
#if auth.user and auth.has_membership(role='manager'):
#     response.menu.append()
