from Airport import Airport

METAR_NZCH = 'METAR NZCH 021100Z AUTO 26005KT 9999 FEW025/// BKN065/// 07/05 Q1024 NOSIG RMK SUGARLOAF 20016KT='
METAR_NZWR = 'METAR NZWR 021100Z AUTO 35003KT 19KM NCD 10/08 Q1022='
INVALID_METAR = 'MET NZCH CLEARLY NOT A VALID METAR STRING'
ICAO_INDEX = 1


def test_validate_metar():
    assert(Airport.validate_metar(METAR_NZCH))
    assert(Airport.validate_metar(METAR_NZWR))
    assert(Airport.validate_metar(INVALID_METAR) is False)


def test_validate_icao():
    nzch = Airport('NZCH', -43.489444, 172.532222, 'Christchurch')
    metars_nzch = METAR_NZCH.split(' ')
    assert(nzch.validate_icao(metars_nzch[ICAO_INDEX]))
    nzwr = Airport('NZWR', -35.768333, 174.365, 'Whangarei')
    metars_nzwr = METAR_NZWR.split(' ')
    assert(nzwr.validate_icao(metars_nzwr[ICAO_INDEX]))
    assert(nzwr.validate_icao(metars_nzch[ICAO_INDEX]) is False)
