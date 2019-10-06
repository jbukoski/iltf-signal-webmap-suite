import os
from django.contrib.gis.utils import LayerMapping
from . import models

aoc_mi_stmarys_mapping = {
    'aoc' : 'AOC',
    'state' : 'STATE',
    'geom' : 'MULTIPOLYGON',
}

aoc_mi_stmarys_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'aoc_mi_stmarys.shp'))

boundary_mapping = {
    'oid_field' : 'OID_',
    'name' : 'Name',
    'folderpath' : 'FolderPath',
    'symbolid' : 'SymbolID',
    'altitudemo' : 'AltitudeMo',
    'clamped' : 'Clamped',
    'extruded' : 'Extruded',
    'snippet' : 'Snippet',
    'popupinfo' : 'PopupInfo',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON25D',
}

boundary_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'boundary.shp'))

buffered_bndry_mapping = {
    'id' : 'id',
    'geom' : 'MULTIPOLYGON',
}

buffered_bndry_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'buffered_bndry.shp'))

ceded_territory_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'ceaded2_field' : 'CEADED2_',
    'ceaded2_id' : 'CEADED2_ID',
    'geom' : 'MULTIPOLYGON',
}

ceded_territory_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'ceded_territory.shp'))

chippewa_cnty_mapping = {
    'statefp' : 'STATEFP',
    'countyfp' : 'COUNTYFP',
    'countyns' : 'COUNTYNS',
    'affgeoid' : 'AFFGEOID',
    'geoid' : 'GEOID',
    'name' : 'NAME',
    'lsad' : 'LSAD',
    'aland' : 'ALAND',
    'awater' : 'AWATER',
    'geom' : 'MULTIPOLYGON',
}

chippewa_cnty_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'chippewa_cnty.shp'))

chippewa_roads_mapping = {
    'fcc' : 'FCC',
    'rdname' : 'RDNAME',
    'fraddl' : 'FRADDL',
    'toaddl' : 'TOADDL',
    'fraddr' : 'FRADDR',
    'toaddr' : 'TOADDR',
    'zipl' : 'ZIPL',
    'zipr' : 'ZIPR',
    'fmcdl' : 'FMCDL',
    'fmcdr' : 'FMCDR',
    'fedirp' : 'FEDIRP',
    'name' : 'NAME',
    'fetype' : 'FETYPE',
    'fedirs' : 'FEDIRS',
    'fedirp2' : 'FEDIRP2',
    'name2' : 'NAME2',
    'fetype2' : 'FETYPE2',
    'fedirs2' : 'FEDIRS2',
    'fedirp3' : 'FEDIRP3',
    'name3' : 'NAME3',
    'fetype3' : 'FETYPE3',
    'fedirs3' : 'FEDIRS3',
    'nfc' : 'NFC',
    'ru_l' : 'RU_L',
    'ru_r' : 'RU_R',
    'legalsyst' : 'LEGALSYST',
    'pr' : 'PR',
    'bmp' : 'BMP',
    'emp' : 'EMP',
    'bpt' : 'BPT',
    'ept' : 'EPT',
    'lrs_link' : 'LRS_LINK',
    'length' : 'LENGTH',
    'oid_1' : 'OID_1',
    'ver' : 'VER',
    'mgf_hist' : 'MGF_HIST',
    'geom' : 'MULTILINESTRING',
}

chippewa_roads_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'chippewa_roads.shp'))

chippewa_streams_mapping = {
    'oid_field' : 'OID_',
    'name' : 'Name',
    'folderpath' : 'FolderPath',
    'symbolid' : 'SymbolID',
    'altitudemo' : 'AltitudeMo',
    'clamped' : 'Clamped',
    'extruded' : 'Extruded',
    'snippet' : 'Snippet',
    'popupinfo' : 'PopupInfo',
    'shape_leng' : 'Shape_Leng',
    'geom' : 'MULTILINESTRING25D',
}

chippewa_streams_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'chippewa_streams.shp'))

