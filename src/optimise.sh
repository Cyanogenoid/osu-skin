OPTIONS='--enable-id-stripping --enable-comment-stripping --shorten-ids --remove-metadata'

for f in *.svg; do
  if [[ ! $f == "selection-mod-"* ]]; then
    scour $OPTIONS -i $f -o $f.new
    rm $f
    mv $f.new $f
  fi
done
