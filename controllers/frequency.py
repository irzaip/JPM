# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Frequency"
    response.subtitle="Jenis-jenis frequency pembayaran"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.frequency)
    return locals()
