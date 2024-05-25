reset
set terminal png
#set terminal pngcairo enhanced font 'Arial,20'

FILES = "filmtrust.dat ml-100k.dat ml-latest-small.dat rng-1000-1000-001.dat rng-1000-1000-01.dat rng-400-200-001.dat rng-400-200-01.dat rng-800-400-001.dat rng-800-400-01.dat"

set autoscale xfix
set autoscale yfix
set logscale x
set xlabel 'k (log scale)'

do for [datfile in FILES] {
	mainname = sprintf('%s', split(datfile, ".")[1])
	
	yname = "mean squared error"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:2 title "original" with lp ps 0.5 lw 2 lt 7 lc rgb "#888888" , \
	datfile u 1:5 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:8 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:11 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"
	
	yname = "above threshold count"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:3 title "original" with lp ps 0.5 lw 2 lt 7 lc rgb "#888888" , \
	datfile u 1:6 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:9 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:12 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"
	
	yname = "effective density"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:4 title "original" with lp ps 0.5 lw 2 lt 7 lc rgb "#888888" , \
	datfile u 1:7 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:10 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:13 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"
	
	yname = "support distance"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:14 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:15 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:16 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"
	
	yname = "support count"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:17 title "original" with lp ps 0.5 lw 2 lt 7 lc rgb "#888888" , \
	datfile u 1:18 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:19 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:20 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"

	yname = "algorithm runtime"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:21 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:22 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:23 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"
	
	yname = "recommendation system runtime"
	name = mainname." - ".yname
	set output name.".png"
	set title name
	set ylabel yname
	plot \
	datfile u 1:24 title "original" with lp ps 0.5 lw 2 lt 7 lc rgb "#888888" , \
	datfile u 1:25 title "approx" with lp ps 0.5 lw 2 lt 6 lc rgb "#884444" , \
	datfile u 1:26 title "svg" with lp ps 0.5 lw 2 lt 5 lc rgb "#444488" , \
	datfile u 1:27 title "nmf" with lp ps 0.5 lw 2 lt 7 lc rgb "#448844"

}
