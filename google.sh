echo "Please fire your query"
read q
echo $q|sed -e 's/ /+/g' > plus
z=$(cat /root/Desktop/hackathon/plus)
x=$(cat /root/Desktop/hackathon/city)
echo $z
echo $x
chromium google.com/search?q=$z+$x
