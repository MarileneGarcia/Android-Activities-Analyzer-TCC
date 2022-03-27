#include "tcc.h"

int main (){
    manageDirectories("logs.txt");
}

void manageDirectories(string logFile){
    vector<Pid> pids = PidsTidsList(logFile);
    if(PidsTidsDirectories(pids, logFile)){
        cout << "Directories create with sucess!" << endl;
    } else {
        cout << "Error: can not create pid directories" << endl;
        exit(0);
    }
    TidFunctions(pids);
}

vector<Pid> PidsTidsList(string logFile){
    string str = "awk '{print $3\" \"$4}' logs.txt | sort -u > pids.txt";
    const char *command = str.c_str();

    //When system() return 0, everything goes well
    if(system(command)){        
        cout << "Error can not create a File with Pids list" << endl;
        exit(0);
    } else {
        ifstream file;
        string line;
        vector<Pid> pids;
        vector<int> pid_tid;
        file.open("pids.txt");

        if(file.is_open()){        
            while(getline(file, line)){
                pid_tid = split(line, ' ');
                if(pid_tid[0]){
                    if(!pids.empty()){
                        if(pids.back().get_pid() != pid_tid[0]){
                            pids.push_back(Pid(pid_tid[0]));
                        }
                    } else{
                        pids.push_back(Pid(pid_tid[0]));
                    }
                pids.back().add_tid(pid_tid[1]);
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

bool PidsTidsDirectories(vector<Pid> pids, string log_file){
    string str = "mkdir Pids";
    string grep, pid_id, tid_id;
    const char *command = str.c_str();

    if(system(command)){        
        cout << "Error: can not create a pids root directory" << endl;
        exit(0);
    } else {
        for(Pid pid : pids){
            pid_id = to_string(pid.get_pid());
            str = "mkdir ./Pids/" + pid_id;
            command = str.c_str();
            if(system(command)){        
                cout << "Error: can not create a pid directory: "<< pid.get_pid() << endl;
                exit(0);
            } else {
                grep = "grep ' " + pid_id + " ' " + log_file + " > ./Pids/" + pid_id + "/" + pid_id + ".txt";
                command = grep.c_str();
                if(system(command)){        
                    cout << "Error: can not create a pid file: "<< pid.get_pid() << endl;
                    exit(0);
                }
            }

            for(Tid tid : pid.get_tids()){
                tid_id = to_string(tid.get_tid());
                str = "mkdir ./Pids/" + pid_id + "/" + tid_id;
                command = str.c_str();
                if(system(command)){         
                    cout << "Error: can not create a tid subdirectory: "<< tid.get_tid() << "of a pid directory: "<< pid.get_pid()  << endl;
                    exit(0);
                }
                else {
                    grep = "grep ' " + tid_id + " ' " + "./Pids/" + pid_id + "/" + pid_id + ".txt" + " > ./Pids/" + pid_id + "/" + tid_id + "/" + tid_id + ".txt";
                    command = grep.c_str();
                    if(system(command)){        
                        cout << "Error: can not create a pid file: "<< pid.get_pid() << endl;
                        exit(0);
                    }
                }
            }
        }
    }
    return true;
}

vector<int> split(string str, char delimiter) { 
  vector<int> value; 
  stringstream ss(str); 
  string number; 
 
  while(getline(ss, number, delimiter)) { 
    value.push_back(stoi(number)); 
  } 
 
  return value; 
}

bool TidFunctions(vector<Pid> pids){
    string str, dir, grep, pid_id, tid_id;
    const char *command;
    vector<string> functions;
    for(Pid pid : pids){
        pid_id = to_string(pid.get_pid());
        for(Tid tid : pid.get_tids()){
            tid_id = to_string(tid.get_tid());
            dir = "./Pids/" + pid_id + "/" + tid_id + "/";
            functions = pick_functions(dir, tid_id);
            for (string function : functions){
                str = "mkdir " + dir + function;
                command = str.c_str();
                if(system(command)){         
                    cout << "Error: can not create a function subdirectory: "<< dir << function << endl;
                    //exit(0);
                } else {
                    grep = "grep" + dir + function + "/" + function + ".txt";
                }
            }
        }
    }
}

vector<string> pick_functions(string dir, string tid_id){
    string str = "awk '{print (substr($6, length($6), 1) != \":\") ? $6 : substr($6, 1, length($6)-1) }' " + dir + tid_id + ".txt" + "| sort -u > " + dir + "functions.txt";
    const char *command = str.c_str();
    if(system(command)){         
        cout << "Error: can not select funcions of: "<< dir << tid_id << ".txt" << endl;
        exit(0);
    }
    else {
        vector<string> functions = read_functions(dir);
        return functions;
    }
}

vector<string> read_functions(string dir){
    ifstream file;
    string function;
    vector<string> functions;
    file.open(dir+"functions.txt");

    if(file.is_open()){        
        while(getline(file, function)){
            functions.push_back(function);
        }
        file.close();
        return functions;
    } else {
        cout << "Error to acess the functions data base of: " << dir <<"functions.txt" << endl;
        exit(0);
    }
}
