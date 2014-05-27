# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Building"
    response.subtitle="Nama-nama building yang dikelola"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.building)
    return locals()
