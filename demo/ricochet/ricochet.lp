% from http://www.cs.uni-potsdam.de/~torsten/Potassco/Talks/robotsIULP15.pdf

time (1..horizon).

dir(-1, 0; 1, 0; 0, -1; 0, 1).

stop( DX, DY, X, Y) :- barrier(X, Y, DX, DY).
stop(-DX, -DY, X+DX, Y+DY) :- stop(DX, DY, X, Y).

pos(R, X, Y, 0) :- pos(R,X,Y).

1{move(R, DX, DY, T): robot(R), dir(DX, DY)}1 :- time(T).

move(R ,T) :- move(R, _ , _, T).

halt(DX, DY, X-DX, Y-DY, T)
  :- pos(_, X, Y, T), dir(DX, DY), dim(X-DX), dim(Y-DY), not stop(-DX,-DY,X,Y), T < horizon.

goto(R, DX, DY, X, Y, T)
  :- pos(R, X, Y, T), dir(DX, DY), T < horizon.
goto(R, DX, DY, X+DX, Y+DY, T)
  :- goto(R, DX, DY, X, Y, T), dim(X + DX), dim(Y + DY), not stop(DX, DY, X, Y), not halt(DX, DY, X, Y, T).
pos(R, X, Y, T)
  :- move(R, DX, DY, T), goto(R, DX, DY, X, Y, T-1), not goto(R, DX, DY, X+DX, Y+DY, T-1).
pos(R, X, Y, T)
  :- pos(R, X, Y, T-1), time(T), not move(R,T).

:- target(R, X, Y), not pos(R, X, Y, horizon).

#show move/4.