#include "tcc.h"
#ifdef TCC_H

int main (int argc, char *argv[]){
    string str = "";
    switch (stoi(argv[1])){
        case 0:
            if(!ProgramBegin()){
                cout << "program error: PANIC the program can not begin" << endl;
                cout << "program exit" << endl;
                exit(0);
            }
            break;

        case 1:
            str = str + argv[2];
            CheckPath(str);
            break;
        
        case 2:
            str = "../config/logs.txt";
            FileOrganization(str);
            break;
    }
}

/**
 * ProgramBegin
 * 
 * The begining of a program, a file "logs_exe.txt"
 * will be create with all code execution of the program
 * running for a one action, and remove a auxiliar folder
 * ../config/pids, for after create again
 * @param  {} 
 * @return {bool} true or false
 */
bool ProgramBegin(){
    string str = "rm -rf ../config/pids";
    const char *command = str.c_str();
    if(system(command)){        
        cout << "program error: Can not remove a old pid root directory" << endl;
        return false;
    } 

    str = "mkdir ../config/pids";
    command = str.c_str();
    if(system(command)){        
        cout << "program error: Can not create a new pid root directory" << endl;
        return false;
    }

    str = "echo \"program sucess: begining..\"  > ../config/logs_exe.txt";
    command = str.c_str();
    if(system(command)){        
        cout << "program error: Can not initialize " << endl;
        return false;
    } else {
        cout << "program sucess: beginning completed" << endl;
        return true;
    }
}

/**
 * WriteFile
 * 
 * write in a file
 * @param  {string} file: path of the file 
 * @param  {string} message: the message to be write 
 * @return {bool} true or false
 */
bool WriteFile(string file, string message){
        ofstream myfile;
        myfile.open (file);
    if (myfile.is_open()){
        myfile << message << endl;
        myfile.close();
        return true;
    } else {
        return false;
    }
}

/**
 * CheckPath
 * 
 * Check a path, if not exist, it is created
 * @param  {string} dir: path
 * @return {} 
 */
void CheckPath(string str){
    string dir = "../config/activities/" + str;
    if(IsPathExist(dir)){
        cout << "program sucess: path " << dir << " already exists" << endl;
    } else {
        string str = "mkdir " + dir;
        const char *command = str.c_str();
        
        if(system(command)){        
            cout << "program error: Can not create a path: " << dir << endl;
            cout << "program exit" << endl;
            exit(0);
        } else {
            cout << "program sucess: path " << dir << "was created" << endl;
        }
    }
}

/**
 * CheckDirectory
 * 
 * Check if the directory exist, and return 
 * true or false
 * Implementation for:
 * https://www.systutorials.com/how-to-test-a-file-or-directory-exists-in-c/
 * 
 * @param  {string} str: path of directory
 * @return {bool} true or false
 */
bool IsPathExist(const string &str){
  struct stat buffer;
  return (stat (str.c_str(), &buffer) == 0);
}

/**
 * FileOrganization
 * 
 * Create the entire file organization for
 * pids, tids and functions of a log file 
 * @param  {string} logs: psth of log file
 * @return {}
 */
void FileOrganization(string logs){
    vector<Pid> pids = allPids(logs);
    if(PidsTidsDirectories(pids, logs)){
        cout << "program sucess: pids and tid directories created with sucess" << endl;
    } else {
        cout << "program error: can not create pids directories" << endl;
        cout << "program exit" << endl;
        exit(0);
    }
    if(TidFunctions(pids)){
        cout << "program sucess: all function directories created with sucess" << endl;
    } else {
        cout << "program error: can not create function directories" << endl;
        cout << "program exit" << endl;
        exit(0);
    }
}

/**
 * allPids
 * 
 * Extract all pids of logs, salve in a text file.
 * Create a class for each pid, and the tid vector 
 * with the all tids class that refer to this pid
 * @param  {string} logs: path of logs
 * @return {vector<Pid>} pids: a vector 
 * with all pids
 */
vector<Pid> allPids(string logs){
    string pid_path = "../config/pids/pids.txt";
    string str = "awk '{print $3\" \"$4}' " + logs + " | sort -u | sort -n -k 1 > " + pid_path;
    const char *command = str.c_str();

    //When system() return 0, everything goes well
    if(system(command)){        
        cout << "program error: can not create a file with pids list" << endl;
        exit(0);
    } else {
        ifstream file;
        string line;
        vector<Pid> pids;
        vector<int> pid_tid;
        file.open(pid_path);

        if(file.is_open()){        
            while(getline(file, line)){
                pid_tid = split_number(line, ' ');
                if(pid_tid[0]){
                    if(!pids.empty()){
                        if(pids.back().get_pid() != pid_tid[0]){
                            pids.push_back(Pid(pid_tid[0]));
                        }
                    } else {
                        pids.push_back(Pid(pid_tid[0]));
                    }
                pids.back().add_tid(pid_tid[1]);
                } else {
                    cout << "program error: invalid format of some pids in a file: pids.txt" << endl;
                    cout << "program exit" << endl;
                    exit(0);
                }    
            }
            file.close();
            return pids;
        } else {
            cout << "program error: can not acess the pids file: pids.txt" << endl;
            cout << "program exit" << endl;
            exit(0);
        }
    }
}


/**
 * split_number
 * 
 * Convert string pids in integer pids
 * @param  {string} str: string pids
 * @param  {char} delimiter: delimeter between pids
 * @return {vector<int>} value: numerical pids 
 */
