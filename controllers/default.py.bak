# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import datetime

@auth.requires_login()
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    now=datetime.datetime.now()
    #db.todo.insert(tanggal=now,keterangan="Tanggal",status_pekerjaan="1",priority="1",url="/jpm/")

    response.flash = "Selamat menggunakan JPM"
    response.title = "JPM"
    response.subtitle="Juragan Property Millenium"


    
    #delete todo list
    query = (db.todo.id > 0)
    set = db(query)
    set.delete()
    
    #check room available
    query = (db.unit.available == True)
    set = db(query)
    rows = set.select()
   
    for row in rows: 
      db.todo.insert(tanggal=now,priority=4,keterangan=CAT('Jual ',row.nama_unit),status_pekerjaan=7,url=URL('unit','index'))

    todo = db((db.todo.id > 0) & (db.priority.id == db.todo.priority) & (db.status_pekerjaan.id == db.todo.status_pekerjaan)).select()
    
    return dict(todo=todo,bows=rows)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    response.title="Please Login"
    response.subtitle="Anda harus log-in untuk memakai system ini"
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
