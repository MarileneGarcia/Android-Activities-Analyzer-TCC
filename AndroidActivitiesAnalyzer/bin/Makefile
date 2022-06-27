#    Makefile
# 
#    Copyright (c) 2022, Garcia M. A. <marilenegarcia@usp.br>
#
#    This file is part of Android Activities Analyzer Program.
#
#    Android Activities Analyzer Program is free software: you 
#    can redistribute it and/or modify it under the terms of the 
#    GNU General Public License as published by the Free Software 
#    Foundation, either version 3 of the License, or (at your option) 
#    any later version.
#   
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#   
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


run:
	python3 interface.py || python interface.py

install:
	sudo apt install sed
	pip3 install tk || pip install tk
	pip3 install python-igraph || pip install python-igraph

compile: tcc.cpp tcc.h
	g++ tcc.cpp -o program.out