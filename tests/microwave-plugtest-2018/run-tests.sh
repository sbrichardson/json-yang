#!/bin/bash -i

# "test suite" exits 0 only if all tests exit with 0

EXIT=0
printf '%-16s%-16s%-32s%-8s\n' "STRATEGY" "WHAT" "JSON" "OUT"
for STRATEGY in pyang yanglint; do
    for WHAT in data; do
	for JSON in mw-topo eth-topo eth-tran-service; do
	    rm -rf target downloads

	    validate -j $JSON.json -w "$WHAT" -y . -s $STRATEGY 2> .stderr 1> /dev/null
	    OUT=$?
	    EXIT=$((EXIT + OUT))
	    printf '%-16s%-16s%-32s%-8s\n' "$STRATEGY" "$WHAT" "$JSON" "$OUT"
	    rm -f .stderr
	done
    done
done
exit $EXIT