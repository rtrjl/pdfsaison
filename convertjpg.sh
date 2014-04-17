convert input.jpg -resize 670x375 -background black -compose Copy -gravity center -extent 670x375 -quality 92 output.jpg

ls -1 *.JPG | parallel -j 4 convert '{}' -resize 1500x -quality 89% '{.}-mini.jpg'
