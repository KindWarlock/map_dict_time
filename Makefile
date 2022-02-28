run: map dict
	python3 ./make_graphs.py
map:
	g++ main.cpp -o map_cpp
dict:
	python3 ./main.py	