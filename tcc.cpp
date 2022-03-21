#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>

using namespace std;

/* The message of each log */
typedef struct Events{
    string event;   
    Events* next; 
} Events;

/* Thread identificator */
class Tid { 
    private:
        int tid;
        Events* event_head;
        Events* event_tail; 

    public:           
        Tid(int tid) {     
        this->tid = tid;
        event_head = NULL;
        event_tail = NULL;
        }

        int get_tid(){
            return tid;
        }

        void add_event(string event) {
            if(event_head == NULL){
                event_head = (Events*) malloc (sizeof(Events));
                if(event_head == NULL) {
                    cout << "Error to create a first event of tid: " + tid << endl;
                    exit(0);
                }
                event_head -> event = event;
                event_head -> next = NULL;
                event_tail = event_head;
            } else {
                event_tail -> next = (Events*) malloc (sizeof(Events));
                if(event_tail -> next == NULL) {
                    cout << "Error to create an event of tid: " + tid << endl;
                    exit(0);
                }
                event_tail -> next -> event = event;
                event_tail -> next -> next = NULL;
                event_tail = event_tail -> next;
            }
        }

        void print_all_events(){
            int i = 0;
            while (event_tail -> next != NULL){
                cout << "Message " << i << ": " << event_tail -> event << endl; 
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

        void print_all_tids(){
            cout << "As threads referentes ao processo " << pid << "são: " << endl;

            for(Tid tid : tids){
                cout << tid.get_tid() << endl;
            }
        }
};

void managePids(string);
vector<Pid> PidsList(string);
bool PidDirectories(vector<Pid>);

int main (){
    managePids("logs.txt");
}

void managePids(string logFile){
    vector<Pid> pids = PidsList(logFile);
    if(PidDirectories(pids)){
        cout << "Directories create with sucess!" << endl;
    } else {
        cout << "Error: can not create pid directories" << endl;
        exit(0);
    }

}

vector<Pid> PidsList(string logFile){
    string str = "awk '{print $3}' logs.txt | sort -u > pids.txt";
    const char *command = str.c_str();

    //When system() return 0, everything goes well
    if(system(command)){        
        cout << "Error can not create a File with Pids list" << endl;
        exit(0);
    } else {
        ifstream file;
        string line;
        vector<Pid> pids;
        file.open("pids.txt");

        if(file.is_open()){        
            while(getline(file, line)){
                if(stoi(line)){
                    pids.push_back(Pid(stoi(line)));
                } else {
                    cout << "Error: invalid format of some pids in a file: pids.txt" << endl;
                    exit(0);
                }    
            }
            file.close();
            return pids;
        } else {
            cout << "Error: can not acess the pids file: pids.txt" << endl;
            exit(0);
        }
    }
}

bool PidDirectories(vector<Pid> pids){
    string str = "mkdir Pids";
    const char *command = str.c_str();

    if(system(command)){        
        cout << "Error: can not create a pids root directory" << endl;
        exit(0);
    } else {
        for(Pid pid : pids){
            str = "mkdir ./Pids/" + to_string(pid.get_pid());
            command = str.c_str();
            if(system(command)){        
                cout << "Error: can not create a pid directory: "<< pid.get_pid() << endl;
                exit(0);
            }
        }
    }
    return true;
}