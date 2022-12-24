for d in */ ; do
    cd "$d"
    for f in *-[0-9].py; do
        echo "$f"
        python3 "$f"
    done
    cd ".."
done
