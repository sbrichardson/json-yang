#!/bin/bash -i

# "test suite" exits 0 only if all tests exit with 0

EXIT=0
printf '%-16s%-16s%-8s\n' "STRATEGY" "WHAT" "OUT"
for STRATEGY in pyang yanglint; do
    for WHAT in data; do
        rm -rf target downloads

        validate -j use-case-1-odu2-service.json -w "$WHAT" -m models -s $STRATEGY 2> .stderr 1> /dev/null
	OUT=$?
	EXIT=$((EXIT + OUT))
	printf '%-16s%-16s%-8s\n' "$STRATEGY" "$WHAT" "$OUT"
	rm -f .stderr
    done
done
exit $EXIT
