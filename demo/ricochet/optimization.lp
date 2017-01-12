% from http://www.cs.uni-potsdam.de/~torsten/Potassco/Talks/robotsIULP15.pdf

goon(T) :- target(R,X,Y), T = 0..horizon, not pos(R,X,Y,T).

:- move(R, DX, DY, T-1), time(T), not goon(T-1), not move(R, DX, DY, T).

#minimize {1, T: goon(T)}.