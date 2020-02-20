#include "colors.inc"
camera { perspective location <0,0,-4> look_at <0,0,0>} 
light_source { <1,3,-3>, White}
box {<-1,-1,-1>, <1,1,1,>pigment {Red}}   
plane { y, -1 pigment {White} }