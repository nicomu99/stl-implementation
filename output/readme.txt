seperated by " " each line contains:

0: k
1: 0
2: above_threshold_og
3: density_og
4: mse_ap
5: above_threshold_ap
6: density_ap
7: mse_svg
8: above_threshold_svg
9: density_svg
10: mse_nmf
11: above_threshold_nmf
12: density_nmf
13: dist_ap
14: dist_svg
15: dist_nmf
16: len(support_og)
17: len(support_ap)
18: len(support_svg)
19: len(support_nmf)
20: algorithm_time
21: svg_time
22: nmf_time
23: original_rec_time
24: approx_rec_time
25: svg_rec_time
26: nmf_rec_time

in output use the makefile to greate PNGs,
you might need to change the gnuplot_script.gp file where the *.dat files are hardcoded.