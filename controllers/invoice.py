# coding: utf8
# try something like
def index():
    response.title="Invoice"
    response.subtitle="Daftar seluruh tagihan"
    
    rows = db((db.invoice.id>0) & (db.tenant.id==db.invoice.tenant)).select()
    if not rows: raise HTTP(404)
    
    return dict(rows=rows)

def view():
    response.title="Lihat Invoice"
    response.subtitle="melihat detail invoice"
    
    ids = request.args[0]
    inv = db((db.invoice.id==ids) & (db.tenant.id==db.invoice.tenant)).select()
    if not inv: raise HTTP(404)
    
    detail = db(db.invoice_item.invoice==ids).select()
    
    return dict(inv=inv,detail=detail)

def add():
    response.title="Tambah Invoice"
    response.subtitle="menambah Invoice"
    
    form = SQLFORM(db.invoice)
    #form = SQLFORM.factory(db.invoice,db.invoice_item)
    #form = FORM('Nama Tenant',INPUT(name="nama_tenant")
    #my_extra_element = TR(LABEL('I agree to the terms and conditions'), INPUT(_name='agree',value=True,_type='checkbox'))
    
    my_extra = [TR(LABEL('Keterangan'),LABEL('Jumlah'))]
    for i in range(1,5):
        ket = 'keterangan' + str(i)
        jum = 'jumlah' + str(i)
        my_extra.append(TR(INPUT(_name=ket),INPUT(_name=jum,requires=IS_EMPTY_OR(IS_INT_IN_RANGE(0,1000000000,error_message="Harus angka")))))


    my_extra_element = TR(my_extra)
    
    form[0].insert(-1,my_extra_element)           

    if form.validate():
        id = db.invoice.insert(**db.invoice._filter_fields(form.vars))
        form.vars.invoice = id
        
        #masukkan data satu persatu.
        for i in range(1,5):
            ket = 'keterangan' + str(i)
            jum = 'jumlah' + str(i)
            #ambil isi form.vars
            fvk = form.vars[ket]
            fvj = form.vars[jum]
            
            if (fvk and fvj):
                id = db.invoice_item.insert(invoice=form.vars.invoice,keterangan=fvk,jumlah=fvj)
        
        response.flash="Berhasil"
        
        
    return dict(form=form)

def edit():
    response.title="Edit Invoice"
    response.subtitle="Merubah isi Invoice"
    
    ids=request.args[0]

    form=SQLFORM(db.invoice)
    
    if form.validate():
        if form.deleted:
            db(db.invoice_item.invoice==ids).delete()
            response.flash = "Data Deleted - Record:" + str(ids)

        response.flash = "Data Update - Record:" + str(ids)
        redirect(URL('invoice','index'))
    
    return dict(form=crud.update(db.invoice,ids))
