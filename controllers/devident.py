# coding: utf8

@auth.requires_login()
def index():
    response.title="Devident"
    response.subtitle="devident penerimaan dari tiap gedung"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.devidend)
    return locals()
