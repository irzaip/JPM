# coding: utf8
# try something like
@auth.requires_login()
def index():
    response.title="Accounting"
    response.subtitle="Entry GL Accounting"
    response.view="generic.html"
    
    grid = SQLFORM.smartgrid(db.accounting)
    return locals()

@auth.requires_login()
def add():
    response.title="Tambahkan Entry Accounting"
    response.subtitle="Jangan salah menambahkan entry accounting."
 
    form=SQLFORM(db.accounting,submit_button="Tambahkan Entry")

    #pindahkan var dari GET
    form.vars.tenant = request.vars.tenant
    form.vars.unit = request.vars.unit
    form.vars.notes = "leaseref:" + str(request.vars.unit) + " s/d " + str(request.vars.sewaakhir)
    form.vars.jumlah_di_bayar = request.vars.harga_sewa
    form.vars.category = 1
    form.vars.vendor = 1
    form.vars.entry_by = auth.user.first_name
    
    sewaakhir = request.vars.sewaakhir
    #update field sewa akhir di tabel unit
    #query = (db.unit.id == request.vars.unit)
    #set = db(query)
    #set.update(sewa_akhir=str(request.vars.sewaakhir))
            
    if form.accepts(request,session):
        response.flash = 'form accepted'

        #update field sewa akhir di tabel unit
        query = (db.unit.id == request.vars.unit)
        set = db(query)
        set.update(sewa_akhir=sewaakhir)        
        
        redirect(URL('unit','index'))
        
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'

    return dict(form=form,sewaakhir=sewaakhir)
