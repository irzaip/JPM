# coding: utf8
# try something like
import datetime

now=datetime.datetime.now()

def index():
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
    

            
    if form.accepts(request,session):
        response.flash = "OK"
        

        
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill the form'

    return dict(form=form)

def test():
    response.flash = "Testing"
    query = (db.lease.tenant==2)
    set = db(query)
    row = set.select()
    
    return dict(row=row)

    
    
    
    
def update_todo():
    db.todo.insert(tanggal="2008-10-10",keterangan="Tanggal",status_pekerjaan="1",priority="1",url="/jpm/")
    return "OK"

def drop():
    db.todo.drop()
    return "OK"
