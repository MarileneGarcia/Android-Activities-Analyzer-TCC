/*  tcc.h - Library of Main Code of the Program
 
    Copyright (c) 2022, Garcia M. A. <marilenegarcia@usp.br>

    This file is part of Android Activities Analyzer Program.

    Android Activities Analyzer Program is free software: you 
    can redistribute it and/or modify it under the terms of the 
    GNU General Public License as published by the Free Software 
    Foundation, either version 3 of the License, or (at your option) 
    any later version.
   
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
   
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#pragma once
#ifndef TCC_H
#define TCC_H

#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <sstream> 
#include <regex>
#include <sys/stat.h>
#include <algorithm>

using namespace std;

/* The message of each log */
typedef struct Message{
    string message;   
    Message* next; 
} Message;

/* Thread identificator */
class Tid { 
    private:
        int tid;
        vector<string> functions;

    public:           
        Tid(int tid) {     
        this->tid = tid;
        }

        int get_tid(){
            return tid;
        }

        void add_function(string function) {
            functions.push_back(function);
        }

        vector<string>& get_functions() {
            return functions;
        }

        void print_all_functions(){
            cout << "The functions related to the thread " << tid << " are: " << endl;

            for(string function : functions){
                cout << function << endl;
            }
        }
};

/* Process identificator */
class Pid { 
    private:
        int pid;
        vector<Tid> tids;

    public:           
        Pid(int pid) {     
        this->pid = pid;
        }

        int get_pid(){
            return pid;
        }

        void add_tid(int tid) {
            tids.push_back(Tid(tid));
        }

        vector<Tid>& get_tids() {
            return tids;
        }

        void print_all_tids(){
            cout << "The threads related to the process " << pid << " are: " << endl;

            for(Tid tid : tids){
                cout << tid.get_tid() << endl;
            }
        }
};

/* Auxiliar Functions */
void apply_command(const char *);
bool WriteFile(string, string);
string GetStdoutFromCommand(string);
void printPids(vector<Pid>);
vector<int> split_number(string, char);
vector<string> split_character(string, char);
vector<string> pick_functions(string, string);

/* Register Activity */
bool ProgramBegin();
void CheckPath(string);
bool IsPathExist(const string &);
vector<Pid> FileOrganization(string);
vector<Pid> allPids(string);
void InitialOrganization(string);
bool createDirectories(string);
vector<Pid> PidsTidsList(string);
bool PidsTidsDirectories(vector<Pid>&, string);
bool TidFunctions(vector<Pid>&);
vector<string> FunctionsDirectory(string, string);
void CreateFileAllInformation(vector<Pid>&);
bool CreateActivityDirectory(string);
bool CreateOtherWayActivity(string, string);
bool RegisterActivity(string, string);
bool FinishRegisterActivity(string, vector<int>);

/* Analyze Activity */
bool CompareFile(string);
double AnalizeZipSize(string);
double AnalizeCommands(string);

#endif