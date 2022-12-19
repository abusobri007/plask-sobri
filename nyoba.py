def hijriToSolar(hd, hm, hy):
    '''
    Converts a given Hijri date to Solar date.
    '''
 
 
    nhd1 = (hy - 1) * 354.3671 + (hm - 1) * 29.5306 + hd
    nhd = int(nhd1)
    nsd = nhd1 + 227016
    if nhd > 350721:
        gc = 10
    else:
        gc = 0
    if nhd > 393898:
        gc = 11
    if nhd > 430422:
        gc = 12
    if nhd > 466946:
        gc = 13
    sy = int( (nsd + gc)/365.25) + 1
    mn = round((nsd+gc)-(sy-1)*365.25)
    mn1 = 0
    sm = 1
    if mn > 31:
        mn1 = 31
        sm = 2
    if int(sy/4) == (sy/4):
        (mn1, sm) = leapYear(mn, mn1, sm)
    else:
        (mn1, sm) = ordinaryYear(mn, mn1, sm)
    if sy == 1700 or sy == 1800:
        (mn1, sm) = ordinaryYear(mn, mn1, sm)
    if sy == 1900:
        (mn1, sm) = ordinaryYear(mn, mn1, sm)

    smStr = solarMonthName(sm)

    sd = int(mn - mn1)
    return (sd, sm, sy)