#!/bin/bash
my_string=$(sensors | grep temp1 | tr -d \)tem:p=\(cri) 
my_array=($(echo $my_string | tr " " "\n"))
cat <<EOF > /disk/dev/VMConfigKeeper/myprojectenv/temp_cpu/myjson.json
{"CPU_temp" : "${my_array[1]}",
 "GPU_temp" : "${my_array[4]}",
 "uptime" : "$(uptime)"
}
EOF

