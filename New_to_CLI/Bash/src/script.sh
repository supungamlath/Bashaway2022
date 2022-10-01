START_TIME=$(date +%H:%M:%S)
read -p "Enter team name: " TEAM_NAME
TEAM_NAME_TIME=$(date +%H:%M:%S)
TEAM_NAME="${TEAM_NAME// /_}"


read -p "Enter number of members: " N

NAMES=()
NICS=()
PHONES=()
ADDRS=()
TIMES=()
IFS=

for ((i=1; i<=N; i++)){
  read -p "Enter name of member $i: " NAME 
  read -p "Enter NIC of member $i: " NIC 
  read -p "Enter phone number of member $i: " PHONE 
  read -p "Enter address of member $i: " ADDR 
  NAMES+=($NAME)
  NICS+=($NIC)
  PHONES+=($PHONE)
  ADDRS+=($ADDR)
  TIME=$(date +%H:%M:%S)
  TIMES+=($TIME)
}
END_TIME=$(date +%H:%M:%S)
echo "Start time of script ${START_TIME}" > ${TEAM_NAME}.txt

echo "Team name: ${TEAM_NAME}" >> ${TEAM_NAME}.txt
echo "End time at entering team name: ${TEAM_NAME_TIME}" >> ${TEAM_NAME}.txt
echo "Number of members: ${N}" >> ${TEAM_NAME}.txt


for ((i=0; i<N; i++)){
  j=$((i+1))
  echo "Name of member $j: ${NAMES[$i]}" >> ${TEAM_NAME}.txt
  echo "NIC of member $j: ${NICS[$i]}" >> ${TEAM_NAME}.txt
  echo "Phone number of member $: ${PHONES[$i]}" >> ${TEAM_NAME}.txt
  echo "Address of member $j: ${ADDRS[$i]}" >> ${TEAM_NAME}.txt
  echo "End time at entering details of member $j: ${TIMES[$i]}" >> ${TEAM_NAME}.txt
}

echo "End time of script ${END_TIME}" >> ${TEAM_NAME}.txt
  



