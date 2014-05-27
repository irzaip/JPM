# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Status Pekerjaan"
    response.subtitle="Jenis-jenis status pekerjaan di terima"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.status_pekerjaan)
    return locals()
