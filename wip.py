import pandas as pd

df = pd.read_csv('https://data.boston.gov/export/9fd/bdc/9fdbdcad-67c8-4b23-b6ec-861e77d56227.tsv','\t')


df[df.Street == 'Worcester St']

between 42.340865, -71.079541 tremont and columbus
df.loc[(df['Street'] == 'Worcester St') & (df['from'] == 'Tremont St'), 'from_lat'] = 42.340150
df.loc[(df['Street'] == 'Worcester St') & (df['from'] == 'Tremont St'), 'from_lng'] = -71.078852

df.loc[(df['Street'] == 'Worcester St') & (df['from'] == 'Washington St'), 'from_lat'] = 42.337483
df.loc[(df['Street'] == 'Worcester St') & (df['from'] == 'Washington St'), 'from_lng'] = -71.075638


df.loc[(df['Street'] == 'Worcester St') & (df['to'] == 'Columbus Ave'), 'to_lat'] = 42.341588
df.loc[(df['Street'] == 'Worcester St') & (df['to'] == 'Columbus Ave'), 'to_lng'] = -71.080440


df.loc[(df['Street'] == 'Worcester St') & (df['to'] == 'Tremont St'), 'to_lat'] = 42.340150
df.loc[(df['Street'] == 'Worcester St') & (df['to'] == 'Tremont St'), 'to_lng'] = -71.078852


#street_from = dict()
for street, _from in df[['Street','from']].drop_duplicates().values:
    
    if (street,_from) not in street_from:
        lnk = 'https://maps.googleapis.com/maps/api/geocode/json?API_KEY=AIzaSyCi9iAy7BR-MmHxqHe3gjDnwTWN_-MUfj4&address={}+&+{},+Boston,+MA'.format(street,_from)
        street_from[(street,_from)] = requests.get(lnk).json()
    #d[(street,_from)]['lat'] = lat
    #d[(street,_from)]['lng'] = lng
    #coords = requests.get(lnk).json()['results'][0]['geometry']['location']
    #lat = coords['lat']
    #lng = coords['lng']
