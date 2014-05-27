# coding: utf8
# try something like
@auth.requires_login()
def index():
    response.title = "Daftar Nama Vendor"
    response.subtitle= "mencakup semua vendor yang kita gunakan."
    
    dbref=db 
    qry=(db.vendor)
    headers=['Nama Usaha','Nama Kontak','No Tel Kantor','No Tel Kontak']
    fields=['nama_usaha','nama_kontak','no_tel_kantor','no_tel_kontak'] 
    sel=[db.vendor[field] for field in fields] 
    #rows=SQLTABLE(dbref(qry).select(*sel))
    rows=db(db.vendor).select()
    return dict(rows=rows,headers=headers)


@auth.requires_login()
def add():
    response.title="Tambahkan Vendor"
    response.subtitle="Bagaimanapun juga anda harus menambah vendor sebagai rekanan anda."
    form=SQLFORM(db.vendor,submit_button="Tambahkan Vendor")
        
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)
    

@auth.requires_login()
def edit():
    response.title="Edit Vendor"
    response.subtitle="Merubah data vendor"
    
    ids = request.args[0]
    vendor = db(db.vendor.id==ids)
    if not vendor: raise HTTP(404)
    
    return dict(form=crud.update(db.vendor,ids))
    
    
@auth.requires_login()
def view():
    response.title="Detail Vendor"
    response.subtitle="Melihat detail informasi vendor"
    
    ids = request.args[0]
    vendor = db(db.vendor.id==ids)
    if not vendor: raise HTTP(404)
    
    return dict(form=crud.read(db.tenant,ids))
