OPTIONS='--enable-id-stripping --enable-comment-stripping --shorten-ids --remove-metadata'

for f in *.svg; do
  if [[ ! $f == "selection-mod-"* ]]; then
    scour $OPTIONS --quiet -i "$f" -o "$f.new"
    if [[ $(wc -c < "$f.new") -lt $(wc -c < "$f") ]]; then
	  rm $f
	  mv $f.new $f
	  echo Optimised $f.
	else
	  rm $f.new
	fi
  fi
done
