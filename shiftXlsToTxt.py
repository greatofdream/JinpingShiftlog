import pandas as pd, argparse
psr = argparse.ArgumentParser()
psr.add_argument('-i', dest="input", help="input xlsx file")
psr.add_argument('-o', dest="output", help="output txt file")
psr.add_argument('-O', dest='goodrun', help='goodrun list file')
psr.add_argument('-t', dest='tail', help='cut down tail data')
args = psr.parse_args()
tail = int(args.tail)
xlsx = pd.read_excel(args.input, sheet_name='shiftLog', index_col=None, na_values=['NA'])
xlsxLength = xlsx.shape[0]
formerDate = ''
with open(args.output, 'w') as opt, open(args.goodrun, 'w') as opt2:
    for index, row in xlsx.iterrows():
        if index>(xlsxLength+tail-1):
            break
        #print(row)
        if formerDate!=row['Date']:
            opt.write('{}\n'.format(row['Date'].strftime('%Y-%m-%d')))
            formerDate = row['Date']
            opt.write('{}\n'.format(row['Weather']))
        if not pd.isna(row['EnterTime']):
            opt.write('{} Get in Lab\n'.format(row['EnterTime'].strftime('%H:%M')))
        opt.write('{} stop phy run {}\n\n'.format(row['PhyEndTime'].strftime('%H:%M'), row['PhyEndRun']))
        if not pd.isna(row['EnterTime']):
            opt.write('light: {:.2f} MO cm, {:.1f} degree\nDark: {:.2f} MO cm, {:.1f} degree\n'.format(row['Light'], row['LightTemperature'], row['Dark'], row['DarkTemperature']))
            opt.write('Outer tank: {:.2f} cm, {:.1f} degree\nInner tank: {:.2f} cm, {:.1f} degree\n'.format(row['Outer'], row['OuterTemperature'], row['Inner'], row['InnerTemperature']))
            opt.write('\n')
        opt.write('{} start ped run {}\n{} stop ped run {}\n'.format(row['PedStartTime'].strftime('%H:%M'), row['PedRun'], row['PedEndTime'].strftime('%H:%M'), row['PedRun']))
        opt.write('{} start phy run {}\n'.format(row['PhyStartTime'].strftime('%H:%M'), row['PhyRun']))
        opt.write('\n')
        if not (pd.isna(row['EnterTime']) or pd.isna(row['Oxygen'])):
            opt.write('Nitrogen input: {:.2f} Mpa\nNitrogen output: {:.2f} Mpa\nFlux: {:.2f} sccm\nInflation: {}\n'.format(row['N2In'], row['N2Out'], row['flux'], row['inflation']))
            opt.write('Oxygen: {:.1f}%, {:.1f} degree\n\n'.format(row['Oxygen'], row['Temperature']))
        if not pd.isna(row['Accident']):
            opt.write('Accident:\n{}\n'.format('\n'.join(str(row['Accident']).split(';'))))
        opt.write('\n')
        opt2.write('{}\n'.format(row['PhyRun']))
    opt2.write('\n')