chippewa_waterwells_mapping = {
    'wellid' : 'WELLID',
    'county' : 'COUNTY',
    'permit_num' : 'PERMIT_NUM',
    'township' : 'TOWNSHIP',
    'town' : 'TOWN',
    'range' : 'RANGE',
    'section' : 'SECTION',
    'owner_name' : 'OWNER_NAME',
    'well_addr' : 'WELL_ADDR',
    'well_city' : 'WELL_CITY',
    'well_zip' : 'WELL_ZIP',
    'well_depth' : 'WELL_DEPTH',
    'well_type' : 'WELL_TYPE',
    'type_other' : 'TYPE_OTHER',
    'wel_status' : 'WEL_STATUS',
    'status_oth' : 'STATUS_OTH',
    'wssn' : 'WSSN',
    'well_num' : 'WELL_NUM',
    'driller_id' : 'DRILLER_ID',
    'drill_meth' : 'DRILL_METH',
    'meth_other' : 'METH_OTHER',
    'const_date' : 'CONST_DATE',
    'case_type' : 'CASE_TYPE',
    'case_other' : 'CASE_OTHER',
    'case_dia' : 'CASE_DIA',
    'case_depth' : 'CASE_DEPTH',
    'screen_frm' : 'SCREEN_FRM',
    'screen_to' : 'SCREEN_TO',
    'swl' : 'SWL',
    'flowing' : 'FLOWING',
    'aq_type' : 'AQ_TYPE',
    'test_depth' : 'TEST_DEPTH',
    'test_hours' : 'TEST_HOURS',
    'test_rate' : 'TEST_RATE',
    'test_methd' : 'TEST_METHD',
    'test_other' : 'TEST_OTHER',
    'grout' : 'GROUT',
    'pmp_cpcity' : 'PMP_CPCITY',
    'latitude' : 'LATITUDE',
    'longitude' : 'LONGITUDE',
    'methd_coll' : 'METHD_COLL',
    'elevation' : 'ELEVATION',
    'elev_methd' : 'ELEV_METHD',
    'geom' : 'MULTIPOINT',
}

chippewa_waterwells_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'chippewa_waterwells.shp'))

coastal_wetlands_mapping = {
    'objectid' : 'OBJECTID',
    'type' : 'TYPE',
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'acres' : 'ACRES',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

coastal_wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'coastal_wetlands.shp'))

comm_forst_ceded_mapping = {
    'id' : 'ID',
    'landowner' : 'LANDOWNER',
    'legal_acre' : 'LEGAL_ACRE',
    'input_id' : 'INPUT_ID',
    'grouped' : 'GROUPED',
    'county' : 'COUNTY',
    'geom' : 'MULTIPOLYGON',
}

comm_forst_ceded_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'comm_forst_ceded.shp'))

critical_dunes_mapping = {
    'objectid' : 'OBJECTID',
    'acres' : 'ACRES',
    'dune_type' : 'DUNE_TYPE',
    'code' : 'CODE',
    'ruleid' : 'RuleID',
    'shapestare' : 'ShapeSTAre',
    'shapestlen' : 'ShapeSTLen',
    'geom' : 'MULTIPOLYGON',
}

critical_dunes_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'critical_dunes.shp'))

drainfields_mapping = {
    'objectid' : 'OBJECTID',
    'lot_id' : 'Lot_ID',
    'address' : 'address',
    'name' : 'name',
    'date_const' : 'date_const',
    'contractor' : 'contractor',
    'repaired' : 'repaired',
    'inspected' : 'inspected',
    'lyr_pass' : 'pass',
    'sq_ft' : 'sq__ft',
    'flow' : 'flow',
    'ihs_funded' : 'IHS_funded',
    'lyr_type' : 'type',
    'notes' : 'notes',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}

drainfields_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'drainfields.shp'))

e_hiawathanf_mapping = {
    'objectid' : 'OBJECTID',
    'gisacres' : 'GISACRES',
    'rev_date' : 'REV_DATE',
    'shape_area' : 'SHAPE_AREA',
    'shape_len' : 'SHAPE_LEN',
    'type_class' : 'TYPE_CLASS',
    'geom' : 'MULTIPOLYGON',
}

e_hiawathanf_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'e_hiawathanf.shp'))

eup_state_parks_mapping = {
    'objectid' : 'OBJECTID',
    'acres' : 'ACRES',
    'district' : 'DISTRICT',
    'facility' : 'FACILITY',
    'geom' : 'MULTIPOLYGON',
}

eup_state_parks_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'eup_state_parks.shp'))

golf_course_mapping = {
    'id' : 'ID',
    'geom' : 'MULTIPOLYGON',
}

golf_course_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'golf_course.shp'))

great_lakes_mapping = {
    'name' : 'NAME',
    'geom' : 'MULTIPOLYGON',
}

great_lakes_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'great_lakes.shp'))

ir_roads_mapping = {
    'rdname' : 'RDNAME',
    'cnt_rdname' : 'CNT_RDNAME',
    'irr' : 'IRR',
    'route_95' : 'ROUTE_95',
    'class_95' : 'CLASS_95',
    'constru_95' : 'CONSTRU_95',
    'surface_95' : 'SURFACE_95',
    'owner_95' : 'OWNER_95',
    'sect_95' : 'SECT_95',
    'sec_nam_95' : 'SEC_NAM_95',
    'z5_length' : 'Z5_LENGTH',
    'z3_surface' : 'Z3_SURFACE',
    'z3_conditi' : 'Z3_CONDITI',
    'z3_constru' : 'Z3_CONSTRU',
    'z3_owner' : 'Z3_OWNER',
    'z3_other' : 'Z3_OTHER',
    'on_reserva' : 'ON_RESERVA',
    'length' : 'LENGTH',
    'length_mil' : 'LENGTH_MIL',
    'need_01' : 'NEED_01',
    'type_class' : 'Type_Class',
    'pro_surfac' : 'Pro_Surfac',
    'pro_should' : 'Pro_Should',
    'pro_width' : 'Pro_Width',
    'cost' : 'Cost',
    'length2010' : 'Length2010',
    'geom' : 'MULTILINESTRING',
}

