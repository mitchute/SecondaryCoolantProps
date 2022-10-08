' Attribute VB_Name = "AntifreezeProperties"
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'' * Copyright Oklahoma State Universtiy
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''
''   LIBRARY:        Secondary coolant property utilities
''
''   LANGUAGE:         VB6
''
''   DEVELOPER:      Muhammad Haider Khan
''                   Oklahoma State University
''
''   REVISION DATE:
''
''   REFERENCE:      (1) Khan, M.H., and Spitler, J.D.,
''                       Thermophysical Properties of Antifreeze Mixtures
''
''   USAGE:          The library contains the following functions -
''
''   SECCVISC(CONCENT,TEMP,ISECC)     Calculate the dynamic viscosity   (N/m**2.s)
''   SECCCOND(CONCENT,TEMP,ISECC)     Calculate the Thermal conductivity (W/m.K)
''   SECCDENS(CONCENT,TEMP,ISECC)     Calculate the density (kg/m**3)
''   SECCSPHT(CONCENT,TEMP,ISECC)     Calculate the specific heat (J/kg.K)
''
''                   All functions use an integer (ISECC) as their last
''                   argument to select the fluid type. The fluids are:
''                     ISECC   FLUID
''                       1     Propylene Glycol solution
''                       2     Ethylene Glycol solution
''                       3     Methyl Alcohol solution
''                       4     Ethyl Alcohol solution
'C=======================================================================
''
''
'      BLOCK DATA SCNDCOOL
''
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'' *
'' * PURPOSE:  Contains data shared between functions in the library
'' *
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'' * INPUTS
'' * ======
'' * N/A
'' *
'' * OUTPUT
'' * ======
'' * N/A
'' *
'' * VARIABLES
'' * =========
'' * NSECC       Parameter for number of secondary coolants.
'' *
'' *
'' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
''
Option Base 1
''*^ Number of fluids
    'Const NSECC = 4
''*^ Arrays for viscosity coefficient data
        Dim b, c, d, e
''*^ Arrays for conductivity coefficient data
      Dim B0
''*^ Arrays for density coefficient data
      Dim BD
