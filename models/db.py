# -*- coding: utf-8 -*-
from decimal import Decimal
def moneyfmt(value, places=0, curr='', sep='.', dp=',', pos='', neg='-', trailneg=''):
    """Convert Decimal to a money formatted string.

    places:  required number of places after the decimal point
    curr:    optional currency symbol before the sign (may be blank)
    sep:     optional grouping separator (comma, period, space, or blank)
    dp:      decimal point indicator (comma or period)
             only specify as blank when places is zero
    pos:     optional sign for positive numbers: '+', space or blank
    neg:     optional sign for negative numbers: '-', '(', space or blank
    trailneg:optional trailing minus indicator:  '-', ')', space or blank

    >>> d = Decimal('-1234567.8901')
    >>> moneyfmt(d, curr='$')
    '-$1,234,567.89'
    >>> moneyfmt(d, places=0, sep='.', dp='', neg='', trailneg='-')
    '1.234.568-'
    >>> moneyfmt(d, curr='$', neg='(', trailneg=')')
    '($1,234,567.89)'
    >>> moneyfmt(Decimal(123456789), sep=' ')
    '123 456 789.00'
    >>> moneyfmt(Decimal('-0.02'), neg='<', trailneg='>')
    '<0.02>'

    """
    q = Decimal(10) ** -places      # 2 places --> '0.01'
    sign, digits, exp = value.quantize(q).as_tuple()
    result = []
    digits = map(str, digits)
    build, next = result.append, digits.pop

    if places == 0:
        dp = ''

    if sign:
        build(trailneg)
    for i in range(places):
        build(next() if digits else '0')

    build(dp)
    if not digits:
        build('0')

    i = 0
    while digits:
        build(next())
        i += 1
        if i == 3 and digits:
            i = 0
            build(sep)
    build(curr)
    build(neg if sign else pos)
    return ''.join(reversed(result))
#########################################################################
## This scaffolding model makes your app work on Google App Engine too
## File is released under public domain and you can use without limitations
#########################################################################

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, un1comment the line below:
# request.requires_https()

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL('sqlite://storage.sqlite')
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore')
    ## store sessions and tickets there
    session.connect(request, response, db = db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db, hmac_key=Auth.get_or_create_key())
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables()

## configure email
mail=auth.settings.mailer
mail.settings.server = 'smtp.gmail.com:25'
mail.settings.sender = 'ir@gmail.com'
mail.settings.login = 'irzaip:sys'

## configure auth policy
auth.settings.registration_requires_verification = True
auth.settings.registration_requires_approval = True
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth,filename='private/janrain.key')

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################
db.define_table(
    'user',
    Field('user'),
    Field('email'),
    Field('password','password')
    )
    
db.define_table('account',
    Field('nama',length=50),
    Field('deskripsi',length=100),
    Field('tipe',length=50))

db.define_table('typepayment',
    Field('tipe',length=50))
    
db.define_table('typecat',
    Field('type',length=50))
    
db.define_table('category',
    Field('category',length=50),
    Field('typecat',requires=IS_IN_DB(db,db.typecat,'%(type)s',error_message="Harus di Isi")),
    Field('keterangan','text'))

db.define_table('frequency',
    Field('frequency',length=50))

db.define_table('priority',
    Field('priority',length=100))

db.define_table('status_pekerjaan',
    Field('status_pekerjaan',length=100))

db.define_table('vendor',
    Field('nama_usaha',length=200),
    Field('nama_kontak',length=200),
    Field('no_tel_kantor',length=100),
    Field('no_tel_kontak',length=100),
    Field('alamat',length=200),
    Field('kota',length=100),
    Field('kode_pos',length=100),
    Field('keterangan','text'),
    Field('rating','integer'))

db.define_table('todo',
    Field('tanggal','date'),
    Field('keterangan',length=200),
    Field('status_pekerjaan',requires=IS_IN_DB(db,db.status_pekerjaan,'%(status_pekerjaan)s',error_message="Harus di Isi")),
    Field('priority',requires=IS_IN_DB(db,db.priority,'%(priority)s',error_message="Harus di Isi")),
    Field('url',requires=IS_NOT_EMPTY()),
    Field('komentar','text'))

db.define_table('status',
    Field('status',length=100),
    format = "%(status)s"
    )

    
db.define_table('tenant',
    Field('nama_lengkap',length=100,label="Nama Leng"),
    Field('alamat_lengkap',length=200),
    Field('kota_asal',length=100),
    Field('kode_pos',length=100),
    Field('no_tel_selular',length=100),
    Field('no_tel_rumah',length=100),
    Field('no_tel_kantor',length=100),
    Field('email',length=100),
    Field('tmp_tgl_lahir',length=100),
    Field('no_identitas',length=100),
    Field('status',requires=IS_IN_DB(db,db.status,'%(status)s',error_message="Harus ada")),
    Field('catatan','text'))

db.define_table('receipt',
    Field('user',requires=IS_IN_DB(db,db.user,'%(user)s',error_message="Harus di isi")),
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus isi")),
    Field('tgl_bayar','date'),
    Field('keterangan','text'),
    Field('jumlah','integer'))

