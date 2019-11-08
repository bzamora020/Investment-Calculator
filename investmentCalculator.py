import random

while True:
    simYears = int(input('Please enter the number of years to simulate: '))
    print('Below are the investment options and their ranges of returns : \nMoney Market : (0.1%,8.8%) \nBond :         (0.8%, 12.0%) \nReal Estate :  (-1.2%, 8.4%) \nS&P :          (-43.84%, 52.56%)')
    investCapital = input('Please enter your investment capital: ')
    print('Please enter the amount of investment in each category:')
    moneyMarket = int(input('Money Market =  '))
    bond = int(input('Bond         =  '))
    realEstate = int(input('Real Estate  =  '))
    s_p = int(input('S&P          =  '))
    initialInvestment = int(investCapital)

    if (moneyMarket + bond + realEstate + s_p) == initialInvestment:

        yearStart = []
        yearRet = []
        yearEnd = []
        i = 0
        x = 0
        y = 0
        z = 0
        yearsTotalReturn = 0

        while i < simYears:
            i += 1

            yearStartTotal = int((moneyMarket + bond + realEstate + s_p))
            yearStart.append(yearStartTotal)

            startMoney = moneyMarket
            startBond = bond
            startReal = realEstate
            startS_p = s_p

            moneyRate = random.uniform(0.1, 8.8)
            moneyRate = float(moneyRate)
            # Displays money market rate
            # print("%.2f" % moneyRate)

            moneyYearly = moneyRate/100 * moneyMarket
            # Prints yearly return for money market
            # print(moneyYearly)

            # Prints ending amt for money market
            moneyMarket = (moneyMarket + moneyYearly)
            # This is the new starting amount for the Money Market
            # print(moneyMarket)

            bondRate = random.uniform(0.8, 12.0)
            bondRate = float(bondRate)
            # Displays money bond
            # print(bondRate)

            bondYearly = bondRate/100 * bond
            # Prints yearly return for bond
            # print(bondYearly)

            # Prints ending amt for bond
            bond = (bond + bondYearly)
            # This is the new value for Bond
            # print(bond)

            realRate = random.uniform(-1.2, 8.4)
            realRate = float(realRate)
            # Displays money bond
            # print(realRate)

            realYearly = realRate/100 * realEstate
            # Prints yearly return for Real Estate
            # print(realYearly)

            # Prints ending amt for Real Estate
            realEstate = (realEstate + realYearly)
            # This is the new value for Real Estate
            # print(realEstate)

            s_pRate = random.uniform(-43.84, 52.56)
            s_pRate = float(s_pRate)
            # Displays money bond
            # print(s_pRate)

            s_pYearly = s_pRate/100 * s_p
            # Prints yearly return for Real Estate
            # print(s_pYearly)

            # Prints ending amt for Real Estate
            s_p = (s_p + s_pYearly)
            # This is the new value for S&P
            # print(s_p)
            yearRetTotal = (moneyYearly + bondYearly + realYearly + s_pYearly)
            yearEndTotal = (moneyMarket + bond + realEstate + s_p)
            yearsTotalReturn = (yearsTotalReturn + yearRetTotal)

            yearRet.append(yearRetTotal)

            yearEnd.append(yearEndTotal)
            print('\nYear ', i, ' Return Details:\n')
            print(' CATEGORIES          START AMT       RATE        YEARLY RET.         ENDING AMT')
            print('Money Market        ', "%.2f" % startMoney, '       ' "%.2f" % moneyRate, '        ' "%.2f" % moneyYearly, '           ' "%.2f" % moneyMarket)
            print('Bond                ', "%.2f" % startBond, '        ' "%.2f" % bondRate, '       ' "%.2f" % bondYearly, '          ' "%.2f" % bond)
            print('Real Estate         ', "%.2f" % startReal, '       ' "%.2f" % realRate, '       ' "%.2f" % realYearly, '           ' "%.2f" % realEstate)
            print('S&P                 ', "%.2f" % startS_p, '       ' "%.2f" % s_pRate, '      ' "%.2f" % s_pYearly, '          ' "%.2f" % s_p)
            print('\nYear', i, 'Total', '       ', "%.2f" % yearStartTotal, '           ', '     ', "%.2f" % yearRetTotal, '          ', "%.2f" % yearEndTotal)

        for i in yearStart:
            x += 1
            print('\nYear', x, 'Starting Amount',  "%.2f" % i)
        for i in yearRet:
            y += 1
            print('\nYear', y, 'Yearly Ret',  "%.2f" % i)
        for i in yearEnd:
            z += 1
            print('\nYear', z, 'Ending Amt',  "%.2f" % i)

        print('\nInvestment Amount = ', "%.2f" % initialInvestment)
        print('Ending Balance = ', "%.2f" % yearEnd[-1])
        print(z, 'Years total returns = ', "%.2f" % yearsTotalReturn)
