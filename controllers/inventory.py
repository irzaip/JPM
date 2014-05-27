# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title="Inventory"
    response.subtitle="Barang-barang yang tersedia di unit kamar"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.inventory)
    return locals()
