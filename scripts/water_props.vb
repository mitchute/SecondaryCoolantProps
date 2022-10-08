
Function WRHO(TW)
'***********************************************************************
'  Density eq. for water at 1 atm., from CRC Handbook of Chem. & Phys.,
'   61st Edition (1980-1981), p. F-6.  Density (kg/m3) given temp. (C).
'***********************************************************************
        Dim AR0 As Double, AR1 As Double, AR2 As Double, AR6 As Double
        Dim AR3 As Double, AR4 As Double, AR5 As Double

        AR0 = 999.83952
        AR1 = 16.945176
        AR2 = -0.0079870401
        AR6 = 0.01687985
        AR3 = -4.6170461E-05
        AR4 = 1.0556302E-07
        AR5 = -2.8054253E-10

        WRHO = (AR0 + TW * AR1 + (TW ^ 2) * AR2 + (TW ^ 3) * AR3 + (TW ^ 4) * AR4 + (TW ^ 5) * AR5) / (1 + AR6 * TW)

        'Return
        End Function

Function WMU(TW)
'***********************************************************************
'  Viscosity equations for water at 1 atm., from CRC Handbook (op.cit.),
'   page F-51.  WMU in kg/meter-sec; for centipoise, multiply by 1000.
'    For temps > 100 C, fit to data from Karlekar & Desmond (saturated).
'***********************************************************************
        Dim AM0 As Single, AM1 As Single, AM2 As Single, AM3 As Single, AM4 As Single
        Dim AM5 As Single, AM6 As Single, AM7 As Single, AM8 As Single, A10 As Single
        Dim A11 As Single, A12 As Single, A13 As Single
        AM0 = -3.30233
        AM1 = 1301
        AM2 = 998.333
        AM3 = 8.1855
        AM4 = 0.00585
        AM5 = 1.002
        AM6 = -1.3272
        AM7 = -0.001053
        AM8 = 105
        A10 = 0.68714
        A11 = -0.0059231
        A12 = 2.1249E-05
        A13 = -2.69575E-08

        WMU = AM5 * 10 ^ ((TW - 20) * (AM6 + (TW - 20) * AM7) / (TW + AM8))
        If (TW < 20) Then
           WMU = 10 ^ (AM0 + AM1 / (AM2 + (TW - 20) * (AM3 + AM4 * (TW - 20)))) * 100
        End If
        If (TW > 100) Then WMU = A10 + TW * A11 + (TW ^ 2) * A12 + (TW ^ 3) * A13
        WMU = 0.001 * WMU

        'Return
        End Function
'***********************************************************************

Function WK(TW)
'***********************************************************************
'  Thermal conductivity equation from linear least-squares fit to data
'   in CRC Handbook (op.cit.), page E-11; temps. from 270 K to 620 K.
'    Temperature in Celsius, WK in [W/(m K)].  Values at one atmosphere
'    for T from 0 to 100 C, at saturation for T above 100.
'***********************************************************************
        Dim AK0 As Single, AK1 As Double, AK2 As Double, AK3 As Double, AK4 As Double

        AK0 = 0.560101
        AK1 = 0.00211703
        AK2 = -1.05172E-05
        AK3 = 1.497323E-08
        AK4 = -1.48553E-11

        WK = (AK0 + TW * AK1 + (TW ^ 2) * AK2 + (TW ^ 3) * AK3 + (TW ^ 4) * AK4)

        'Return
        End Function
'***********************************************************************

Function WCP(TW)
'***********************************************************************
'  Specific heat of water at 1 atmosphere, 0 to 100 C.  Equation from
'    linear least-squares regression of data from CRC Handbook (op.cit.)
'    page D-174; in  J/kg-C.
'    For temps > 100, fit to data from Karlekar & Desmond (saturated).
'***********************************************************************
        Dim ACP0 As Single, ACP1 As Double, ACP2 As Double, ACP3 As Single, ACP4 As Double
        Dim ACP5 As Single, ACP6 As Single, ACP7 As Single, ACP8 As Double

        ACP0 = 4.21534
        ACP1 = -0.00287819
        ACP2 = 7.4729E-05
        ACP3 = -7.79624E-07
        ACP4 = 3.220424E-09
        ACP5 = 2.9735
        ACP6 = 0.023049
        ACP7 = -0.00013953
        ACP8 = 3.092474E-07

        WCP = (ACP0 + TW * ACP1 + (TW ^ 2) * ACP2 + (TW ^ 3) * ACP3 + (TW ^ 4) * ACP4) * 1000
        If (TW > 100) Then WCP = (ACP5 + TW * ACP6 + (TW ^ 2) * ACP7 + (TW ^ 3) * ACP8) * 1000

        'Return
        End Function

Function WBETA(TW)
'Gives the volumetric thermal expansion coefficient in units (1/K), given the
'water temperature in degrees C
'
'NOTE: This has low accuracy below about 10 degrees C, so additional data for water
'are needed in equation fit.
Dim TWK As Double
TWK = TW + 273.15
WBETA = 1.06069E-09 * TWK ^ 3 - 1.05063E-06 * TWK ^ 2 + 0.00035339 * TWK - 0.0398214

End Function

Function WTDIFF(TW)
'Gives the thermal diffusivity, k/(density*spec heat) in m2/s
Dim k As Double, Rho As Double, cp As Double
k = WK(TW) * 1000 'W/mK
Rho = WRHO(TW) 'kg/m3
cp = WCP(TW) * 1000 ' J/kgK
WTDIFF = k / (Rho * cp)

End Function

Function WPR(TW)
'Gives Prandtl number as function of water temperature
WPR = (WMU(TW) / WRHO(TW)) / WTDIFF(TW)
End Function