ir_roads_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'ir_roads.shp'))

lake_sprior_grid_mapping = {
    'grid_no' : 'GRID_NO',
    'lake_trout' : 'LAKE_TROUT',
    'wfmu' : 'WFMU',
    'geom' : 'MULTIPOLYGON',
}

lake_sprior_grid_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'lake_sprior_grid.shp'))

mi_cntys_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'id' : 'ID',
    'cnty_fips' : 'CNTY_FIPS',
    'st_fips' : 'ST_FIPS',
    'fipsstco' : 'FIPSSTCO',
    'name' : 'NAME',
    'name2' : 'NAME2',
    'totpop' : 'TOTPOP',
    'total_ai' : 'Total_AI',
    'geom' : 'MULTIPOLYGON',
}

mi_cntys_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'mi_cntys.shp'))

mi_lakes_mapping = {
    'id' : 'ID',
    'county' : 'COUNTY',
    'cfcc' : 'CFCC',
    'landname' : 'LANDNAME',
    'landpoly' : 'LANDPOLY',
    'inland' : 'Inland',
    'geom' : 'MULTIPOLYGON',
}

mi_lakes_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'mi_lakes.shp'))

mi_state_parks_mapping = {
    'objectid' : 'OBJECTID',
    'acres' : 'ACRES',
    'district' : 'DISTRICT',
    'facility' : 'FACILITY',
    'geom' : 'MULTIPOLYGON',
}

mi_state_parks_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'mi_state_parks.shp'))

onsitewaste_mapping = {
    'objectid' : 'OBJECTID',
    'lot_id' : 'Lot_ID',
    'address' : 'address',
    'name' : 'name',
    'tank_size' : 'tank_size',
    'last_pumpe' : 'last_pumpe',
    'pass_fail' : 'pass_fail',
    'inspection' : 'inspection',
    'notes' : 'notes',
    'ft_from_wa' : 'Ft_from_wa',
    'rstre' : 'rstre',
    'drainfield' : 'drainfield',
    'drainfi8el' : 'drainfi8el',
    'lyr_type' : 'type',
    'city' : 'City',
    'state' : 'State',
    'powts' : 'POWTS',
    'yr_cnstrtd' : 'Yr_Cnstrtd',
    'qstnre_cmp' : 'Qstnre_Cmp',
    'occupnts_c' : 'Occupnts_C',
    'occupnts_a' : 'Occupnts_A',
    'vacant_mon' : 'Vacant_Mon',
    'nmbr_bedro' : 'Nmbr_Bedro',
    'water_mete' : 'Water_Mete',
    'backup' : 'Backup',
    'system_rep' : 'System_Rep',
    'inspcted_o' : 'Inspcted_O',
    'inspcted_w' : 'Inspcted_W',
    'inspcted_f' : 'Inspcted_F',
    'service_co' : 'Service_Co',
    'srvc_cntrc' : 'Srvc_Cntrc',
    'tnk_last_p' : 'Tnk_Last_P',
    'pump_frequ' : 'Pump_frequ',
    'pump_compa' : 'Pump_Compa',
    'size_gal_g' : 'Size_Gal_g',
    'pump_gpm_t' : 'Pump_gpm_t',
    'pretreat_g' : 'Pretreat_g',
    'pump2_gpm_field' : 'Pump2_gpm_',
    'soil_trt_u' : 'Soil_Trt_U',
    'graywtr_sy' : 'GrayWtr_Sy',
    'observatio' : 'Observatio',
    'tank_mater' : 'Tank_Mater',
    'inletbaffl' : 'InletBaffl',
    'warning_la' : 'Warning_La',
    'locate_cov' : 'Locate_Cov',
    'cover_secu' : 'Cover_Secu',
    'srfc_wtr_i' : 'Srfc_Wtr_I',
    'fail_indic' : 'Fail_Indic',
    'inspect_li' : 'Inspect_li',
    'effluent_f' : 'Effluent_F',
    'run_op_tes' : 'Run_Op_Tes',
    'gall_added' : 'Gall_Added',
    'pump_out_p' : 'Pump_Out_P',
    'backflow_c' : 'Backflow_C',
    'inspect_pr' : 'Inspect_Pr',
    'inspect_ba' : 'Inspect_Ba',
    'dosing_pum' : 'Dosing_Pum',
    'integrity_field' : 'Integrity_',
    'pump_eleva' : 'Pump_Eleva',
    'pump_work' : 'Pump_Work',
    'checkvalve' : 'CheckValve',
    'high_water' : 'High_Water',
    'alarm_work' : 'Alarm_Work',
    'electrical' : 'Electrical',
    'clean_pump' : 'Clean_Pump',
    'probe_soil' : 'Probe_Soil',
    'gravity_pr' : 'Gravity_Pr',
    'previous_f' : 'Previous_F',
    'seepage' : 'Seepage',
    'lush_veget' : 'Lush_Veget',
    'ponding' : 'Ponding',
    'even_distr' : 'Even_Distr',
    'feet_to_we' : 'Feet_to_We',
    'groundwate' : 'Groundwate',
    'depth_to_s' : 'Depth_to_S',
    'pretreatme' : 'Pretreatme',
    'pretreat_1' : 'Pretreat_1',
    'pretreat_2' : 'Pretreat_2',
    'soil_treat' : 'Soil_Treat',
    'soil_area_field' : 'Soil_Area_',
    'pump_tank' : 'Pump_Tank',
    'pump_tank_field' : 'Pump_Tank_',
    'inspector' : 'Inspector',
    'inspecti_1' : 'Inspecti_1',
    'data_entry' : 'Data_Entry',
    'data_ent_1' : 'Data_Ent_1',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'geom' : 'MULTIPOINT',
}

