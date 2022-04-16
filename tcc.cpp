#include "tcc.h"
#ifdef TCC_H

int main (int argc, char *argv[]){
    string dir = "";

    switch (stoi(argv[2])){
        case 1:
            dir = dir + argv[3] + "/";
            dir = CheckPath(dir);
            break;
        
        case 2:
            dir = dir + argv[3] + "/";
            dir = CheckPath(dir);
            break;
    }
}

/**
 * CheckPath
 * 
 * Check a path, if not exist, it is created
 * @param  {string} dir: path
 * @return {string} dir: path
 */
string CheckPath(string dir){
    if(isDirectoryExist(dir)){
        cout << "\npath " << dir << " already exists" << endl;
    } else {
        string str = "mkdir " + dir;
        const char *command = str.c_str();
        
        if(system(command)){        
            cout << "\nprogram error: Can not create a path: " << dir << endl;
            exit(0);
        } else {
            cout << "\n" << "path " << dir << "was created" << endl;
        }
    }
    return dir;
}

/**
 * CheckDirectory
 * 
 * Check if the directory exist, and return 
 * true or false
 * @param  {string} str: path of directory
 * @return {bool} true or false
 */
bool CheckDirectory(const string &str){
  struct stat buffer;
  return (stat (str.c_str(), &buffer) == 0);
}

/**
 * FileOrganization
 * 
 * Create the entire file organization for
 * pids, tids and functions of a log file 
 * @param  {string} logs: file with logs
 * @return {bool} if everything goes well
 */
bool FileOrganization(string logs){
    vector<Pid> pids = allPids(logs);
    if(PidsTidsDirectories(pids, logs)){
        cout << "Directories create with sucess!" << endl;
    } else {
        cout << "Error: can not create pid directories" << endl;
        exit(0);
    }
    
    //?TidFunctions(pids);
}

/**
 * allPids
 * 
 * Extract all pids of logs 
 * @param  {string} logs: path of logs
 * @return {vector<Pid>} pids: a vector 
 * with all pids
 */
vector<Pid> allPids(string logs){
    string pid_path 
    string str = "awk '{print $3\" \"$4}'" + logs + "| sort -n -k 1 -u > pids.txt";
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
                pid_tid = split_number(line, ' ');
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

vector<int> split_number(string str, char delimiter) { 
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
            for(string function : functions){
                tid.add_function(function);
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
        vector<string> functions = read_functions(dir, tid_id);
        return functions;
    }
}

vector<string> read_functions(string dir, string tid_id){
    ifstream file;
    string function, function_aux, str;
    const char *command;
    vector<string> functions, vec_name;
    file.open(dir+"functions.txt");

    if(file.is_open()){        
        while(getline(file, function)){
            if (function.find('/') != string::npos){
                vec_name = split_character(function, '/');
                function_aux = "";
                for(string name : vec_name){
                    function_aux = function_aux + "_" + name;
                }
            } else if (!regex_match(function,regex("^[a-zA-Z0-9_.-]*$"))) {
                function_aux = function;
                function_aux = regex_replace(function_aux, regex("[^0-9a-zA-Z]+"), "");
            } else {
                function_aux = function;
            }
            str = "mkdir " + dir + function_aux;
            command = str.c_str();
            if(system(command)){         
                cout << "Error: can not create a function subdirectory: "<< dir << function << endl;
                exit(0);
            } else {
                str = "grep " + function + " " + dir + tid_id + ".txt > " + dir + function_aux + "/" + function_aux + ".txt";
                cout << str << endl;
                command = str.c_str();

                if(system(command)){         
                cout << "Error: can not create a function file: "<< dir << function_aux << function_aux << ".txt" << endl;
                exit(0);
                }
            }
            functions.push_back(function);
        }
        file.close();
        return functions;
    } else {
        cout << "Error to acess the functions data base of: " << dir <<"functions.txt" << endl;
        exit(0);
    }
}

vector<string> split_character (string str, char delimiter) { 
  vector<string> value; 
  stringstream ss(str); 
  string character; 
  while(getline(ss, character, delimiter)) { 
    value.push_back(character); 
  } 
  return value; 
}

/**
 * GetStdoutFromCommand
 * 
 * Capture the output of a linux command
 * Implementation for:
 * https://www.jeremymorgan.com/tutorials/c-programming/how-to-capture-the-output-of-a-linux-command-in-c/ 
 * 
 * @param  {string} cmd: linux command
 * @return {string} pids: output of linux command
 * with all pids
 */
string GetStdoutFromCommand(string data) {
  string data;
  FILE * stream;
  const int max_buffer = 256;
  char buffer[max_buffer];
  cmd.append(" 2>&1");

  stream = popen(cmd.c_str(), "r");

  if (stream) {
    while (!feof(stream))
      if (fgets(buffer, max_buffer, stream) != NULL) data.append(buffer);
    pclose(stream);
  }
  return data;
}


#else
cout << "Some problems were found to execute the program" << endl;
#endif