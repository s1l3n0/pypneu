% from http://www.cs.uni-potsdam.de/~torsten/Potassco/Talks/robotsIULP15.pdf

#external goal(1..16).

target(red, 5, 2) :- goal(1).
target(red, 15, 2) :- goal(2).
target(green, 2, 3) :- goal(3).
target(blue, 12, 3) :- goal(4).
target(yellow, 7, 4) :- goal(5).
target(blue, 4, 7) :- goal(6).
target(green, 14, 7) :- goal(7).
target(yellow, 11, 8) :- goal(8).
target(yellow, 5, 10) :- goal(9).
target(green, 2, 11) :- goal(10).
target(red, 14, 11) :- goal(11).
target(green, 11, 12) :- goal(12).
target(yellow, 15, 13) :- goal(13).
target(blue, 7, 14) :- goal(14).
target(red, 3, 15) :- goal(15).
target(blue, 10, 15) :- goal(16).

robot(red; green; blue; yellow).

#external  pos((red; green; blue; yellow), 1..16, 1..16).