onsitewaste_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'onsitewaste.shp'))

onsitewastewater_mapping = {
    'objectid' : 'OBJECTID',
    'lot_id' : 'lot_ID',
    'address' : 'address',
    'name' : 'Name',
    'volume' : 'Volume',
    'tank_manuf' : 'tank_manuf',
    'tank_type' : 'tank_TYPE',
    'inspected' : 'Inspected',
    'last_inspe' : 'Last_inspe',
    'pumped' : 'pumped',
    'lastpumped' : 'lastpumped',
    'flow' : 'flow',
    'lyr_filter' : 'filter',
    'last_filte' : 'Last_filte',
    'pass_failu' : 'pass_failu',
    'cover_secu' : 'cover_secu',
    'inspection' : 'inspection',
    'geom' : 'MULTIPOINT',
}

onsitewastewater_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'onsitewastewater.shp'))


parcels_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'lots3_field' : 'LOTS3_',
    'address' : 'ADDRESS',
    'acres' : 'ACRES',
    'street' : 'STREET',
    'street_typ' : 'STREET_TYP',
    'street_2' : 'STREET_2',
    'c_address' : 'C_ADDRESS',
    'label' : 'Label',
    'svc_ln_upd' : 'Svc_Ln_Upd',
    'flow_dir' : 'Flow_Dir',
    'geom' : 'MULTIPOLYGON',
}

parcels_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'parcels.shp'))

pwr_syst_backup_2014_mapping = {
    'objectid' : 'OBJECTID',
    'lot_id' : 'Lot_ID',
    'address' : 'address',
    'name' : 'name',
    'tank_size' : 'tank_size',
    'last_pumpe' : 'last_pumpe',
    'pass_fail' : 'pass_fail',
    'inspection' : 'inspection',
    'notes' : 'notes',
    'ft_from_wa' : 'Ft_from_wa',
    'rstre' : 'rstre',
    'drainfield' : 'drainfield',
    'drainfi8el' : 'drainfi8el',
    'class_type' : 'class_type',
    'city' : 'City',
    'state' : 'State',
    'powts' : 'POWTS',
    'yr_cnstrtd' : 'Yr_Cnstrtd',
    'qstnre_cmp' : 'Qstnre_Cmp',
    'occupnts_c' : 'Occupnts_C',
    'occupnts_a' : 'Occupnts_A',
    'vacant_mon' : 'Vacant_Mon',
    'nmbr_bedro' : 'Nmbr_Bedro',
    'water_mete' : 'Water_Mete',
    'backup' : 'Backup',
    'system_rep' : 'System_Rep',
    'inspcted_o' : 'Inspcted_O',
    'inspcted_w' : 'Inspcted_W',
    'inspcted_f' : 'Inspcted_F',
    'service_co' : 'Service_Co',
    'srvc_cntrc' : 'Srvc_Cntrc',
    'tnk_last_p' : 'Tnk_Last_P',
    'pump_frequ' : 'Pump_frequ',
    'pump_compa' : 'Pump_Compa',
    'size_gal_g' : 'Size_Gal_g',
    'pump_gpm_t' : 'Pump_gpm_t',
    'pretreat_g' : 'Pretreat_g',
    'pump2_gpm_field' : 'Pump2_gpm_',
    'soil_trt_u' : 'Soil_Trt_U',
    'graywtr_sy' : 'GrayWtr_Sy',
    'observatio' : 'Observatio',
    'tank_mater' : 'Tank_Mater',
    'inletbaffl' : 'InletBaffl',
    'warning_la' : 'Warning_La',
    'locate_cov' : 'Locate_Cov',
    'cover_secu' : 'Cover_Secu',
    'srfc_wtr_i' : 'Srfc_Wtr_I',
    'fail_indic' : 'Fail_Indic',
    'inspect_li' : 'Inspect_li',
    'effluent_f' : 'Effluent_F',
    'run_op_tes' : 'Run_Op_Tes',
    'gall_added' : 'Gall_Added',
    'pump_out_p' : 'Pump_Out_P',
    'backflow_c' : 'Backflow_C',
    'inspect_pr' : 'Inspect_Pr',
    'inspect_ba' : 'Inspect_Ba',
    'dosing_pum' : 'Dosing_Pum',
    'integrity_field' : 'Integrity_',
    'pump_eleva' : 'Pump_Eleva',
    'pump_work' : 'Pump_Work',
    'checkvalve' : 'CheckValve',
    'high_water' : 'High_Water',
    'alarm_work' : 'Alarm_Work',
    'electrical' : 'Electrical',
    'clean_pump' : 'Clean_Pump',
    'probe_soil' : 'Probe_Soil',
    'gravity_pr' : 'Gravity_Pr',
    'previous_f' : 'Previous_F',
    'seepage' : 'Seepage',
    'lush_veget' : 'Lush_Veget',
    'ponding' : 'Ponding',
    'even_distr' : 'Even_Distr',
    'feet_to_we' : 'Feet_to_We',
    'groundwate' : 'Groundwate',
    'depth_to_s' : 'Depth_to_S',
    'pretreatme' : 'Pretreatme',
    'pretreat_1' : 'Pretreat_1',
    'pretreat_2' : 'Pretreat_2',
    'soil_treat' : 'Soil_Treat',
    'soil_area_field' : 'Soil_Area_',
    'pump_tank' : 'Pump_Tank',
    'pump_tank_field' : 'Pump_Tank_',
    'inspector' : 'Inspector',
    'inspecti_1' : 'Inspecti_1',
    'data_entry' : 'Data_Entry',
    'data_ent_1' : 'Data_Ent_1',
    'latitude' : 'Latitude',
    'longitude' : 'Longitude',
    'geom' : 'MULTIPOINT',
}

