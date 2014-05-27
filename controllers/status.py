# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Status"
    response.subtitle="Jenis-jenis status yang di terima"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.status)
    return locals()
