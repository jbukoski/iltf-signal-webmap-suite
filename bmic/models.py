from django.contrib.gis.db import models

class aoc_mi_stmarys(models.Model):
    aoc = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class boundary(models.Model):
    oid_field = models.BigIntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altitudemo = models.IntegerField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class buffered_bndry(models.Model):
    id = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class ceded_territory(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    ceaded2_field = models.BigIntegerField()
    ceaded2_id = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class chippewa_cnty(models.Model):
    statefp = models.CharField(max_length=2)
    countyfp = models.CharField(max_length=3)
    countyns = models.CharField(max_length=8)
    affgeoid = models.CharField(max_length=14)
    geoid = models.CharField(max_length=5)
    name = models.CharField(max_length=100)
    lsad = models.CharField(max_length=2)
    aland = models.BigIntegerField()
    awater = models.BigIntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class chippewa_roads(models.Model):
    fcc = models.CharField(max_length=3)
    rdname = models.CharField(max_length=60)
    fraddl = models.BigIntegerField()
    toaddl = models.BigIntegerField()
    fraddr = models.BigIntegerField()
    toaddr = models.BigIntegerField()
    zipl = models.IntegerField()
    zipr = models.IntegerField()
    fmcdl = models.IntegerField()
    fmcdr = models.IntegerField()
    fedirp = models.CharField(max_length=2)
    name = models.CharField(max_length=30)
    fetype = models.CharField(max_length=4)
    fedirs = models.CharField(max_length=2)
    fedirp2 = models.CharField(max_length=2)
    name2 = models.CharField(max_length=30)
    fetype2 = models.CharField(max_length=4)
    fedirs2 = models.CharField(max_length=2)
    fedirp3 = models.CharField(max_length=2)
    name3 = models.CharField(max_length=30)
    fetype3 = models.CharField(max_length=4)
    fedirs3 = models.CharField(max_length=2)
    nfc = models.IntegerField()
    ru_l = models.IntegerField()
    ru_r = models.IntegerField()
    legalsyst = models.IntegerField()
    pr = models.IntegerField()
    bmp = models.FloatField()
    emp = models.FloatField()
    bpt = models.CharField(max_length=8)
    ept = models.CharField(max_length=8)
    lrs_link = models.CharField(max_length=23)
    length = models.FloatField()
    oid_1 = models.BigIntegerField()
    ver = models.CharField(max_length=3)
    mgf_hist = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class chippewa_streams(models.Model):
    oid_field = models.BigIntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altitudemo = models.IntegerField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class chippewa_waterwells(models.Model):
    wellid = models.CharField(max_length=12)
    county = models.CharField(max_length=30)
    permit_num = models.CharField(max_length=20)
    township = models.CharField(max_length=50)
    town = models.CharField(max_length=3)
    range = models.CharField(max_length=3)
    section = models.BigIntegerField()
    owner_name = models.CharField(max_length=30)
    well_addr = models.CharField(max_length=50)
    well_city = models.CharField(max_length=30)
    well_zip = models.CharField(max_length=9)
    well_depth = models.FloatField()
    well_type = models.CharField(max_length=6)
    type_other = models.CharField(max_length=30)
    wel_status = models.CharField(max_length=6)
    status_oth = models.CharField(max_length=254)
    wssn = models.FloatField()
    well_num = models.CharField(max_length=30)
    driller_id = models.CharField(max_length=10)
    drill_meth = models.CharField(max_length=6)
    meth_other = models.CharField(max_length=30)
    const_date = models.CharField(max_length=23)
    case_type = models.CharField(max_length=6)
    case_other = models.CharField(max_length=30)
    case_dia = models.FloatField()
    case_depth = models.FloatField()
    screen_frm = models.FloatField()
    screen_to = models.FloatField()
    swl = models.FloatField()
    flowing = models.CharField(max_length=1)
    aq_type = models.CharField(max_length=6)
    test_depth = models.FloatField()
    test_hours = models.FloatField()
    test_rate = models.FloatField()
    test_methd = models.CharField(max_length=6)
    test_other = models.CharField(max_length=30)
    grout = models.CharField(max_length=1)
    pmp_cpcity = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    methd_coll = models.CharField(max_length=6)
    elevation = models.FloatField()
    elev_methd = models.CharField(max_length=6)
    geom = models.MultiPointField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class coastal_wetlands(models.Model):
    objectid = models.BigIntegerField()
    type = models.CharField(max_length=30)
    area = models.FloatField()
    perimeter = models.FloatField()
    acres = models.FloatField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class comm_forst_ceded(models.Model):
    id = models.IntegerField()
    landowner = models.CharField(max_length=150)
    legal_acre = models.FloatField()
    input_id = models.IntegerField()
    grouped = models.CharField(max_length=75)
    county = models.CharField(max_length=50)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class critical_dunes(models.Model):
    objectid = models.BigIntegerField()
    acres = models.FloatField()
    dune_type = models.CharField(max_length=80)
    code = models.CharField(max_length=80)
    ruleid = models.BigIntegerField()
    shapestare = models.FloatField()
    shapestlen = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class e_hiawathanf(models.Model):
    objectid = models.BigIntegerField()
    gisacres = models.FloatField()
    rev_date = models.DateField(null = True)
    shape_area = models.FloatField()
    shape_len = models.FloatField()
    type_class = models.CharField(max_length=10)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class eup_state_parks(models.Model):
    objectid = models.BigIntegerField()
    acres = models.FloatField()
    district = models.CharField(max_length=80)
    facility = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class golf_course(models.Model):
    id = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class great_lakes(models.Model):
    name = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class ir_roads(models.Model):
    rdname = models.CharField(max_length=254)
    cnt_rdname = models.IntegerField()
    irr = models.CharField(max_length=25)
    route_95 = models.CharField(max_length=10)
    class_95 = models.CharField(max_length=20)
    constru_95 = models.CharField(max_length=30)
    surface_95 = models.CharField(max_length=35)
    owner_95 = models.CharField(max_length=25)
    sect_95 = models.CharField(max_length=25)
    sec_nam_95 = models.CharField(max_length=40)
    z5_length = models.FloatField()
    z3_surface = models.CharField(max_length=40)
    z3_conditi = models.CharField(max_length=40)
    z3_constru = models.CharField(max_length=40)
    z3_owner = models.CharField(max_length=40)
    z3_other = models.CharField(max_length=50)
    on_reserva = models.CharField(max_length=15)
    length = models.FloatField()
    length_mil = models.FloatField()
    need_01 = models.IntegerField()
    type_class = models.FloatField()
    pro_surfac = models.CharField(max_length=150)
    pro_should = models.FloatField()
    pro_width = models.IntegerField()
    cost = models.IntegerField()
    length2010 = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class lake_sprior_grid(models.Model):
    grid_no = models.BigIntegerField()
    lake_trout = models.CharField(max_length=16)
    wfmu = models.CharField(max_length=25)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class mi_cntys(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    id = models.BigIntegerField()
    cnty_fips = models.BigIntegerField()
    st_fips = models.BigIntegerField()
    fipsstco = models.BigIntegerField()
    name = models.CharField(max_length=29)
    name2 = models.CharField(max_length=29)
    totpop = models.IntegerField()
    total_ai = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class mi_lakes(models.Model):
    id = models.IntegerField()
    county = models.CharField(max_length=5)
    cfcc = models.CharField(max_length=3)
    landname = models.CharField(max_length=30)
    landpoly = models.BigIntegerField()
    inland = models.CharField(max_length=20)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class mi_state_parks(models.Model):
    objectid = models.BigIntegerField()
    acres = models.FloatField()
    district = models.CharField(max_length=80)
    facility = models.CharField(max_length=80)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class parcels(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    lots3_field = models.BigIntegerField()
    address = models.CharField(max_length=250)
    acres = models.FloatField()
    street = models.CharField(max_length=50)
    street_typ = models.CharField(max_length=16)
    street_2 = models.CharField(max_length=50)
    c_address = models.CharField(max_length=60)
    label = models.CharField(max_length=13)
    svc_ln_upd = models.CharField(max_length=50)
    flow_dir = models.CharField(max_length=8)
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class pwr_syst_backup_2014(models.Model):
    objectid = models.IntegerField()
    lot_id = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    tank_size = models.IntegerField()
    last_pumpe = models.DateField(null = True)
    pass_fail = models.FloatField()
    inspection = models.DateField(null = True)
    notes = models.CharField(max_length=254)
    ft_from_wa = models.IntegerField()
    rstre = models.IntegerField()
    drainfield = models.IntegerField()
    drainfi8el = models.CharField(max_length=50)
    class_type = models.CharField(max_length=254)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    powts = models.IntegerField()
    yr_cnstrtd = models.IntegerField()
    qstnre_cmp = models.CharField(max_length=15)
    occupnts_c = models.IntegerField()
    occupnts_a = models.IntegerField()
    vacant_mon = models.IntegerField()
    nmbr_bedro = models.IntegerField()
    water_mete = models.CharField(max_length=15)
    backup = models.CharField(max_length=15)
    system_rep = models.CharField(max_length=50)
    inspcted_o = models.CharField(max_length=15)
    inspcted_w = models.CharField(max_length=30)
    inspcted_f = models.CharField(max_length=10)
    service_co = models.CharField(max_length=15)
    srvc_cntrc = models.CharField(max_length=35)
    tnk_last_p = models.DateField(null = True)
    pump_frequ = models.CharField(max_length=15)
    pump_compa = models.CharField(max_length=35)
    size_gal_g = models.IntegerField()
    pump_gpm_t = models.IntegerField()
    pretreat_g = models.IntegerField()
    pump2_gpm_field = models.IntegerField()
    soil_trt_u = models.CharField(max_length=15)
    graywtr_sy = models.CharField(max_length=35)
    observatio = models.CharField(max_length=35)
    tank_mater = models.CharField(max_length=20)
    inletbaffl = models.CharField(max_length=15)
    warning_la = models.CharField(max_length=15)
    locate_cov = models.CharField(max_length=10)
    cover_secu = models.CharField(max_length=10)
    srfc_wtr_i = models.CharField(max_length=10)
    fail_indic = models.CharField(max_length=10)
    inspect_li = models.CharField(max_length=10)
    effluent_f = models.CharField(max_length=10)
    run_op_tes = models.CharField(max_length=10)
    gall_added = models.IntegerField()
    pump_out_p = models.CharField(max_length=10)
    backflow_c = models.CharField(max_length=50)
    inspect_pr = models.CharField(max_length=10)
    inspect_ba = models.CharField(max_length=10)
    dosing_pum = models.CharField(max_length=10)
    integrity_field = models.CharField(max_length=10)
    pump_eleva = models.CharField(max_length=10)
    pump_work = models.CharField(max_length=10)
    checkvalve = models.CharField(max_length=10)
    high_water = models.CharField(max_length=10)
    alarm_work = models.CharField(max_length=10)
    electrical = models.CharField(max_length=10)
    clean_pump = models.CharField(max_length=10)
    probe_soil = models.CharField(max_length=10)
    gravity_pr = models.CharField(max_length=15)
    previous_f = models.CharField(max_length=10)
    seepage = models.CharField(max_length=10)
    lush_veget = models.CharField(max_length=10)
    ponding = models.CharField(max_length=10)
    even_distr = models.CharField(max_length=10)
    feet_to_we = models.IntegerField()
    groundwate = models.CharField(max_length=10)
    depth_to_s = models.IntegerField()
    pretreatme = models.CharField(max_length=25)
    pretreat_1 = models.CharField(max_length=25)
    pretreat_2 = models.CharField(max_length=35)
    soil_treat = models.CharField(max_length=25)
    soil_area_field = models.CharField(max_length=35)
    pump_tank = models.CharField(max_length=25)
    pump_tank_field = models.CharField(max_length=35)
    inspector = models.CharField(max_length=35)
    inspecti_1 = models.DateField(null = True)
    data_entry = models.CharField(max_length=35)
    data_ent_1 = models.DateField()
    latitude = models.CharField(max_length=25)
    longitude = models.CharField(max_length=25)
    geom = models.MultiPointField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class railroad(models.Model):
    fcc = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    length = models.FloatField()
    oid = models.BigIntegerField()
    mgf_hist = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class rivers(models.Model):
    fid = models.CharField(max_length=80)
    name = models.CharField(max_length=80)
    oid_1 = models.CharField(max_length=80)
    ver = models.CharField(max_length=80)
    mgf_hist = models.CharField(max_length=80)
    length = models.CharField(max_length=80)
    fcc = models.CharField(max_length=80)
    name2 = models.CharField(max_length=80)
    name3 = models.CharField(max_length=80)
    fid2 = models.CharField(max_length=80)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class snowmobile_trails(models.Model):
    date = models.DateField(null = True)
    time = models.CharField(max_length=10)
    gps_date = models.DateField(null = True)
    gps_length = models.FloatField(null = True)
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class subwatersheds(models.Model):
    oid_field = models.BigIntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altitudemo = models.IntegerField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class waishkey_add_streams(models.Model):
    fcc = models.CharField(max_length=3)
    name = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    name3 = models.CharField(max_length=30)
    length = models.FloatField()
    oid_1 = models.FloatField()
    ver = models.CharField(max_length=3)
    mgf_hist = models.IntegerField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class waishkey_ptnl_wtlnd_rstrn(models.Model):
    objectid_1 = models.BigIntegerField()
    objectid = models.BigIntegerField()
    res_rank = models.BigIntegerField()
    acres = models.FloatField()
    area_field = models.BigIntegerField()
    shape_star = models.FloatField()
    shape_stle = models.FloatField()
    shapestare = models.FloatField()
    shapestlen = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class waishkey_river(models.Model):
    oid_field = models.BigIntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altitudemo = models.IntegerField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class waiska_watershed(models.Model):
    oid_field = models.BigIntegerField()
    name = models.CharField(max_length=254)
    folderpath = models.CharField(max_length=254)
    symbolid = models.BigIntegerField()
    altitudemo = models.IntegerField()
    clamped = models.IntegerField()
    extruded = models.IntegerField()
    snippet = models.CharField(max_length=254)
    popupinfo = models.CharField(max_length=254)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class wastewater_lines(models.Model):
    objectid = models.FloatField()
    type = models.CharField(max_length=50)
    size = models.BigIntegerField()
    constructi = models.CharField(max_length=24)
    repair_dat = models.CharField(max_length=24)
    contractor = models.CharField(max_length=50)
    original_c = models.BigIntegerField()
    replacemen = models.BigIntegerField()
    flow_vol = models.BigIntegerField()
    shape_leng = models.FloatField()
    geom = models.MultiLineStringField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class wellhead_protection(models.Model):
    objectid = models.BigIntegerField()
    michiganwe = models.CharField(max_length=80)
    wssn = models.CharField(max_length=80)
    system = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
    approval_d = models.CharField(max_length=80)
    shapestare = models.FloatField()
    shapestlen = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class wetland_preserve(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    chippewa_field = models.BigIntegerField()
    chippewa_i = models.BigIntegerField()
    county = models.CharField(max_length=2)
    range = models.CharField(max_length=3)
    town = models.CharField(max_length=3)
    section = models.CharField(max_length=2)
    qtr_qtr = models.CharField(max_length=2)
    qtr = models.CharField(max_length=2)
    twnrng = models.CharField(max_length=6)
    twnrngsec = models.CharField(max_length=8)
    geo_id = models.CharField(max_length=12)
    cnty2 = models.CharField(max_length=2)
    forty = models.IntegerField()
    gov_lot = models.BigIntegerField()
    claim = models.CharField(max_length=4)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    other = models.CharField(max_length=40)
    acreage = models.FloatField()
    new_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)


class whitefish_bay_reserve(models.Model):
    id = models.IntegerField()
    acreage = models.FloatField()
    new_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    id = models.AutoField(primary_key = True)

    def __str__(self):
        return '%s' % (self.id)



#####################
## For file upload ##
#####################

class Document(models.Model):
    name = models.CharField(max_length=40)
    docfile = models.FileField(upload_to='bmic/uploaded')
