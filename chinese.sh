geoiplookup  112.17.65.50 | head -1 > chinalocation
s=$(cat chinalocation)
if [[ "$s" == "GeoIP Country Edition: CN, China" ]]
then echo "We're in china" ; echo "hello";read hello ; $(./hellochinese);echo "how are you?" ; read hru ; $(./hruchina.sh)
fi

