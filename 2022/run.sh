for d in "$1"/ ; do
    cd "$d"
    for f in *-[0-9].py; do
        python3 "$f"
    done
    cd ".."
done
