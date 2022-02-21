#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>

using namespace std;

typedef struct Events{
    string event;   
    Events* next; 
} Events;

class logFunctions { 
    private:
        string name;
        Events* event_head;
        Events* event_tail; 
        
        /* thinking about pid and tid later
        //int pid; 
        //int tid; */

    public:           
        logFunctions(string function) {     
        name = function;
        event_head = NULL;
        event_tail = NULL;
        }

        string get_name(){
            return name;
        }

        void add_evento(string event) {
            if(event_head == NULL){
                event_head = (Events*) malloc (sizeof(Events));
                if(event_head == NULL) {
                    cout << "Error to create a first event of Function: " + name << endl;
                    exit(0);
                }
                event_head -> event = event;
                event_head -> next = NULL;
                event_tail = event_head;
            } else {
                event_tail -> next = (Events*) malloc (sizeof(Events));
                if(event_tail -> next == NULL) {
                    cout << "Error to create an event of Function: " + name << endl;
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

//vector<string> read_logs();
vector<string> pick_functions();
vector<string> read_functions();
vector<logFunctions> select_functions(vector<string> functions);

int main (){
    //vector<string> lines = read_logs();
    vector<string> functions = pick_functions();
    select_functions(functions);
    return 0;
}

vector<string> read_logs(){
    ifstream file;
    string line;
    vector<string> lines;
    file.open("logs.txt");

    if(file.is_open()){        
        while(getline(file, line)){
            lines.push_back(line);
        }
        file.close();
        return lines;
    } else {
        cout << "Error to acess the logs data base" << endl;
        exit(0);
    }
}

vector<string> pick_functions(){
    string str = "awk '{print (substr($6, length($6), 1) != \":\") ? $6 : substr($6, 1, length($6)-1) }' logs.txt | sort -u >> cellphone_functions.txt";
    const char *command = str.c_str();
    system(command);
    vector<string> functions = read_functions();
    return functions;
}

vector<string> read_functions(){
    ifstream file;
    string function;
    vector<string> functions;
    file.open("cellphone_functions.txt");

    if(file.is_open()){        
        while(getline(file, function)){
            functions.push_back(function);
        }
        file.close();
        return functions;
    } else {
        cout << "Error to acess the functions data base" << endl;
        exit(0);
    }
}

vector<logFunctions> select_functions(vector<string> functions){
    vector<logFunctions> events;
    string selection;
    int i = 0;
    cout << "Type 'y' to select a function for analyze, or type 'n' to unselect the function" << endl;
    for (string function : functions){
        cout << "Do you want to analyse: \033[1;31m" + function + "\033[0m ?";
        cin >> selection;

        if(selection == "y"){
            cout << "Do you wanna select" + function << endl;
            events.push_back(logFunctions(function));
            cout << events[i].get_name() << endl;
            i++;
        }
    }
    return events;
}