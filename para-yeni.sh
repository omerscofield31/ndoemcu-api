#!/bin/bash
grdata=$(curl -s https://api.genelpara.com/embed/altin.json | jq '.[] .alis' | sed  's/"//g' | head -n 1)
ceyrekdata=$(curl -s https://api.genelpara.com/embed/altin.json | jq '.[] .alis' | sed  's/"//g' | head -n 2 | tail -n 1)
dolardata=$(curl -s https://api.genelpara.com/embed/doviz.json | jq '.[] .alis' | sed  's/"//g' | head -n 1)
portfoy=$(echo "$grdata*1.5+$dolardata*120+$ceyrekdata" | bc)
date +%m/%d/%y
echo Dolar $dolardata
echo GR Altın $grdata
echo Ceyrek Altın $ceyrekdata
echo Portfoy Toplamı $portfoy
if ! grep -q $(date +%m/%d/%y) "para.csv" ; then
echo "$(date +%m/%d/%y),$portfoy,$grdata,$ceyrekdata,$dolardata" >> para.csv
echo Gün dosyaya işlendi !
fi