pwr_syst_backup_2014_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'pwr_syst_backup_2014.shp'))

railroad_mapping = {
    'fcc' : 'FCC',
    'name' : 'NAME',
    'name2' : 'NAME2',
    'name3' : 'NAME3',
    'length' : 'LENGTH',
    'oid' : 'OID',
    'mgf_hist' : 'MGF_HIST',
    'geom' : 'MULTILINESTRING',
}

railroad_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'railroad.shp'))

rivers_mapping = {
    'fid' : 'fid',
    'name' : 'Name',
    'oid_1' : 'OID_1',
    'ver' : 'VER',
    'mgf_hist' : 'MGF_HIST',
    'length' : 'LENGTH',
    'fcc' : 'FCC',
    'name2' : 'NAME2',
    'name3' : 'NAME3',
    'fid2' : 'FID2',
    'geom' : 'MULTILINESTRING25D',
}

rivers_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'rivers.shp'))

septic_tanks_mapping = {
    'objectid' : 'OBJECTID',
    'lot_id' : 'lot_ID',
    'address' : 'address',
    'name' : 'Name',
    'volume' : 'Volume',
    'tank_manuf' : 'tank_manuf',
    'tank_type' : 'tank_TYPE',
    'inspected' : 'Inspected',
    'last_inspe' : 'Last_inspe',
    'pumped' : 'pumped',
    'lastpumped' : 'lastpumped',
    'flow' : 'flow',
    'lyr_filter' : 'filter',
    'last_filte' : 'Last_filte',
    'pass_failu' : 'pass_failu',
    'cover_secu' : 'cover_secu',
    'inspection' : 'inspection',
    'shape_leng' : 'SHAPE_Leng',
    'shape_area' : 'SHAPE_Area',
    'geom' : 'MULTIPOLYGON',
}

septic_tanks_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'septic_tanks.shp'))


snowmobile_trails_mapping = {
    'date' : 'DATE',
    'time' : 'TIME',
    'gps_date' : 'GPS_DATE',
    'gps_length' : 'GPS_LENGTH',
    'geom' : 'MULTILINESTRING',
}

snowmobile_trails_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'snowmobile_trails.shp'))

subwatersheds_mapping = {
    'oid_field' : 'OID_',
    'name' : 'Name',
    'folderpath' : 'FolderPath',
    'symbolid' : 'SymbolID',
    'altitudemo' : 'AltitudeMo',
    'clamped' : 'Clamped',
    'extruded' : 'Extruded',
    'snippet' : 'Snippet',
    'popupinfo' : 'PopupInfo',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON25D',
}

subwatersheds_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'subwatersheds.shp'))

trails_mapping = {
    'begin' : 'begin',
    'end' : 'end',
    'path' : 'path',
    'geom' : 'MULTILINESTRING',
}

trails_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'trails.shp'))


waishkey_add_streams_mapping = {
    'fcc' : 'FCC',
    'name' : 'NAME',
    'name2' : 'NAME2',
    'name3' : 'NAME3',
    'length' : 'LENGTH',
    'oid_1' : 'OID_1',
    'ver' : 'VER',
    'mgf_hist' : 'MGF_HIST',
    'geom' : 'MULTILINESTRING',
}

waishkey_add_streams_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'waishkey_add_streams.shp'))

