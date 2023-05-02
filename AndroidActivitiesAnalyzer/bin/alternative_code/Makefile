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
	python3 interface_alternative.py || interface_alternative.py

install:
	sudo apt install sed
	sudo apt-get install python3-tk || sudo apt-get install python-tk
	pip3 install python-igraph || pip install python-igraph
# pip3 install tk || pip install tk

compile: tcc_alternative.cpp tcc.h
	g++ tcc_alternative.cpp -o program.out