''*^ Arrays for specific heat coefficient data
      Dim D0, d1, D2, D3

    Function SECCVISC(CONCENT As Double, temp As Double, ISECC As Integer)
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'' *
'' * PURPOSE:  Calculate the dynamic viscosity of secondary coolants
'' *
''*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'' * INPUTS
'' * ======
'' * CONCENT  : Wt concentration of Organic Compound                (%)
'' * TEMP     : Fluid temperature                                     (')
'' * ISECC    : selected secondary coolant                            (-)
'' *
'' * OUTPUT
'' * ======
'' * SECCVISC: Dynamic viscosity                        (N/m^2.s or Pa.s)
'' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

''*^* Arguments
'      Dim CONCENT As Double, TEMP As Double, CONCENTRATION As Double
   '   Dim ISECC As Integer
''   Concentration of water
      Dim CONCofWATER As Double

''*^ Viscosity coefficient data
         b = Array(24311949006#, 2.217684747, 0.357050556, 0.248253314)
         c = Array(24311949006#, 0.006652075, 2.783367272, 1.033876987)
         d = Array(1.4E-09, 1.53602E-05, 0.041380367, 0.00097712)
         e = Array(0, 2.180722899, 1.008552041, 1.937396423)
''*^* Clamp the concentration within 0-100 bounds
    If (CONCENT > 100) Then
        CONCENT = 100
    ElseIf (CONCENT < 0) Then
        CONCENT = 0
    End If

    If (CONCENT = 0 Or ISECC = 0) Then
        SECCVISC = muWater(temp) * 0.001
        Exit Function
    End If

''   mass fraction of Organic Compound
      CONCENTRATION = CONCENT / 100
''   mass fraction of Water
    CONCofWATER = Abs(1 - CONCENTRATION)


''   if Propylene glycol mixture Thermal Conductivity is being calculated ISECC is set to 1

''   The first two fluid type calculations were changed by xiaowei xu 10/20/05
      If (ISECC = 1) Then
    CONCENTRATION = (0.0009035 * CONCENT ^ 2 + 0.9527607 * CONCENT - 0.0009811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
          SECCVISC = Exp(CONCofWATER * Log(muWater(temp)) _
            + CONCENTRATION * Log(MuPrGl(temp)) + _
              d(ISECC) * (125 - temp) ^ e(ISECC) * CONCofWATER * CONCENTRATION _
            + Log(1 + ((CONCENTRATION * CONCofWATER) / _
            (b(ISECC) * CONCofWATER ^ 2 + c(ISECC) * CONCENTRATION ^ 2))))
      ElseIf (ISECC = 2) Then
'   if Ethylene glycol mixture Thermal Conductivity is being calculated ISECC is set to 2
    CONCENTRATION = (0.00137599 * CONCENT ^ 2 + 0.8828875 * CONCENT - 0.02004811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)

          SECCVISC = Exp(CONCofWATER * Log(muWater(temp)) _
            + CONCENTRATION * Log(MuEtGl(temp)) + _
              d(ISECC) * (125 - temp) ^ e(ISECC) * CONCofWATER * CONCENTRATION _
            + Log(1 + ((CONCENTRATION * CONCofWATER) / _
            (b(ISECC) * CONCofWATER ^ 2 + c(ISECC) * CONCENTRATION ^ 2))))
''   The first two fluid type calculations were changed by xiaowei xu 10/20/05

      ElseIf (ISECC = 3) Then
'   if methyl alcohol mixture Thermal Conductivity is being calculated ISECC is set to 3
          SECCVISC = Exp(CONCofWATER * Log(muWater(temp)) _
           + CONCENTRATION * Log(MuMeoH(temp)) + _
           d(ISECC) * (70 - temp) ^ e(ISECC) * CONCofWATER * CONCENTRATION _
           + Log(1 + ((CONCENTRATION * CONCofWATER) / _
           (b(ISECC) * CONCofWATER ^ 2 + c(ISECC) * CONCENTRATION ^ 2))))
      ElseIf (ISECC = 4) Then
'   if ethyl alcohol mixture Thermal Conductivity is being calculated ISECC is set to 4
          SECCVISC = Exp(CONCofWATER * Log(muWater(temp)) _
           + CONCENTRATION * Log(MuEtoH(temp)) + _
           d(ISECC) * (70 - temp) ^ e(ISECC) * CONCofWATER * CONCENTRATION _
           + Log(1 + ((CONCENTRATION * CONCofWATER) / _
           (b(ISECC) * CONCofWATER ^ 2 + c(ISECC) * CONCENTRATION ^ 2))))
      End If
'   CONVERT mPa.S to Pa.S
    SECCVISC = SECCVISC * 0.001
    End Function
'
'
      Function SECCCOND(CONCENT As Double, temp As Double, ISECC As Integer)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of secondary coolants
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * CONCENT  : Wt concentration of Organic Compound                (%)
' * TEMP     : Fluid temperature                                     (')
' * ISECC    : selected secondary coolant                            (-)
' *
' * OUTPUT
' * ======
' * SECCCOND: Thermal conductivity                               (W/m.K)
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'

'*^ Arguments
     ' Dim CONCENT As Double, TEMP As Double, CONCENTRATION As Double
    'Dim ISECC As Integer
'   Concentration of water
    Dim CONCofWATER As Double
''*^ Conductivity coefficient data
         B0 = Array(0.114010508, -0.497355166, 0.193428424, 0.269953496)
'C1*^ Clamp the concentration within 0-100 bounds
      If (CONCENT > 100) Then
        CONCENT = 100
    ElseIf (CONCENT < 0) Then
        CONCENT = 0
    End If
    If (CONCENT = 0 Or ISECC = 0) Then
        SECCCOND = TCWater(temp)
        Exit Function
    End If

'   mass fraction of Organic Compound
      CONCENTRATION = CONCENT / 100
'   mass fraction of Water
    CONCofWATER = Abs(1 - CONCENTRATION)

'C1*^ Calculate thermal conductivity in W/m.K.
      If (ISECC = 1) Then
'   if Propylene glycol mixture Thermal Conductivity is being calculated ISECC is set to 1
    CONCENTRATION = (0.0009035 * CONCENT ^ 2 + 0.9527607 * CONCENT - 0.0009811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
          SECCCOND = (CONCofWATER * TCWater(temp) ^ B0(ISECC) _
                   + CONCENTRATION * TCPrGl(temp) ^ B0(ISECC)) _
                   ^ (1 / B0(ISECC))
      ElseIf (ISECC = 2) Then
'   if Ethylene glycol mixture Thermal Conductivity is being calculated ISECC is set to 2
    CONCENTRATION = (0.00137599 * CONCENT ^ 2 + 0.8828875 * CONCENT - 0.02004811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
          SECCCOND = (CONCofWATER * TCWater(temp) ^ B0(ISECC) _
                   + CONCENTRATION * TCEtGl(temp) ^ B0(ISECC)) _
                   ^ (1 / B0(ISECC))
      ElseIf (ISECC = 3) Then
'   if methyl alcohol mixture Thermal Conductivity is being calculated ISECC is set to 3
          SECCCOND = (CONCofWATER * TCWater(temp) ^ B0(ISECC) _
                   + CONCENTRATION * TCMeoH(temp) ^ B0(ISECC)) _
                   ^ (1 / B0(ISECC))
      ElseIf (ISECC = 4) Then
'   if ethyl alcohol mixture Thermal Conductivity is being calculated ISECC is set to 4
          SECCCOND = (CONCofWATER * TCWater(temp) ^ B0(ISECC) _
                   + CONCENTRATION * TCEtoH(temp) ^ B0(ISECC)) _
                   ^ (1 / B0(ISECC))
      End If

      End Function
'
'-----------------------------------------------------------------------
'
      Function SECCDENS(CONCENT As Double, temp As Double, ISECC As Integer)
'
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the density of secondary coolants
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * CONCENT  : Wt concentration of Organic Compound                (%)
' * TEMP     : Fluid temperature                                     (')
' * ISECC    : selected secondary coolant                            (-)
' *
' * OUTPUT
' * ======
' * SECCDENS: Density                                           (kg/m**3)
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
'*^ Arguments
'      Dim CONCENT As Double, TEMP As Double, CONCENTRATION As Double
'    Dim ISECC As Integer
''   Concentration of water
    Dim CONCofWATER As Double
''*^ Density coefficient data
         BD = Array(0.100712784, 0.084211734, 0.107165766, 0.090924937)
'C1*^ Clamp the concentration within 0-100 bounds
    If (CONCENT > 100) Then
        CONCENT = 100
    ElseIf (CONCENT < 0) Then
        CONCENT = 0
    End If

    If (CONCENT = 0 Or ISECC = 0) Then
        SECCDENS = densWater(temp) * 1000
        Exit Function
    End If

'   mass fraction of Organic Compound
      CONCENTRATION = CONCENT / 100
'   mass fraction of Water
    CONCofWATER = Abs(1 - CONCENTRATION)
      If (ISECC = 1) Then
'   if Propylene glycol mixture Density is being calculated ISECC is set to 1
    CONCENTRATION = (0.0009035 * CONCENT ^ 2 + 0.9527607 * CONCENT - 0.0009811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
        SECCDENS = CONCofWATER * densWater(temp) + _
               CONCENTRATION * densPrGl(temp) _
               + BD(ISECC) * CONCofWATER * CONCENTRATION
      ElseIf (ISECC = 2) Then
'   if Ethylene glycol mixture Density is being calculated ISECC is set to 2
    CONCENTRATION = (0.00137599 * CONCENT ^ 2 + 0.8828875 * CONCENT - 0.02004811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
        SECCDENS = CONCofWATER * densWater(temp) + _
               CONCENTRATION * densEtGl(temp) _
               + BD(ISECC) * CONCofWATER * CONCENTRATION
      ElseIf (ISECC = 3) Then
'   if Methyl alcohol mixture Density is being calculated ISECC is set to 3
        SECCDENS = CONCofWATER * densWater(temp) + _
               CONCENTRATION * densMeoH(temp) _
               + BD(ISECC) * CONCofWATER * CONCENTRATION
      ElseIf (ISECC = 4) Then
'   if Ethyl alcohol mixture Density is being calculated ISECC is set to 4
        SECCDENS = CONCofWATER * densWater(temp) + _
               CONCENTRATION * densEtoH(temp) _
               + BD(ISECC) * CONCofWATER * CONCENTRATION
      End If
'   Change from g/cm**3 to kg/m**3
      SECCDENS = SECCDENS * 1000
  End Function

'
'-----------------------------------------------------------------------
'
      Function SECCSPHT(CONCENT As Double, temp As Double, ISECC As Integer)
'
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of secondary coolants
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * CONCENT  : Wt concentration of Organic Compound                (%)
' * TEMP     : Fluid temperature                                     (')
' * ISECC    : selected secondary coolant                            (-)
' *
' * OUTPUT
' * ======
' * SECCSPHT: specific heat                                     (J/kg.K)
' *
' * FUNCTION CALLS
' * ======
' *       cpMeoH
' *       cpEtoH
' *       cpPrGl
' *       cpEtGl
' *       cpWater
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'

'*^ Arguments
'      Dim CONCENT As Double, TEMP As Double, CONCENTRATION As Double
'    Dim ISECC As Integer
'   Concentration of water
    Dim CONCofWATER As Double
''*^ Specific heat coefficient data
         D0 = Array(0.512566798, 0.25408174, 0.867040451, 1.072637702)
         d1 = Array(-0.003097081, -0.005879748, -0.063, -0.037433876)
         D2 = Array(249.088, 138.448, 56.78139184, 74.396)
         D3 = Array(-0.000414405, -0.000824252, 0.003086734, 0.002727949)
'C1*^ Clamp the concentration within 0-100 bounds
      If (CONCENT > 100) Then
        CONCENT = 100
    ElseIf (CONCENT < 0) Then
        CONCENT = 0
    End If

    If (CONCENT = 0 Or ISECC = 0) Then
        SECCSPHT = cpWater(temp) * 1000
        Exit Function
    End If

'   mass fraction of Organic Compound
      CONCENTRATION = CONCENT / 100
'   mass fraction of Water
    CONCofWATER = Abs(1 - CONCENTRATION)

      If (ISECC = 1) Then
'   if Propylene glycol mixture Specific Heat is being calculated ISECC is set to 1
    CONCENTRATION = (0.0009035 * CONCENT ^ 2 + 0.9527607 * CONCENT - 0.0009811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
        SECCSPHT = (cpWater(temp) * CONCofWATER + cpPrGl(temp) * CONCENTRATION) _
               * (1 + D0(ISECC) * CONCofWATER * CONCENTRATION) _
               + d1(ISECC) * (D2(ISECC) - temp) * CONCENTRATION * CONCofWATER _
               + D3(ISECC) * (D2(ISECC) - temp)
      ElseIf (ISECC = 2) Then
'   if Ethylene glycol mixture Specific Heat is being calculated ISECC is set to 2
    CONCENTRATION = (0.00137599 * CONCENT ^ 2 + 0.8828875 * CONCENT - 0.02004811) / 100#
    CONCofWATER = Abs(1 - CONCENTRATION)
        SECCSPHT = (cpWater(temp) * CONCofWATER + cpEtGl(temp) * CONCENTRATION) _
               * (1 + D0(ISECC) * CONCofWATER * CONCENTRATION) _
               + d1(ISECC) * (D2(ISECC) - temp) * CONCENTRATION * CONCofWATER _
               + D3(ISECC) * (D2(ISECC) - temp)
      ElseIf (ISECC = 3) Then
'   if methyl alcohol mixture Specific Heat is being calculated ISECC is set to 3
        SECCSPHT = (cpWater(temp) * CONCofWATER + cpMeoH(temp) * CONCENTRATION) _
               * (1 + D0(ISECC) * CONCofWATER * CONCENTRATION) _
               + d1(ISECC) * (D2(ISECC) - temp) * CONCENTRATION * CONCofWATER _
               + D3(ISECC) * (D2(ISECC) - temp)
      ElseIf (ISECC = 4) Then
'   if ethyl alcohol mixture Specific Heat is being calculated ISECC is set to 4
        SECCSPHT = (cpWater(temp) * CONCofWATER + cpEtoH(temp) * CONCENTRATION) _
               * (1 + D0(ISECC) * CONCofWATER * CONCENTRATION) _
               + d1(ISECC) * (D2(ISECC) - temp) * CONCENTRATION * CONCofWATER _
               + D3(ISECC) * (D2(ISECC) - temp)
      End If

'   Change from KJ/kg.K to J/kg.K
      SECCSPHT = SECCSPHT * 1000
   End Function

      Function TCWater(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of pure water between
' *         the temperature range of 230 to 400K.
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * TCWater: Thermal Conductivity                                    (W/m.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., Liley, P.E., and Saxena, S.'., 1970.
' *     Thermal Conductivity, non metallic liquids and gases,thermophysical properties of matter,
' *     Vol 3, TPRC data series.IFI/Plenum, New York
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'   the polynomial returns the value in (mW/cm.k)
' Argument
   ' Dim Tem As Double
            TCWater = (273.778 + 3.9 * (Tem + 273.15)) * 0.004184 _
                   * 0.1 ''convert to (W/m.k)

    End Function

Function TCPrGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of propylene glycol between
' *         253 to 400K.
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * TCPrGl: Thermal conductivity of propylene glycol                (W/m.K)
' *
' * Reference
' * =========
' * Stephan, K., and Hildwein, H., 1987.
' *     Recommended data of selected compounds and binary mixtures.
' *     DECHEMA,Chemistry Data Series, Vol. IV, part. 1+2.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   the polynomial returns the value in (mW/m.k)
            TCPrGl = (6.525E-07 * (Tem + 273.15) ^ 3 - 0.0019245191 _
               * (Tem + 273.15) ^ 2 + 0.8187420602 * _
               (Tem + 273.15) + 115.8385095349) _
                * 0.001 'convert to (W/m.k)
    End Function

    Function TCEtGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of Ethylene glycol between
' *         250 to 400K.
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * TCEtGl: Thermal conductivity of Ethylene glycol              (W/m.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., Liley, P.E., and Saxena, S.'., 1970.
' *     Thermal Conductivity, non metallic liquids and gases,thermophysical properties of matter,
' *     Vol 3, TPRC data series.IFI/Plenum, New York
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   the polynomial returns the value in (mW/cm.k)
            TCEtGl = (519.442 + 0.32092 * (Tem + 273.15)) * 0.004184 _
                  * 0.1 'convert to (W/m.k)

    End Function


 Function TCMeoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of Methanol between
' *         150-400K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * TCMeoH: Thermal conductivity of Methanol                       (W/m.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., Liley, P.E., and Saxena, S.'., 1970.
' *     Thermal Conductivity, non metallic liquids and gases,thermophysical properties of matter,
' *     Vol 3, TPRC data series.IFI/Plenum, New York
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   The polynomial returns the value in (mW/cm.k)
            TCMeoH = (687.314 - 0.680519 * (Tem + 273.15)) * 0.004184 _
                  * 0.1 'Convert to (W/m.k)
End Function


      Function TCEtoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Thermal conductivity of Ethanol between
' *         150-400K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * TCEtoH   : Thermal conductivity of Ethanol                    (W/m.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., Liley, P.E., and Saxena, S.'., 1970.
' *     Thermal Conductivity, non metallic liquids and gases,thermophysical properties of matter,
' *     Vol 3, TPRC data series.IFI/Plenum, New York
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' Argument
    'Dim Tem As Double
'   The polynomial returns the value in (mW/cm.k)
            TCEtoH = (609.512 - 0.70924 * (Tem + 273.15)) * 0.004184 _
                 * 0.1 'Convert to (W/m.k)
      End Function


      Function densWater(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Density of Water between the temperature range
' *         -34 to 96C
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * densWater: Density of Water                                    (kg/m3)
' *
' * Reference
' * =========
' * D.E Hare and Sorensen   (CHECK)
' * reference 2 missing
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

' Argument
    'Dim Tem As Double
'   if the temperature is less than 0 ' then the following polynomial is used
        If (Tem <= 0) Then
            densWater = 0.99986 + 6.69E-05 * Tem _
             - 8.486E-06 * Tem ^ 2 + 1.518E-07 * Tem ^ 3 _
             - 6.9484E-09 * Tem ^ 4 - 3.6449E-10 * Tem ^ 5 _
             - 7.497E-12 * Tem ^ 6
'   if the temperature is greater than 0 ' the following polynomial is used
        Else
            densWater = 1.55E-08 * Tem ^ 3 - 5.8378E-06 * Tem ^ 2 _
             + 1.08821E-05 * Tem + 1.0000941648
        End If
      End Function


    Function densPrGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Density of Propylene glycol between the
' *         temperature range 213 to 400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * densPrGl: Density of Propylene glycol                         (kg/m3)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
    'Dim Tem As Double
'   The polynomial returns the Density in kmol/m3
            densPrGl = (1.0923 / 0.26106 ^ _
                 (1 + (1 - ((Tem + 273.15) / 626)) ^ 0.20459)) _
                 * 76.095 * 0.001 'Convert to kg/m3 where 76.095 is the
                                   ' molecular weight of proplylene glycol
      End Function


    Function densEtGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Density of Ethylene glycol between the
' *         temperature range 200 to 400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * densEtGl: Density of Ethylene glycol                        (kg/m3)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   The polynomial returns the Density in kmol/m3
            densEtGl = (1.2342 / 0.27029 ^ _
             (1 + (1 - ((Tem + 273.15) / 629)) ^ 0.21997)) _
               * 78.135 * 0.001 'Convert to kg/m3 where 78.135
                                 'is the molecular weight of Ethylene glycol
      End Function

      Function densMeoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Density of Methanol between the
' *         temperature range 175 to 400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * densMeoH: Density of Methanol                                  (kg/m3)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
 '   Dim Tem As Double
'   The polynomial returns the Density in kmol/m3
            densMeoH = (2.308 / 0.27192 ^ _
                 (1 + (1 - ((Tem + 273.15) / 512.58)) ^ 0.2331)) _
                 * 32.042 * 0.001 'Convert to kg/m3 where 32.042
                              'is the molecular weight of Methanol
      End Function


      Function densEtoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Density of Ethanol between the
' *         temperature range 159-400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * densEtoH: Density of Ethanol                                    (kg/m3)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'            '159-400K
' Argument
   ' Dim Tem As Double
'   The polynomial returns the Density in kmol/m3
            densEtoH = (1.5223 / 0.26395 ^ _
                       (1 + (1 - ((Tem + 273.15) / 516.25)) ^ 0.2367)) _
                       * 46.069 * 0.001 'Convert to kg/m3 where 46.069
                                        'is the molecular weight of Ethanol
      End Function


      Function cpWater(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of pure Water in the
' *         temperature range of 236-400K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * cpWater:  specific heat of water                               (kJ/kg.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., and Makita, T., 1970.
' *     Specific heat, non metallic liquids and gases, thermophysical properties of matter,
' *     Vol 6, TPRC data series. IFI/Plenum, New York.
' * Westh, P., and Hvidt, A., 1993.
' *     Heat capacity of aqueous solutions of monohydric alcohols at subzero temperatures.
' *     Biophys. Chem. 46: 27-35.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   if the temperature greater than 0 use the following polynomial
        If (Tem >= 0) Then
'   The polynomial returns the specific heat in Btu/lb. F
            cpWater = (2.13974 - 0.00968137 * (Tem + 273.15) + _
                    2.68536E-05 * (Tem + 273.15) ^ 2 _
                  - 2.42139E-08 * (Tem + 273.15) ^ 3) _
                   * 4.184 '   Convert to kJ/kg.K
        Else
'   if the temperature less than 0 use the following polynomial
            cpWater = -1.134E-07 * Tem ^ 5 - 8.4011E-06 * Tem ^ 4 _
             - 0.0002459819 * Tem ^ 3 - 0.0027076312 * Tem ^ 2 _
             - 0.0168617731 * Tem + 4.1942562129
        End If
      End Function

    Function cpPrGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of Propylene Glycol in the
' *         temperature range of 213-400k
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * cpPrGl: specific heat Propylene Glycol                      (kJ/kg.K)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' '
' Argument
   ' Dim Tem As Double
'   The polynomial returns the specific heat in j/kmol.K
            cpPrGl = (58080 + 445.2 * (Tem + 273.15)) _
                   * 0.0131415 * 0.001  'Convert to kJ/kg.K
                                         '0.0131415 is the molecular weight term (1/76.095)
      End Function

      Function cpEtGl(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of Ethylene Glycol in the
' *         temperature range of 262-400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * cpEtGl: specific heat  of Ethylene Glycol                 (kJ/kg.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., and Makita, T., 1970.
' *     Specific heat, non metallic liquids and gases, thermophysical properties of matter,
' *     Vol 6, TPRC data series. IFI/Plenum, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   The polynomial returns the specific heat in Btu/lb. F
            cpEtGl = (0.016884 + 0.00335083 * (Tem + 273.15) - 7.224E-06 _
             * (Tem + 273.15) ^ 2 + 7.61748E-09 * (Tem + 273.15) ^ 3) _
             * 4.184 'Convert to kJ/kg.K
      End Function

      Function cpMeoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of Methanol 239.15 to 400 K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * cpMeoH: specific heat                                     (kJ/kg.K)
' *
' * Reference
' * =========
' * Touloukian, Y. S., and Makita, T., 1970.
' *     Specific heat, non metallic liquids and gases, thermophysical properties of matter,
' *     Vol 6, TPRC data series. IFI/Plenum, New York.
' * Westh, P., and Hvidt, A., 1993.
' *     Heat capacity of aqueous solutions of monohydric alcohols at subzero temperatures.
' *     Biophys. Chem. 46: 27-35.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
 '   Dim Tem As Double
'   if the temperature is less than 20 ' use the following polynomial
        If (Tem = 20) Then
            cpMeoH = 6.79332E-07 * (Tem + 273.15) ^ 3 - 0.000507395605 _
               * (Tem + 273.15) ^ 2 + 0.130806587813 * (Tem + 273.15) _
               - 9.271119425358
        Else
'   use the following polynomial expression if the temperature is greater than 20C
            cpMeoH = (0.582485 - 0.000375646 * (Tem + 273.15) _
                    - 1.67844E-06 * (Tem + 273.15) ^ 2 _
                   + 1.06214E-08 * (Tem + 273.15) ^ 3) _
                     * 4.184   'Convert to kJ/kg.K
        End If
      End Function


      Function cpEtoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the specific heat of Methanol 241.15 to 400 K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * cpEtoH: specific heat                                     (J/kg.K)
' *
' * Reference
' * =========
' * Stephan, K., and Hildwein, H., 1987.
' *     Recommended data of selected compounds and binary mixtures.
' *     DECHEMA,Chemistry Data Series, Vol. IV, part. 1+2.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

' Argument
 '   Dim Tem As Double
'   Reduced temperature. Calculated by dividing the temperature with
'   critical temperature of 513.92
'   Polynomial gives the value of specific heat in Kj/Kmol.K
        cpEtoH = (8.3143 * (11.7928 - 6.49805 * ((Tem + 273.15) / 513.92) _
            - 3.43888 * ((Tem + 273.15) / 513.92) ^ 2 _
                + 33.9621 * ((Tem + 273.15) / 513.92) ^ 3)) _
                   / 46.069 'Convert to kJ/kg.K where 46.069
                         'is the molecular weight of Ethanol
      End Function


       Function muWater(Tem As Double)

'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Viscosity of pure water between the temperature
' *         range of -23 to 130C
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * muWater: Viscosity of pure water                         (CentiPoise)
' *
' * Reference
' * =========
' * Touloukian, Y. S., Saxena, S.'., and Hestermans, P., 1970.
' *         Viscosity, thermophysical properties of matter, Vol 11,
' *         TPRC data series. IFI/Plenum, New York.
' * Halfpap, B. L., 1981.
' *         An investigation of some properties of supercooled fluids using
' *         photon correlation spectroscopy.
' *         M.S. Thesis. Kansas State University. Manhattan, KS
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
    'Dim Tem As Double
            If (Tem = 0) Then
'   Polynomial gives the value of Viscosity for temperature less than 0C
                muWater = -0.000192677 * Tem ^ 3 - 0.001689785 * Tem ^ 2 _
                        - 0.085518661 * Tem + 1.770253561
            Else
'   Polynomial gives the value of Viscosity for temperature more than/ equal to 0C
                muWater = 0.02414 * 10 ^ (247.8 / ((Tem + 273.15) - 140))
            End If
      End Function

       Function MuPrGl(Tem As Double)

'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Viscosity of Propylene Glycol between
' *         the temperature range of 233-400K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * MuPrGl: Viscosity of Propylene Glycol                          (CentiPoise)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.

' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
    'Dim Tem As Double
'   Polynomial gives the value of value of Viscosity in Centipoise
            MuPrGl = (Exp(-293.07 + (17494 / (Tem + 273.15)) _
             + 40.576 * Log((Tem + 273.15)))) _
               * 1000#
      End Function


       Function MuEtGl(Tem As Double)

'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Viscosity of Ethylene Glycol between
' *         the temperature range of 200-400K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * MuEtGl: Viscosity of Ethylene Glycol                    (CentiPoise)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
    'Dim Tem As Double
'   Polynomial gives the value of  Viscosity in Centipoise
            MuEtGl = (Exp(-16.548 + (3022.7 / (Tem + 273.15)) + _
                 0.08248 * Log((Tem + 273.15)))) _
                 * 1000#
      End Function


     Function MuMeoH(Tem As Double)

'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Viscosity of Methanol between
' *         the temperature range of 230-375K
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * MuMeoH: Viscosity of Methanol                                    (CentiPoise)
' *
' * Reference
' * =========
' * Daubert, T.E., and Danner, R.P., 1989.
' *     Physical and thermodynamic properties of pure chemicals: data compilation.
' *     Hemisphere Pub. Corp, New York.
' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
   ' Dim Tem As Double
'   Polynomial gives the value of  Viscosity in Centipoise
            MuMeoH = (Exp(-7.288 + (1065.3 / (Tem + 273.15)) _
                 - 0.6657 * Log((Tem + 273.15)))) _
                 * 1000

      End Function


     Function MuEtoH(Tem As Double)
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' *
' * PURPOSE:  Calculate the Viscosity of Ethanol between
' *         the temperature range of 200-400K
' *
'*^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
' * INPUTS
' * ======
' * TEMP     : Fluid temperature                                     (')
' *
' * OUTPUT
' * ======
' * MuEtoH: Viscosity of Ethanol                                     (CentiPoise)
' *
' * Reference
' * =========
' * Stephan, K., and Hildwein, H., 1987.
' *     Recommended data of selected compounds and binary mixtures.
' *     DECHEMA,Chemistry Data Series, Vol. IV, part. 1+2.

' ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
'
' Argument
  '  Dim Tem As Double
'   returns the value of viscosity in Centipoise
          MuEtoH = (69.8963 * Exp((877.267 / ((Tem + 273.15) - 43.8958)) _
                 - 2.13138 * ((Tem + 273.15) / 513.92) ^ 2.0094)) _
                   * 0.001

      End Function
      
