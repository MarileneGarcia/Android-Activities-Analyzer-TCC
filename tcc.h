#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>
#include <sstream> 

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
        Message* msg_head;
        Message* msg_tail; 

    public:           
        Tid(int tid) {     
        this->tid = tid;
        msg_head = NULL;
        msg_tail = NULL;
        }

        int get_tid(){
            return tid;
        }

        void add_message(string message) {
            if(msg_head == NULL){
                msg_head = (Message*) malloc (sizeof(Message));
                if(msg_head == NULL) {
                    cout << "Error to create a first message of tid: " + tid << endl;
                    exit(0);
                }
                msg_head -> message = message;
                msg_head -> next = NULL;
                msg_tail = msg_head;
            } else {
                msg_tail -> next = (Message*) malloc (sizeof(Message));
                if(msg_tail -> next == NULL) {
                    cout << "Error to create an message of tid: " + tid << endl;
                    exit(0);
                }
                msg_tail -> next -> message = message;
                msg_tail -> next -> next = NULL;
                msg_tail = msg_tail -> next;
            }
        }

        void print_all_messages(){
            int i = 0;
            while (msg_tail -> next != NULL){
                cout << "Message " << i << ": " << msg_tail -> message << endl; 
                i++;
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
            cout << "As threads referentes ao processo " << pid << "são: " << endl;

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
string split_character(string, char);
vector<string> pick_functions(string, string);
vector<string> read_functions(string);