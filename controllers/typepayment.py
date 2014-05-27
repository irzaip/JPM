# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Type Payment"
    response.subtitle="Jenis-jenis payment yang di terima"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.typepayment)
    return locals()
