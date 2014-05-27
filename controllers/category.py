# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Category"
    response.subtitle="Jenis-jenis category di terima"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.category)
    return locals()