waishkey_ptnl_wtlnd_rstrn_mapping = {
    'objectid_1' : 'OBJECTID_1',
    'objectid' : 'OBJECTID',
    'res_rank' : 'Res_rank',
    'acres' : 'Acres',
    'area_field' : 'AREA_',
    'shape_star' : 'Shape_STAr',
    'shape_stle' : 'Shape_STLe',
    'shapestare' : 'ShapeSTAre',
    'shapestlen' : 'ShapeSTLen',
    'geom' : 'MULTIPOLYGON',
}

waishkey_ptnl_wtlnd_rstrn_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'waishkey_ptnl_wtlnd_rstrn.shp'))

waishkey_river_mapping = {
    'oid_field' : 'OID_',
    'name' : 'Name',
    'folderpath' : 'FolderPath',
    'symbolid' : 'SymbolID',
    'altitudemo' : 'AltitudeMo',
    'clamped' : 'Clamped',
    'extruded' : 'Extruded',
    'snippet' : 'Snippet',
    'popupinfo' : 'PopupInfo',
    'shape_leng' : 'Shape_Leng',
    'geom' : 'MULTILINESTRING25D',
}

waishkey_river_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'waishkey_river.shp'))

waiska_watershed_mapping = {
    'oid_field' : 'OID_',
    'name' : 'Name',
    'folderpath' : 'FolderPath',
    'symbolid' : 'SymbolID',
    'altitudemo' : 'AltitudeMo',
    'clamped' : 'Clamped',
    'extruded' : 'Extruded',
    'snippet' : 'Snippet',
    'popupinfo' : 'PopupInfo',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON25D',
}

waiska_watershed_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'waiska_watershed.shp'))

wastewater_lines_mapping = {
    'objectid' : 'OBJECTID',
    'type' : 'type',
    'size' : 'size',
    'constructi' : 'constructi',
    'repair_dat' : 'repair_dat',
    'contractor' : 'contractor',
    'original_c' : 'original_c',
    'replacemen' : 'replacemen',
    'flow_vol' : 'flow_vol',
    'shape_leng' : 'SHAPE_Leng',
    'geom' : 'MULTILINESTRING25D',
}

wastewater_lines_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'wastewater_lines.shp'))

watermains_mapping = {
    'rdname' : 'RDNAME',
    'cnt_rdname' : 'CNT_RDNAME',
    'irr' : 'IRR',
    'route_95' : 'ROUTE_95',
    'class_95' : 'CLASS_95',
    'constru_95' : 'CONSTRU_95',
    'surface_95' : 'SURFACE_95',
    'owner_95' : 'OWNER_95',
    'sect_95' : 'SECT_95',
    'sec_nam_95' : 'SEC_NAM_95',
    'z5_length' : 'Z5_LENGTH',
    'z3_surface' : 'Z3_SURFACE',
    'z3_conditi' : 'Z3_CONDITI',
    'z3_constru' : 'Z3_CONSTRU',
    'z3_owner' : 'Z3_OWNER',
    'z3_other' : 'Z3_OTHER',
    'on_reserva' : 'ON_RESERVA',
    'length' : 'LENGTH',
    'length_mil' : 'LENGTH_MIL',
    'need_01' : 'NEED_01',
    'wtrmn_clss' : 'wtrmn_clss',
    'pro_surfac' : 'Pro_Surfac',
    'pro_should' : 'Pro_Should',
    'pro_width' : 'Pro_Width',
    'cost' : 'Cost',
    'length2010' : 'Length2010',
    'geom' : 'MULTILINESTRING',
}

watermains_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'watermains.shp'))

wellhead_protection_mapping = {
    'objectid' : 'OBJECTID',
    'michiganwe' : 'michiganWE',
    'wssn' : 'WSSN',
    'system' : 'SYSTEM',
    'type' : 'TYPE',
    'approval_d' : 'APPROVAL_D',
    'shapestare' : 'ShapeSTAre',
    'shapestlen' : 'ShapeSTLen',
    'geom' : 'MULTIPOLYGON',
}

wellhead_protection_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'wellhead_protection.shp'))

wetland_preserve_mapping = {
    'area' : 'AREA',
    'perimeter' : 'PERIMETER',
    'chippewa_field' : 'CHIPPEWA_',
    'chippewa_i' : 'CHIPPEWA_I',
    'county' : 'COUNTY',
    'range' : 'RANGE',
    'town' : 'TOWN',
    'section' : 'SECTION',
    'qtr_qtr' : 'QTR_QTR',
    'qtr' : 'QTR',
    'twnrng' : 'TWNRNG',
    'twnrngsec' : 'TWNRNGSEC',
    'geo_id' : 'GEO_ID',
    'cnty2' : 'CNTY2',
    'forty' : 'FORTY',
    'gov_lot' : 'GOV_LOT',
    'claim' : 'CLAIM',
    'x_coord' : 'X_COORD',
    'y_coord' : 'Y_COORD',
    'other' : 'OTHER',
    'acreage' : 'Acreage',
    'new_area' : 'New_area',
    'geom' : 'MULTIPOLYGON',
}

