#Jake Hayes
#GDAL/OGR

#Question 1
"""
    Yes, based on the results from previous examples of GetEnvelope(), GetArea(), and Centroid()
    the inputs for question 1 are reasonable.
"""

#Question 2
from osgeo import ogr
driver = ogr.GetDriverByName('ESRI Shapefile')

vector = None
while vector is None: #Making sure that the input for the vector is valid
    fname = raw_input('Enter shapefile name: ')
    vector = driver.Open(fname, 0)

layer = vector.GetLayer(0)
num_features = layer.GetFeatureCount()
print 'There are %s feature'%(num_features) #Providing information to user
f = layer.GetFeature(0)
n = f.GetFieldCount()
print 'Here are all the fields:' #Give fields to user so user can know what information is in shapefile
for i in range(n):
    print f.GetFieldDefnRef(i).GetName(),
print

while True: #Loops until user enters 'DONE'
    i = raw_input('Enter feature index (\'DONE\' to exit\): ')
    if i == 'DONE':
        break
    if not i.isdigit():
        print 'Invalid index'
    else:
        i = int(i)
        if i<0 or i>num_features:
            print 'Invalid index'
        else:
            f = layer.GetFeature(i)
            print f.items()
            geom = f.GetGeometryRef() #Placeholder for reference
            print 'Number of geometries: %d'%(geom.GetGeometryCount()) #provide geometries
            print 'Centroid: ', geom.Centroid() #provide centroid
            print 'Area: ', geom.GetArea() #provide areas


