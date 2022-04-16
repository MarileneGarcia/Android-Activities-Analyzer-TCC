#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <sstream> 
#include <regex>

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

        vector<string> get_functions() {
            return functions;
        }

        void print_all_functions(){
            cout << "The functions related to the thread" << tid << "are: " << endl;

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

        vector<Tid> get_tids() {
            return tids;
        }

        void print_all_tids(){
            cout << "The threads related to the process " << pid << "are: " << endl;

            for(Tid tid : tids){
                cout << tid.get_tid() << endl;
            }
        }
};

void manageDirectories(string);
vector<Pid> PidsTidsList(string);
bool PidsTidsDirectories(vector<Pid>, string);
bool TidFunctions(vector<Pid>);
vector<int> split_number(string, char);
vector<string> split_character(string, char);
vector<string> pick_functions(string, string);
vector<string> read_functions(string, string);