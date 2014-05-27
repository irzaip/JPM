# coding: utf8
# try something like

@auth.requires_login()
def index():
    response.title = "Daftar Nama Tenant"
    response.subtitle= "mencakup semua tenant lampau/pelanggan/prospek."
    #response.view="main.html"
    
    dbref=db 
    qry=(db.tenant.id>0) & (db.status.id==db.tenant.status)
    headers=['Nama','Alamat','Status']
    fields=['nama_lengkap','alamat_lengkap','status'] 
    sel=[db.tenant[field] for field in fields] 
    #rows=SQLTABLE(dbref(qry).select(*sel))
    rows=db((db.tenant.id>0) & (db.status.id==db.tenant.status)).select(db.tenant.id, db.tenant.nama_lengkap, db.tenant.alamat_lengkap, db.status.status)
    return dict(rows=rows,headers=headers)

@auth.requires_login()
def edit():
    response.title="Edit Tenant"
    response.subtitle="Merubah data Tenant"
    
    ids = request.args[0]
    tenant = db(db.tenant.id==ids)
    if not tenant: raise HTTP(404)
    
    return dict(form=crud.update(db.tenant,ids))

@auth.requires_login()
def add():
    response.title="Tambahkan tenant"
    response.subtitle="Bagaimanapun juga anda harus menambah tenant sekarang juga."
    form=SQLFORM(db.tenant,submit_button="Tambahkan Tenant")
        
    if form.accepts(request,session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'
    return dict(form=form)


@auth.requires_login()
def checkin():
    response.title="Check-in tenant"
    response.subtitle="Isi data tenant secara lengkap."
    form=SQLFORM(db.tenant,submit_button="Check-in Tenant")
    
    #apabila dari booking
    if request.vars.tenant > 1:
      form.vars = db.tenant[request.vars.tenant]
      #isi menjadi pelanggan
      form.vars.status = 3
        
    if form.accepts(request,session):
        response.flash = 'Berhasil'
        
        #update tenant di tabel unit
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(tenant=form.vars.id,available=False)
        
        redirect(URL('unit','index'))
        
        
    elif form.errors:
        response.flash = 'Ada kesalahan pengisian'
    else:
        response.flash = 'isi form dibawah ini'
    return dict(form=form)


@auth.requires_login()
def booking():
    response.title="Booking tenant"
    response.subtitle="Isi data tenant secara lengkap."
    form=SQLFORM(db.tenant,submit_button="Booking Tenant")
    
    #buat status potensial
    form.vars.status=1    
    
    if form.accepts(request,session):
        response.flash = 'Berhasil'
        
        #update tenant di tabel unit
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(tenant=form.vars.id,available=False,booked=True)
        
        redirect(URL('unit','index'))
        
        
    elif form.errors:
        response.flash = 'Ada kesalahan pengisian'
    else:
        response.flash = 'isi form dibawah ini'
    return dict(form=form)

@auth.requires_login()
def confirm():
    response.title="Konfirmasi Check-IN"
    response.subtitle="Apakah yakin Pelanggan ini Menetap?"
    
    form = SQLFORM.factory(Field('checkin','boolean'))
    btn = form.element("input",_type="submit")
    btn["_onclick"] = "return confirm('Apakah anda Yakin?');"
    
    if form.accepts(request,session):
        response.flash="Berhasil Check-IN"
        
        #update available dan booking
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(available=False,booked=False)
        
        #update status tenant ke pelanggan
        query = (db.tenant.id == request.vars.tenant)
        set = db(query)
        set.update(status=3)
        
        redirect(URL('unit','index'))
        
    return dict(form=form)

    
@auth.requires_login()
def checkout():
    response.title="Konfirmasi Check-Out"
    response.subtitle="Apakah yakin Pelanggan ini Keluar?"
    
    form = SQLFORM.factory(Field('checkout','boolean'))
    btn = form.element("input",_type="submit")
    btn["_onclick"] = "return confirm('Apakah anda Yakin?');"
    
    if form.accepts(request,session):
        response.flash="Berhasil Checkout"
        
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(tenant=1,available=True,booked=False)
        
        query = (db.tenant.id == request.vars.tenant)
        set = db(query)
        set.update(status=4)
        
        redirect(URL('unit','index'))
        
    return dict(form=form)


@auth.requires_login()
def bookcancel():
    response.title="Membatalkan booking"
    response.subtitle="Apakah yakin Pelanggan ini Membatalkan?"
    
    form = SQLFORM.factory(Field('cancel','boolean'))
    btn = form.element("input",_type="submit")
    
    if form.accepts(request,session):
        response.flash="Berhasil Membatalkan"
        
        #membatalkan booking
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(tenant=1,available=True,booked=False)
        
        query = (db.tenant.id == request.vars.tenant)
        set = db(query)
        set.update(status=4)
        
        redirect(URL('unit','index'))
        
    return dict(form=form)
    
    
@auth.requires_login()
def view():
    response.title="Detail Tenant"
    response.subtitle="Melihat detail informasi Pelanggan"
    
    ids = request.args[0]
    tenant = db((db.tenant.id==ids) & (db.status.id == db.tenant.status)).select()
    if not tenant: raise HTTP(404)
    
    query = (db.unit.tenant == tenant[0].tenant.id)
    set = db(query)
    rows = set.select()
    if not rows: 
      unit = 0
    else: 
      unit = rows[0].id
    
    #lihat kontrak sewa
    lease = db((db.lease.tenant==ids) & (db.frequency.id == db.lease.frequency)).select()
    
    #lihat pembayaran dan akunting
    accounting = db(db.accounting.tenant==ids).select()
        
    return dict(tenant=tenant,lease=lease,unit=unit,accounting=accounting,ids=ids)