wetland_preserve_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'wetland_preserve.shp'))

whitefish_bay_reserve_mapping = {
    'id' : 'Id',
    'acreage' : 'Acreage',
    'new_area' : 'New_area',
    'geom' : 'MULTIPOLYGON',
}

whitefish_bay_reserve_shp = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'bmic', 'whitefish_bay_reserve.shp'))

def load_additional(verbose=True):

    watermains_lm = LayerMapping(
        models.watermains, watermains_shp, watermains_mapping,
        transform=False, encoding='iso-8859-1'
    )
    watermains_lm.save(strict=True, verbose=verbose)

def run(verbose=True):

    aoc_mi_stmarys_lm = LayerMapping(
        models.aoc_mi_stmarys, aoc_mi_stmarys_shp, aoc_mi_stmarys_mapping,
        transform=False, encoding='iso-8859-1'
    )
    aoc_mi_stmarys_lm.save(strict=True, verbose=verbose)

    boundary_lm = LayerMapping(
        models.boundary, boundary_shp, boundary_mapping,
        transform=False, encoding='iso-8859-1'
    )
    boundary_lm.save(strict=True, verbose=verbose)

    buffered_bndry_lm = LayerMapping(
        models.buffered_bndry, buffered_bndry_shp, buffered_bndry_mapping,
        transform=False, encoding='iso-8859-1'
    )
    buffered_bndry_lm.save(strict=True, verbose=verbose)

    ceded_territory_lm = LayerMapping(
        models.ceded_territory, ceded_territory_shp, ceded_territory_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ceded_territory_lm.save(strict=True, verbose=verbose)

    chippewa_cnty_lm = LayerMapping(
        models.chippewa_cnty, chippewa_cnty_shp, chippewa_cnty_mapping,
        transform=False, encoding='iso-8859-1'
    )
    chippewa_cnty_lm.save(strict=True, verbose=verbose)

    chippewa_roads_lm = LayerMapping(
        models.chippewa_roads, chippewa_roads_shp, chippewa_roads_mapping,
        transform=False, encoding='iso-8859-1'
    )
    chippewa_roads_lm.save(strict=True, verbose=verbose)

    chippewa_streams_lm = LayerMapping(
        models.chippewa_streams, chippewa_streams_shp, chippewa_streams_mapping,
        transform=False, encoding='iso-8859-1'
    )
    chippewa_streams_lm.save(strict=True, verbose=verbose)

    chippewa_waterwells_lm = LayerMapping(
        models.chippewa_waterwells, chippewa_waterwells_shp, chippewa_waterwells_mapping,
        transform=False, encoding='iso-8859-1'
    )
    chippewa_waterwells_lm.save(strict=True, verbose=verbose)

    coastal_wetlands_lm = LayerMapping(
        models.coastal_wetlands, coastal_wetlands_shp, coastal_wetlands_mapping,
        transform=False, encoding='iso-8859-1'
    )
    coastal_wetlands_lm.save(strict=True, verbose=verbose)

    comm_forst_ceded_lm = LayerMapping(
        models.comm_forst_ceded, comm_forst_ceded_shp, comm_forst_ceded_mapping,
        transform=False, encoding='iso-8859-1'
    )
    comm_forst_ceded_lm.save(strict=True, verbose=verbose)

    critical_dunes_lm = LayerMapping(
        models.critical_dunes, critical_dunes_shp, critical_dunes_mapping,
        transform=False, encoding='iso-8859-1'
    )
    critical_dunes_lm.save(strict=True, verbose=verbose)

    e_hiawathanf_lm = LayerMapping(
        models.e_hiawathanf, e_hiawathanf_shp, e_hiawathanf_mapping,
        transform=False, encoding='iso-8859-1'
    )
    e_hiawathanf_lm.save(strict=True, verbose=verbose)

    eup_state_parks_lm = LayerMapping(
        models.eup_state_parks, eup_state_parks_shp, eup_state_parks_mapping,
        transform=False, encoding='iso-8859-1'
    )
    eup_state_parks_lm.save(strict=True, verbose=verbose)

    golf_course_lm = LayerMapping(
        models.golf_course, golf_course_shp, golf_course_mapping,
        transform=False, encoding='iso-8859-1'
    )
    golf_course_lm.save(strict=True, verbose=verbose)

    great_lakes_lm = LayerMapping(
        models.great_lakes, great_lakes_shp, great_lakes_mapping,
        transform=False, encoding='iso-8859-1'
    )
    great_lakes_lm.save(strict=True, verbose=verbose)

    ir_roads_lm = LayerMapping(
        models.ir_roads, ir_roads_shp, ir_roads_mapping,
        transform=False, encoding='iso-8859-1'
    )
    ir_roads_lm.save(strict=True, verbose=verbose)

    lake_sprior_grid_lm = LayerMapping(
        models.lake_sprior_grid, lake_sprior_grid_shp, lake_sprior_grid_mapping,
        transform=False, encoding='iso-8859-1'
    )
    lake_sprior_grid_lm.save(strict=True, verbose=verbose)

    mi_cntys_lm = LayerMapping(
        models.mi_cntys, mi_cntys_shp, mi_cntys_mapping,
        transform=False, encoding='iso-8859-1'
    )
    mi_cntys_lm.save(strict=True, verbose=verbose)

    mi_lakes_lm = LayerMapping(
        models.mi_lakes, mi_lakes_shp, mi_lakes_mapping,
        transform=False, encoding='iso-8859-1'
    )
    mi_lakes_lm.save(strict=True, verbose=verbose)

    mi_state_parks_lm = LayerMapping(
        models.mi_state_parks, mi_state_parks_shp, mi_state_parks_mapping,
        transform=False, encoding='iso-8859-1'
    )
    mi_state_parks_lm.save(strict=True, verbose=verbose)

    parcels_lm = LayerMapping(
        models.parcels, parcels_shp, parcels_mapping,
        transform=False, encoding='iso-8859-1'
    )
    parcels_lm.save(strict=True, verbose=verbose)

    pwr_syst_backup_2014_lm = LayerMapping(
        models.pwr_syst_backup_2014, pwr_syst_backup_2014_shp, pwr_syst_backup_2014_mapping,
        transform=False, encoding='iso-8859-1'
    )
    pwr_syst_backup_2014_lm.save(strict=True, verbose=verbose)

    railroad_lm = LayerMapping(
        models.railroad, railroad_shp, railroad_mapping,
        transform=False, encoding='iso-8859-1'
    )
    railroad_lm.save(strict=True, verbose=verbose)

    rivers_lm = LayerMapping(
        models.rivers, rivers_shp, rivers_mapping,
        transform=False, encoding='iso-8859-1'
    )
    rivers_lm.save(strict=True, verbose=verbose)

    snowmobile_trails_lm = LayerMapping(
        models.snowmobile_trails, snowmobile_trails_shp, snowmobile_trails_mapping,
        transform=False, encoding='iso-8859-1'
    )
    snowmobile_trails_lm.save(strict=True, verbose=verbose)

    subwatersheds_lm = LayerMapping(
        models.subwatersheds, subwatersheds_shp, subwatersheds_mapping,
        transform=False, encoding='iso-8859-1'
    )
    subwatersheds_lm.save(strict=True, verbose=verbose)

    waishkey_add_streams_lm = LayerMapping(
        models.waishkey_add_streams, waishkey_add_streams_shp, waishkey_add_streams_mapping,
        transform=False, encoding='iso-8859-1'
    )
    waishkey_add_streams_lm.save(strict=True, verbose=verbose)

    waishkey_ptnl_wtlnd_rstrn_lm = LayerMapping(
        models.waishkey_ptnl_wtlnd_rstrn, waishkey_ptnl_wtlnd_rstrn_shp, waishkey_ptnl_wtlnd_rstrn_mapping,
        transform=False, encoding='iso-8859-1'
    )
    waishkey_ptnl_wtlnd_rstrn_lm.save(strict=True, verbose=verbose)

    waishkey_river_lm = LayerMapping(
        models.waishkey_river, waishkey_river_shp, waishkey_river_mapping,
        transform=False, encoding='iso-8859-1'
    )
    waishkey_river_lm.save(strict=True, verbose=verbose)

    waiska_watershed_lm = LayerMapping(
        models.waiska_watershed, waiska_watershed_shp, waiska_watershed_mapping,
        transform=False, encoding='iso-8859-1'
    )
    waiska_watershed_lm.save(strict=True, verbose=verbose)

    wastewater_lines_lm = LayerMapping(
        models.wastewater_lines, wastewater_lines_shp, wastewater_lines_mapping,
        transform=False, encoding='iso-8859-1'
    )
    wastewater_lines_lm.save(strict=True, verbose=verbose)

    watermains_lm = LayerMapping(
        models.watermains, watermains_shp, watermains_mapping,
        transform=False, encoding='iso-8859-1'
    )
    watermains_lm.save(strict=True, verbose=verbose)

    wellhead_protection_lm = LayerMapping(
        models.wellhead_protection, wellhead_protection_shp, wellhead_protection_mapping,
        transform=False, encoding='iso-8859-1'
    )
    wellhead_protection_lm.save(strict=True, verbose=verbose)

    wetland_preserve_lm = LayerMapping(
        models.wetland_preserve, wetland_preserve_shp, wetland_preserve_mapping,
        transform=False, encoding='iso-8859-1'
    )
    wetland_preserve_lm.save(strict=True, verbose=verbose)

    whitefish_bay_reserve_lm = LayerMapping(
        models.whitefish_bay_reserve, whitefish_bay_reserve_shp, whitefish_bay_reserve_mapping,
        transform=False, encoding='iso-8859-1'
    )
    whitefish_bay_reserve_lm.save(strict=True, verbose=verbose)
