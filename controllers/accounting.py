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
    import datetime
    response.title="Tambahkan Entry Accounting"
    response.subtitle="Jangan salah menambahkan entry accounting."
 
    form=SQLFORM(db.accounting,submit_button="Tambahkan Entry")


     #pindahkan var dari GET
    form.vars.tenant = request.vars.tenant
    form.vars.unit = request.vars.unit
    form.vars.notes = "leaseref:" + str(request.vars.lease) + " s/d " + str(request.vars.sewaakhir)
    form.vars.jumlah_di_bayar = request.vars.harga_sewa
    form.vars.category = 1
    form.vars.vendor = 1
    form.vars.entry_by = auth.user.first_name
    form.vars.tgl_jatuh_tempo = request.vars.sewaakhir
    form.vars.tgl_di_bayar = datetime.datetime.now()

    if form.accepts(request,session):
        response.flash = 'form accepted'
        
        query = (db.unit.id == form.vars.unit)
        set = db(query).update(sewa_akhir=request.vars.sewaakhir)
        
        redirect(URL('tenant','view',args=request.vars.tenant))
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'Isi formulir ini jangan lupa mengganti tanggal di bayar.'

    return dict(form=form,sewaakhir=request.vars.sewaakhir)


def view():
    response.title="Accounting entry"
    response.subtitle="melihat detail akunting"

    ids = request.args[0]
    accounting = db(db.accounting.id==ids).select()
    if not accounting: raise HTTP(404)

    return dict(form=crud.update(db.accounting,ids))
