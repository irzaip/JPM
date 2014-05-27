# coding: utf8
# try something like
def index(): 
    response.title="WorkOrder"
    response.subtitle="Melihat surat perintah kerja ke supplier"
    response.view="generic.html"
    
    tbl = SQLFORM.grid(db.workorder)
    return locals()
