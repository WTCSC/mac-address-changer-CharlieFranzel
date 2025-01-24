checkifvalid() {
mac=$1
for (( i=0; i<${#mac}; i++ )); do
    char="${string:$i:1}"
    echo "Character: $char"
done

}

checkifvalid "11:11:11:11:11:11"