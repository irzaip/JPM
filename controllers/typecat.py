# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Type Category"
    response.subtitle="Jenis-jenis kategori di terima"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.typecat)
    return locals()