db.define_table('receipt_item',
    Field('receipt',requires=IS_IN_DB(db,db.receipt,None,error_message="Harus isi")),
    Field('keterangan',length=200),
    Field('jumlah','integer'))

db.define_table('building',
    Field('nama_building', length=100),
    Field('alamat',length=100),
    Field('notes','text'))

db.define_table('devidend',
    Field('building',requires=IS_IN_DB(db,db.building,'%(nama_building)s',error_message="Harus Isi")),
    Field('user',requires=IS_IN_DB(db,db.user,'%(user)s',error_message="Harus di isi")),
    Field('percentage','integer'),
    Field('keterangan','text'))

db.define_table('unit',
    Field('nama_unit',length=100),
    Field('building',requires=IS_IN_DB(db,db.building,'%(nama_building)s',error_message="Harus Isi")),
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Haris di ISI")),
    Field('available','boolean'),
    Field('booked','boolean'),
    Field('sewa_akhir','date'),
    Field('keterangan','text'),
    Field('iklan','text'))
   
    
db.define_table('inventory',
    Field('nama_inventory',length=100),
    Field('tipe',length=50),
    Field('unit',requires=IS_IN_DB(db,db.unit,'%(nama_unit)s',error_message="Harus di isi")),
    Field('estimasi_harga','integer',default=0),
    Field('keterangan','text'),
    Field('foto','upload'))
    
db.define_table('accounting',
    Field('tgl_jatuh_tempo','date',default=request.now),
    Field('tgl_di_bayar','date',default=request.now),
    Field('keterangan',length=200,default="Pembayaran"),
    Field('jumlah_hutang_piutang','integer',default=0),
    Field('jumlah_di_bayar','integer',default=0),
    #Field('account',db.account),
    Field('typepayment',requires=IS_IN_DB(db,db.typepayment,'%(tipe)s',error_message="Harus di Isi")),
    Field('category',requires=IS_IN_DB(db,db.category,'%(category)s',error_message="Harus di isi")),
    Field('vendor',requires=IS_IN_DB(db,db.vendor,'%(nama_usaha)s',error_message="Harus di isi")),
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di Isi")),
    Field('unit',requires=IS_IN_DB(db,db.unit,'%(nama_unit)s',error_message="Harus di isi")),
    Field('entry_by','text'),
    Field('notes', 'text'))

db.define_table('workorder',
    Field('tanggal','date'),
    Field('keterangan',length=200),
    Field('status_pekerjaan',requires=IS_IN_DB(db,db.status_pekerjaan,'%(status_pekerjaan)s',error_message="Harus di Isi")),
    Field('priority',requires=IS_IN_DB(db,db.priority,'%(priority)s',error_message="Harus di Isi")),
    Field('biaya','integer',default=0),
    Field('category',requires=IS_IN_DB(db,db.category,'%(category)s',error_message="Harus di isi")),
    Field('jatuh_tempo_bayar','date'),
    Field('vendor',requires=IS_IN_DB(db,db.vendor,'%(nama_usaha)s',error_message="Harus di isi")),
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di isi")),
    Field('unit',requires=IS_IN_DB(db,db.unit.id,'%(nama_unit)s',error_message="Harus di isi")),
    Field('komentar','text'))

db.define_table('lease',
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di isi")),
    Field('unit',requires=IS_IN_DB(db,db.unit,'%(nama_unit)s',error_message="Harus di isi")),
    Field('tgl_masuk','date'),
    Field('tgl_keluar','date'),
    Field('sewa_awal','date'),
    Field('sewa_akhir','date'),
    Field('frequency',requires=IS_IN_DB(db,db.frequency,'%(frequency)s',error_message="Harus di isi")),
    Field('harga_sewa','integer'),
    Field('keterangan','text'))

db.define_table('invoice',
    Field('user',db.user),
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di isi")),
    Field('tgl_mulai','date'),
    Field('tgl_selesai','date'),
    Field('keterangan',length=100))
    
db.define_table('invoice_item',
    Field('invoice',requires=IS_IN_DB(db,db.invoice,'%(id)s',error_message="Harus di isi")),
    Field('keterangan',length=100),
    Field('jumlah','integer'))

db.define_table('uploads',
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di isi")),
    Field('jenis','string'),
    Field('mainfile','upload'),
    Field('thumb','upload',writable=False,readable=False),
    )

db.define_table('tesme',
    Field('tenant',requires=IS_IN_DB(db,db.tenant,'%(nama_lengkap)s',error_message="Harus di isi"),label="Nama Tenant",comment="Mohon di isi nama lengkap"),
    Field('jenis','string'),
    )



db.user.user.requires = IS_NOT_EMPTY()
db.user.email.requires = [IS_EMAIL(), IS_NOT_IN_DB(db, 'user.email')]
db.accounting.keterangan.requires = IS_NOT_EMPTY()
db.lease.harga_sewa.requires = IS_NOT_EMPTY()
db.tenant.nama_lengkap.requires = IS_NOT_EMPTY()
db.tenant.no_identitas.requires = IS_NOT_EMPTY()