vector<int> split_number(string str, char delimiter) { 
  vector<int> value; 
  stringstream ss(str); 
  string number; 
  while(getline(ss, number, delimiter)) { 
    value.push_back(stoi(number)); 
  } 
  return value; 
}

/**
 * PidsTidsDirectories
 * 
 * Create all organization of the pids
 * and tids
 * @param  {pids} vector of pids
 * @param  {string} log_file: path of logs
 * @return {bool} true or false  
 */
bool PidsTidsDirectories(vector<Pid> pids, string log_file){
    string dir = "../config/pids/";
    string str, grep, pid_id, tid_id;
    const char *command;

    for(Pid pid : pids){
        pid_id = to_string(pid.get_pid());
        str = "mkdir " + dir + pid_id;
        command = str.c_str();
        if(system(command)){        
            cout << "program error: can not create a pid directory: "<< pid.get_pid() << endl;
            cout << "program exit" << endl;
            exit(0);
        } else {
            grep = "grep ' " + pid_id + " ' " + log_file + " > " + dir + pid_id + "/" + pid_id + ".txt";
            command = grep.c_str();
            if(system(command)){        
                cout << "program error: can not create a pid file: "<< pid.get_pid() << endl;
                cout << "program exit" << endl;
                exit(0);
            }
        }

        for(Tid tid : pid.get_tids()){
            tid_id = to_string(tid.get_tid());
            str = "mkdir " + dir + pid_id + "/" + tid_id;
            command = str.c_str();
            if(system(command)){         
                cout << "program error: can not create a tid subdirectory: "<< tid.get_tid() << "of a pid directory: "<< pid.get_pid()  << endl;
                cout << "program exit" << endl;
                exit(0);
            }
            else {
                grep = "grep ' " + tid_id + " ' " + dir + pid_id + "/" + pid_id + ".txt" + " > " + dir + pid_id + "/" + tid_id + "/" + tid_id + ".txt";
                command = grep.c_str();
                if(system(command)){        
                    cout << "program error: can not create a pid file: "<< pid.get_pid() << endl;
                    cout << "program exit" << endl;
                    exit(0);
                }
            }
        }
    }
    return true;
}

/**
 * TidFunctions
 * 
 * Salve all functions of each tid in 
 * the refer class
 * @param  {pids} vector of pids
 * @return {bool} true or false  
 */
bool TidFunctions(vector<Pid> pids){
    string str, dir, grep, pid_id, tid_id;
    const char *command;
    vector<string> functions;
    for(Pid pid : pids){
        pid_id = to_string(pid.get_pid());
        for(Tid tid : pid.get_tids()){
            tid_id = to_string(tid.get_tid());
            dir = "../config/pids/" + pid_id + "/" + tid_id + "/";
            functions = pick_functions(dir, tid_id);
            for(string function : functions){
                tid.add_function(function);
            }
        }
    }
    return true;
}

/**
 * pick_functions
 * 
 * Return all functios of each tid
 * @param  {dir} path of a tid directory
 * @param  {tid_id} tid id
 * @return {vector<string>} the funcions
 */
vector<string> pick_functions(string dir, string tid_id){
    string str = "awk '{print (substr($6, length($6), 1) != \":\") ? $6 : substr($6, 1, length($6)-1) }' " + dir + tid_id + ".txt" + "| sort -u > " + dir + "functions.txt";
    const char *command = str.c_str();
    if(system(command)){         
        cout << "program error: can not select funcions of: "<< dir << tid_id << ".txt" << endl;
        cout << "program exit" << endl;
        exit(0);
    }
    else {
        vector<string> functions = FunctionsDirectory(dir, tid_id);
        return functions;
    }
}

/**
 * FunctionsDirectory
 * 
 * Ensure the correct format of funcions, and create a 
 * directory for each function in the correct path and 
 * create a file with all log of each function
 * @param  {dir} path of a tid directory
 * @param  {tid_id} tid id
 * @return {vector<string>} the funcions
 */
vector<string> FunctionsDirectory(string dir, string tid_id){
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
                cout << "program error: can not create a function subdirectory: "<< dir << function << endl;
                cout << "program exit" << endl;
                exit(0);
            } else {
                str = "grep " + function + " " + dir + tid_id + ".txt > " + dir + function_aux + "/" + function_aux + ".txt";
                command = str.c_str();

                if(system(command)){ 
                cout << "program exit" << endl;        
                cout << "program error: can not create a function file: "<< dir << function_aux << function_aux << ".txt" << endl;
                exit(0);
                }
            }
            functions.push_back(function);
        }
        file.close();
        return functions;
    } else {
        cout << "program error: can not acess the functions data base of: " << dir <<"functions.txt" << endl;
        cout << "program exit" << endl;
        exit(0);
    }
}

/**
 * split_character
 * 
 * Split a string in unallowed characteres
 * @param  {string} str: string function
 * @param  {char} delimiter: delimeter unallowed characteres
 * @return {vector<int>} value: characteres betwwen the 
 * unallowed characteres 
 */
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
string GetStdoutFromCommand(string cmd) {
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

/**
 * printPids
 * 
 * Print all pids of a pid vector
 * @param  {vector<Pid>} pid vector
 * @return {} 
 */
void printPids(vector<Pid> pids){
    for(Pid aux : pids){
        cout << "para o pid :" << aux.get_pid() << endl;
        aux.print_all_tids();
        cout << endl; 
    }
}

#else
cout << "Some problems were found to execute the program" << endl;
#endif