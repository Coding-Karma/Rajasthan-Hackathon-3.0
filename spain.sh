geoiplookup 88.26.241.248 | head -1 > spainlocation
s=$(cat spainlocation) 
echo $s
#if [ "$s" = "GeoIP Country Edition: ES, Spain" ] then
echo "We're in spain so it's gonna be spanish"
echo "Hello"
read hello
$(./hola.sh)
echo "How are you"
read hru
$(./hru.sh)
