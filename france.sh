geoiplookup 94.23.205.32 | head -1 > francelocation
s=$(cat francelocation)
if [[ "$s" == "GeoIP Country Edition: FR, France" ]]
then echo "We're in france" ; echo "hello" ; read hello ; $(./hellofrench);echo "how are you?";read hru;$(./hrufrench.sh) 
fi
