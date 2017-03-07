import os
from django.contrib.gis.utils import LayerMapping
from .models import cotton, caddo, counties, grady, jefferson, kiowa, stephens, tillman


# Parcels mappings

caddo_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Caddo_County_UTM14_NAD83_4326.shp'))

caddo_mapping = {
    'objectid' : 'OBJECTID',
    'objectid_1' : 'OBJECTID_1',
    'parcel_id' : 'PARCEL_ID',
    'shape_leng' : 'Shape_Leng',
    'rec_num' : 'REC_NUM',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


cotton_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Cotton_County_4326.shp'))

cotton_mapping = {
    'parcelid' : 'PARCELID',
    'ag_acres' : 'ag_acres',
    'asd_acres' : 'asd_acres',
    'agparcelid' : 'AGPARCELID',
    'parcelid_1' : 'ParcelID_1',
    'owner' : 'Owner',
    'addr1' : 'Addr1',
    'addr2' : 'Addr2',
    'city' : 'City',
    'st' : 'St',
    'zip' : 'Zip',
    'school' : 'School',
    'acres' : 'Acres',
    'ownerperc' : 'OwnerPerc',
    'mktland' : 'MktLand',
    'assdland' : 'AssdLand',
    'mktimp' : 'MktImp',
    'assdimp' : 'AssdImp',
    'mktother' : 'MktOther',
    'assdother' : 'AssdOther',
    'exemption' : 'Exemption',
    'dblexempt' : 'DblExempt',
    'image' : 'Image',
    'legal' : 'Legal',
    'geom' : 'POLYGON',
}


grady_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Grady_UTM14_NAD83_4326.shp'))

grady_mapping = {
    'objectid' : 'OBJECTID',
    'label' : 'LABEL',
    'name' : 'NAME',
    'acres' : 'ACRES',
    'parcel' : 'PARCEL',
    'mpin' : 'MPIN',
    'problem' : 'PROBLEM',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


jefferson_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Jefferson_UTM14_NAD83L_4326.shp'))

jefferson_mapping = {
    'objectid' : 'OBJECTID',
    'label' : 'LABEL',
    'name' : 'NAME',
    'acres' : 'ACRES',
    'parcel' : 'PARCEL',
    'mpin' : 'MPIN',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


kiowa_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Kiowa_County_UTM14_NAD83_4326.shp'))

kiowa_mapping = {
    'objectid_1' : 'OBJECTID_1',
    'objectid' : 'OBJECTID',
    'parcelnum' : 'PARCELNUM',
    'shape_leng' : 'Shape_Leng',
    'acreage' : 'acreage',
    'parcelid' : 'ParcelID',
    'owner' : 'Owner',
    'addr1' : 'Addr1',
    'addr2' : 'Addr2',
    'city' : 'City',
    'st' : 'St',
    'zip' : 'Zip',
    'school' : 'School',
    'acres' : 'Acres',
    'ownerperc' : 'OwnerPerc',
    'mktland' : 'MktLand',
    'assdland' : 'AssdLand',
    'mktimp' : 'MktImp',
    'assdimp' : 'AssdImp',
    'mktother' : 'MktOther',
    'assdother' : 'AssdOther',
    'exemption' : 'Exemption',
    'dblexempt' : 'DblExempt',
    'image' : 'Image',
    'legal' : 'Legal',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


stephens_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Stephens_UTM14_NAD83_4326.shp'))

stephens_mapping = {
    'objectid' : 'OBJECTID',
    'label' : 'LABEL',
    'name' : 'NAME',
    'acres' : 'ACRES',
    'parcel' : 'PARCEL',
    'mpin' : 'MPIN',
    'account' : 'ACCOUNT',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


tillman_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Parcels_Tillman_County_UTM14_NAD83_4326.shp'))

tillman_mapping = {
    'objectid_1' : 'OBJECTID_1',
    'objectid' : 'OBJECTID',
    'label' : 'LABEL',
    'owner' : 'OWNER',
    'acres' : 'ACRES',
    'parcel' : 'PARCEL',
    'mpin' : 'MPIN',
    'shape_leng' : 'Shape_Leng',
    'shape_le_1' : 'Shape_Le_1',
    'shape_area' : 'Shape_Area',
    'geom' : 'POLYGON',
}


# Counties mapping

counties_mapping = {
    'objectid' : 'OBJECTID',
    'name' : 'NAME',
    'state_name' : 'STATE_NAME',
    'state_fips' : 'STATE_FIPS',
    'cnty_fips' : 'CNTY_FIPS',
    'fips' : 'FIPS',
    'population' : 'POPULATION',
    'pop_sqmi' : 'POP_SQMI',
    'pop2010' : 'POP2010',
    'pop10_sqmi' : 'POP10_SQMI',
    'white' : 'WHITE',
    'black' : 'BLACK',
    'ameri_es' : 'AMERI_ES',
    'asian' : 'ASIAN',
    'hawn_pi' : 'HAWN_PI',
    'hispanic' : 'HISPANIC',
    'other' : 'OTHER',
    'mult_race' : 'MULT_RACE',
    'males' : 'MALES',
    'females' : 'FEMALES',
    'age_under5' : 'AGE_UNDER5',
    'age_5_9' : 'AGE_5_9',
    'age_10_14' : 'AGE_10_14',
    'age_15_19' : 'AGE_15_19',
    'age_20_24' : 'AGE_20_24',
    'age_25_34' : 'AGE_25_34',
    'age_35_44' : 'AGE_35_44',
    'age_45_54' : 'AGE_45_54',
    'age_55_64' : 'AGE_55_64',
    'age_65_74' : 'AGE_65_74',
    'age_75_84' : 'AGE_75_84',
    'age_85_up' : 'AGE_85_UP',
    'med_age' : 'MED_AGE',
    'med_age_m' : 'MED_AGE_M',
    'med_age_f' : 'MED_AGE_F',
    'households' : 'HOUSEHOLDS',
    'ave_hh_sz' : 'AVE_HH_SZ',
    'hsehld_1_m' : 'HSEHLD_1_M',
    'hsehld_1_f' : 'HSEHLD_1_F',
    'marhh_chd' : 'MARHH_CHD',
    'marhh_no_c' : 'MARHH_NO_C',
    'mhh_child' : 'MHH_CHILD',
    'fhh_child' : 'FHH_CHILD',
    'families' : 'FAMILIES',
    'ave_fam_sz' : 'AVE_FAM_SZ',
    'hse_units' : 'HSE_UNITS',
    'vacant' : 'VACANT',
    'owner_occ' : 'OWNER_OCC',
    'renter_occ' : 'RENTER_OCC',
    'no_farms12' : 'NO_FARMS12',
    'ave_size12' : 'AVE_SIZE12',
    'crop_acr12' : 'CROP_ACR12',
    'ave_sale12' : 'AVE_SALE12',
    'sqmi' : 'SQMI',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

counties_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'Counties_7.shp'))

def run(verbose=True):

    caddo_lm = LayerMapping(
        caddo, caddo_shp, caddo_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    caddo_lm.save(strict=True, verbose=verbose)

    cotton_lm = LayerMapping(
        cotton, cotton_shp, cotton_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    cotton_lm.save(strict=True, verbose=verbose)
 
    grady_lm = LayerMapping(
        grady, grady_shp, grady_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    grady_lm.save(strict=True, verbose=verbose)

    jefferson_lm = LayerMapping(
        jefferson, jefferson_shp, jefferson_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    jefferson_lm.save(strict=True, verbose=verbose)

    kiowa_lm = LayerMapping(
        kiowa, kiowa_shp, kiowa_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    kiowa_lm.save(strict=True, verbose=verbose)

    stephens_lm = LayerMapping(
        stephens, stephens_shp, stephens_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    stephens_lm.save(strict=True, verbose=verbose)

    tillman_lm = LayerMapping(
        tillman, tillman_shp, tillman_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    tillman_lm.save(strict=True, verbose=verbose)

    counties_lm = LayerMapping(
        counties, counties_shp, counties_mapping,
        transform = False, encoding = 'iso-8859-1',
    )
    counties_lm.save(strict=True, verbose=verbose)
