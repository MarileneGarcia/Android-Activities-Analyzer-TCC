#include "tcc.h"
#ifdef TCC_H

int main (int argc, char *argv[]){
    string str = "", str_dir = "";
    vector<Pid> pids = {};
    vector<int> choose_pids;
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
            str = "../config/pids/logs.txt";
            pids = FileOrganization(str);
            if (!pids.empty())
                CreateFileAllInformation(pids);
            else {
                cout << "program error: PANIC the program can not acess the log information" << endl;
                cout << "program exit" << endl;
                exit(0);
            }
            break;
        
        case 3:
            str = str + argv[2];
            if (!CreateActivityDirectory(str)){
                cout << "program error: activity already registered" << endl;
                cout << "program exit" << endl;
                exit(0);
            }
            break;

        case 4:
            str_dir = str_dir + argv[2];
            str = str + argv[3];
            if (!CreateOtherWayActivity(str_dir, str)){
                cout << "program error: the other way to same activity can not registered" << endl;
                cout << "program exit" << endl;
                exit(0);
            }
            break;
        
        case 5:
            str_dir = str_dir + argv[2];
            if(CompareFile(str_dir)){
                cout << "program sucess" << endl;
            } else {
                cout << "program fail" << endl;
            }
            break;
        
        case 6:
            str = str + argv[2];
            if(IsPathExist(str))
                cout << "yes";
            else
                cout << "no";
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
    string str = "rm -rf ../config/pids && rm -rf ../results";
    const char *command = str.c_str();
    if(system(command)){        
        cout << "program error: Can not remove old results and pid root directory" << endl;
        return false;
    } 

    str = "mkdir ../config/pids && mkdir ../results";
    command = str.c_str();
    if(system(command)){        
        cout << "program error: Can not create new results and pid root directory" << endl;
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
            cout << "program sucess: path " << dir << " was created" << endl;
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
vector<Pid> FileOrganization(string logs){
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
    return pids;
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
    vector<Pid> pids;
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
bool PidsTidsDirectories(vector<Pid>& pids, string log_file){
    string dir = "../config/pids/";
    string str, grep, pid_id, tid_id;
    const char *command;

    for(Pid& pid : pids){
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

        for(Tid& tid : pid.get_tids()){
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
bool TidFunctions(vector<Pid>& pids){
    string str, dir, grep, pid_id, tid_id;
    const char *command;
    vector<string> functions;
    for(Pid& pid : pids){
        pid_id = to_string(pid.get_pid());
        for(Tid& tid : pid.get_tids()){
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
    string str = "awk '{print (substr($6, length($6), 1) != \":\") ? $6 : substr($6, 1, length($6)-1) }' " + dir + tid_id + ".txt" + "| sort -u > " + dir + "info.txt";
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
    file.open(dir+"info.txt");

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
            apply_command(command);
            
            str = "grep " + function + " " + dir + tid_id + ".txt > " + dir + function_aux + "/" + function_aux + ".txt";
            command = str.c_str();
            apply_command(command);

            str = "tr -s \" \" < " + dir + function_aux + "/" + function_aux + ".txt | cut -d \" \" -f 5- > " + dir + function_aux + "/info.txt && rm -rf " + dir + function_aux + "/" + function_aux + ".txt";
            command = str.c_str();
            apply_command(command);
            
            functions.push_back(function);
        }
        file.close();
        return functions;
    } else {
        cout << "program error: can not acess the functions data base of: " << dir <<"info.txt" << endl;
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

/**
 * CreateFileAllInformation
 * 
 * Create a text file with all organizations
 * pid, tid and function. So, the interface can 
 * acess this and facilite the user choices pids
 * @param  {vector<Pid>} pid vector
 * @return {} 
 */
void CreateFileAllInformation(vector<Pid>& pids){
    int flag = 0;
    ofstream file("../config/pids/info_file.txt");
    ofstream file_aux("../config/pids/info_file_aux.txt");
    for(Pid pid : pids){
        file << ">" << pid.get_pid() << ": ";
        file_aux << ">" << pid.get_pid() << ": ";
        
        for(Tid tid: pid.get_tids()){
            file << "[" << tid.get_tid()<< ": ";
            file_aux << "[" << tid.get_tid()<< ": ";

            vector<string> it = tid.get_functions();
            vector<string>::iterator ptr;
            flag = 0;
            for(ptr = it.begin(); ptr < it.end(); ptr++){
                flag += 1;
                if(flag >= 2 && ptr != it.end()-1){
                    file << endl;
                    flag = 0;
                }
                if(ptr != it.end()-1){
                    file << *ptr << ",";
                    file_aux << *ptr << ",";
                } else {
                    file << *ptr << "]" << endl;
                    file_aux << *ptr << "]";
                }       
            }
        }
        file_aux << endl;
    }
    file.close();
}

/**
 * CreateActivityDirectory
 * 
 * Create a directory for the new activity 
 * if it does not exist
 * @param  {string} the path of new activity
 * @return {} 
 */
bool CreateActivityDirectory(string dir){
    if(!IsPathExist(dir)){
        string str = "mkdir " + dir;
        const char *command = str.c_str();
        apply_command(command);

        str = "mkdir " + dir + "/way_0";
        command = str.c_str();
        apply_command(command);
        
        return true;
    } else {
        return false;
    }
}

/**
 * CreateOtherWayActivity
 * 
 * Create a directory for other way to same
 * activity
 * @param  {string} the path of activity
 * @return {} 
 */
bool CreateOtherWayActivity(string dir, string pids){
    if(IsPathExist(dir)){
        string str = "ls -l " + dir + " | grep ^d | wc -l ";
        str = GetStdoutFromCommand(str);
        str.erase(remove(str.begin(), str.end(), '\n'), str.end());
        string way = "/way_" + str;

        str = "mkdir " + dir + way;
        const char *command = str.c_str();
        command = str.c_str();
        apply_command(command);

        dir = dir + way;
        if(RegisterActivity(pids, dir))
            return true;
        else 
            return false;
    } else {
        return false;
    }
}

/**
 * RegisterActivity
 * 
 * Register the new activity in repective
 * path
 * @param  {string} the process identificator that 
 * will be register
 * @param  {string} the directory in the activity was
 * register
 * @return {bool} true or false
 */
bool RegisterActivity(string pids_number, string dir){
    string str = "ls -l ../config/pids/ | grep ^d | rev | cut -d \" \" -f 1 | rev";
    vector<int> all_pids = split_number(GetStdoutFromCommand(str),'\n');
    vector<int> choose_pids = split_number(pids_number, ',');
    vector<int> tids;
    const char *command;
    sort(all_pids.begin(), all_pids.end());
    sort(choose_pids.begin(), choose_pids.end());

    dir = dir + "/";
    int i = 0,j = 0;
    while (i < all_pids.size()){
        if(j >= choose_pids.size() || all_pids[i] != choose_pids[j]){
            str = "rm -rf ../config/pids/" + to_string(all_pids[i]);
            command = str.c_str();
            apply_command(command);
            i++;
        } else {
            i++;
            j++;
        } 
    }

    str = "cp -a ../config/pids/. " + dir;
    command = str.c_str();
    apply_command(command);

    for(j = 0; j < choose_pids.size(); j++){
        str = "mv " + dir + to_string(choose_pids[j]) + " " + dir + "process_" + to_string(j);
        command = str.c_str();
        apply_command(command);

        str = "tr -s \" \" < " + dir + "/process_" + to_string(j) + "/" + to_string(choose_pids[j]) + ".txt | cut -d \" \" -f 5- > " 
        + dir + "/process_" + to_string(j) + "/log.txt && rm -f " + dir + "/process_" + to_string(j) + "/" + to_string(choose_pids[j]) + ".txt";
        command = str.c_str();
        apply_command(command);

        str = "ls -l " + dir + "/process_" + to_string(j) + "/" + " | grep ^d | rev | cut -d \" \" -f 1 | rev";
        tids = split_number(GetStdoutFromCommand(str),'\n');

        for(i = 0; i < tids.size(); i++){
            str = "mv " + dir + "process_" + to_string(j) + "/" + to_string(tids[i]) + " " + dir + "process_" + to_string(j) + "/thread_" + to_string(i);
            command = str.c_str();
            apply_command(command);

            str = "tr -s \" \" < " + dir + "/process_" + to_string(j) + "/" "thread_" + to_string(i) + "/" + to_string(tids[i]) + ".txt | cut -d \" \" -f 5- > " + dir + "/process_" 
            + to_string(j) + "/" "thread_" + to_string(i) + "/" + "log.txt && rm -f " + dir + "/process_" + to_string(j) + "/" "thread_" + to_string(i) + "/" + to_string(tids[i]) + ".txt";
            command = str.c_str();
            apply_command(command);
        }

        str = "tr -s \" \" < " + dir + "/process_" + to_string(j) + "/log.txt | cut -d \" \" -f 2 | tr \":\" \" \" | sort -u > "+ dir + "/process_" + to_string(j) + "/info.txt" ; 
        command = str.c_str();
        apply_command(command); 
    }

    str = "rm -f " + dir + "pids.txt";
    command = str.c_str();
    apply_command(command);

    if(FinishRegisterActivity(dir, choose_pids))
        return true;
    else
        return false;
}

/**
 * FinishRegisterActivity
 * 
 * To finish the activity register, the info_file.txt
 * and the logs.txt need to be in a right format because
 * the analise activitites will use this files
 * @param  {vector<int>} the process identificator that 
 * will be register
 * @param  {string} the directory in the activity was
 * register
 * @return {bool} true or false
 */
bool FinishRegisterActivity(string dir, vector<int> pids){
    string str;
    const char *command;

    for(int pid : pids){
        str = "tr -s \" \" < " + dir + "logs.txt | grep -E \"[0-9]{1} " + to_string(pid) + " [0-9]{1}\" >> " + dir + "log_aux.txt";
        command = str.c_str();
        apply_command(command);

        str = "tr -s \" \" < " + dir + "info_file_aux.txt | grep -E \">" + to_string(pid) + ":\" >> " + dir + "i_file.txt";
        command = str.c_str();
        apply_command(command);
    }

    str = "rm -rf " + dir + "logs.txt && rm -rf " + dir + "info_file.txt && rm -rf " + dir + "info_file_aux.txt";
    command = str.c_str();
    apply_command(command);

    str = "tr -s \" \" < " + dir + "log_aux.txt| cut -d \" \" -f 5- > " + dir + "log.txt && rm -rf " + dir + "log_aux.txt";
    command = str.c_str();
    apply_command(command);

    str = "sed -E 's/[0-9]+: / /g' " + dir + "i_file.txt | tr \">|[\" \" \" | tr -d \" |\n\" | tr \",|]\" \"\n\" | sort -u > " + dir + "info.txt && rm -rf " + dir + "i_file.txt";
    command = str.c_str();
    apply_command(command);

    return true;
}

/**
 * apply_command
 * 
 * Apply a command in bash
 * @param  {const char *} command
 * @return {}
 */
void apply_command(const char *command){
    if(system(command)){        
        cout << "program error: Can not apply the command: " << command << endl;
        cout << "program exit" << endl;
        exit(0);
    }
}

/**
 * CompareFile
 * 
 * Compare the target file with all the other activities 
 * already registered in the directory
 * @param  {string} directory of activities
 * @return {bool} true or false
 */
bool CompareFile(string dir){
    vector<string> activities;
    vector<string> ways;
    vector<string> info_filter;
    string info;
    double percentage_zip, percentagem_lines;
    string str = "../results/results.txt";
    ofstream file(str);
    int flag = 0;

    file << "The directory:\n" + dir + "\n\n";

    str = "tr -s \" \" < " + dir + "target/target.txt | cut -d \" \" -f 5- > " + dir + "target/log.txt";
    const char *command = str.c_str();
    apply_command(command);

    str = GetStdoutFromCommand("ls -l " + dir + "| grep ^d | tr -s \" \" | cut -d \" \" -f 9");
    activities = split_character(str,'\n');

    if(activities.size() == 1 && activities[0] == "target"){
        cout << "program error: There is no activity regitered in: " << dir << endl;
        cout << "program exit" << endl;
        exit(0);
    } else if (activities.size() == 1) {
        cout << "program error: Something goes wrong" << endl;
        cout << "program exit" << endl;
        exit(0);
    } else {
        for (string activity : activities){
            if(activity != "target"){
                str = GetStdoutFromCommand("ls -l " + dir + activity + "/ | grep ^d | tr -s \" \" | cut -d \" \" -f 9");
                ways = split_character(str,'\n');

                for (string way : ways){
                    info = GetStdoutFromCommand("cat " + dir + activity + "/" + way + "/info.txt");
                    info_filter = split_character(info,'\n');
                    str = "> " + dir + activity + "/" + way + "/log_target.txt";
                    const char *command = str.c_str();
                    apply_command(command);

                    for(string info_aux : info_filter){
                        /* could be a log priority filter here */
                        str = "grep -E \"[S,F,A,E,W,I,D,V] +" + info_aux + " *:\" "+ dir + "target/log.txt >> " + dir + activity + "/" + way + "/log_target.txt";
                        const char *command = str.c_str();
                        system(command);
                    }

                    str = dir + activity + "/" + way + "/";
                    percentage_zip = AnalizeZipSize(str);
                    percentagem_lines = AnalizeCommands(str);
                    /* The accuracy of algorithm can be change here */
                    if (percentage_zip >= 50.0 && percentagem_lines >= 50.0){
                        flag += 1;
                        file << "***************************************\n";
                        file << activity << ": "<< way << ": is a possible match\n";
                        file << percentage_zip << "% of zip percentage\n";
                        file << percentagem_lines << "% of lines percentage\n\n";
                        
                        str = "mkdir -p ../results/" + activity + "/" + way;
                        command = str.c_str();
                        apply_command(command);

                        str = "mv " + dir + activity + "/" + way + "/us_log_t.txt  ../results/" + activity + "/" + way + "/unique_umatch_lines.txt";
                        command = str.c_str();
                        apply_command(command);

                        str = "mv " + dir + activity + "/" + way + "/nh_us_log_t.txt  ../results/" + activity + "/" + way + "/unique_umatch_lines_no_hex.txt";
                        command = str.c_str();
                        apply_command(command);

                        str = "mv " + dir + activity + "/" + way + "/nn_us_log_t.txt  ../results/" + activity + "/" + way + "/unique_umatch_lines_no_numbers.txt";
                        command = str.c_str();
                        apply_command(command);

                        str = "rm -rf " + dir + activity + "/" + way + "/us_log_t.txt && rm -rf " + dir + activity + "/" + way + "/nh_us_log_t.txt && rm -rf " + dir + activity + "/" + way + "/nn_us_log_t.txt && rm -rf " + dir + activity + "/" + way + "/log_target.txt";
                        command = str.c_str();
                        apply_command(command);

                    }
                }
            }
        }
        str = "rm -f " + dir + "target/target.txt && rm -f " + dir + "target/log.txt";
        const char *command = str.c_str();
        apply_command(command);
    }
    if(flag == 0){
        return false;
    } else {
        return true;
    }
}

/**
 * AnalizeZipSize
 * 
 * Compare the target file with the activity 
 * using the size of zip
 * @param  {string} directory of the activity
 * @return {double} percentage of match
 */
double AnalizeZipSize(string dir){
    string str = "zip " + dir + "log.zip " + dir + "log.txt && zip " + dir + "log_target.zip " + dir + "log_target.txt";
    const char *command = str.c_str();
    apply_command(command);

    double size_log, size_log_target, percentage;
    string str_aux;

    str = "ls -l " + dir + "log.zip | tr -s \" \" | cut -d \" \" -f 5 | tr -d \"\n\"";
    str_aux = GetStdoutFromCommand(str);
    size_log = stod(str_aux);

    str = "ls -l " + dir + "log_target.zip | tr -s \" \" | cut -d \" \" -f 5 | tr -d \"\n\"";
    str_aux = GetStdoutFromCommand(str);
    size_log_target = stod(str_aux);

    if(size_log_target >= size_log){
        percentage = (1 - ((size_log_target - size_log)/size_log_target))*100;
    } else {
        percentage = (1 - ((size_log - size_log_target)/size_log))*100;
    }

    str = "rm -rf " + dir + "log.zip && rm -rf " + dir + "log_target.zip";
    command = str.c_str();
    apply_command(command);
    
    cout << "Percentage for zip size is: " << to_string(percentage) << "%\n";
    return percentage;
}

/**
 * AnalizeCommands
 * 
 * Compare the target file with the activity 
 * using unmatch lines
 * @param  {string} directory of the activity
 * @return {double} percentage of match
 */
double AnalizeCommands(string dir){
    /* sort files */
    string str_aux;
    vector<string> match_lines;
    string str = "sort -u " + dir + "log.txt | tr -s \" \" > " + dir + "s_log.txt && sort -u " + dir + "log_target.txt | tr -s \" \" > " + dir + "s_log_t.txt";
    const char *command = str.c_str();
    apply_command(command);

    /* compare using comm */
    /* us_log_t is the answer */
    str = "comm -23 " + dir + "s_log_t.txt " + dir + "s_log.txt > " + dir + "us_log_t.txt";
    command = str.c_str();
    apply_command(command);

    /* compare using grep and remove all the hex number */
    str = "sed -E \"s/[^0-9]0x[a-fA-F0-9]+/(HEX_VALUE)/g\" " + dir + "s_log.txt | tr -s \" \" > " + dir + "nh_s_log.txt && sed -E \"s/[^0-9]0x[a-fA-F0-9]+/(HEX_VALUE)/g\" " + dir + "s_log_t.txt | tr -s \" \" > " + dir + "nh_s_log_t.txt";
    command = str.c_str();
    apply_command(command);
    str_aux = GetStdoutFromCommand("grep -Fxvnf " + dir + "nh_s_log.txt " + dir + "nh_s_log_t.txt | cut -d \":\" -f 1");
    match_lines = split_character(str_aux,'\n');
    str_aux = "";
    for (string line : match_lines){
        str_aux = str_aux + line + "p; ";
    }
    str = "sed -n \"" + str_aux + "\" < " + dir + "s_log_t.txt > " + dir + "nh_us_log_t.txt";
    command = str.c_str();
    apply_command(command);

    /* compare using grep and remove all numbers */
    str = "tr -d [0-9] < " + dir + "nh_s_log.txt | tr -s \" \" > " + dir + "nn_s_log.txt && tr -d [0-9] < " + dir + "nh_s_log_t.txt | tr -s \" \" > " + dir + "nn_s_log_t.txt";
    command = str.c_str();
    apply_command(command);
    str_aux = GetStdoutFromCommand("grep -Fxvnf " + dir + "nn_s_log.txt " + dir + "nn_s_log_t.txt | cut -d \":\" -f 1");
    match_lines = split_character(str_aux,'\n');
    str_aux = "";

    double number_lines = 0, number_total = 0, percentage = 0;

    for (string line : match_lines){
        str_aux = str_aux + line + "p; ";
        number_lines += 1;
    }
    str = "sed -n \"" + str_aux + "\" < " + dir + "s_log_t.txt > " + dir + "nn_us_log_t.txt";
    command = str.c_str();
    apply_command(command);

    str = GetStdoutFromCommand("wc -l < " + dir +"s_log_t.txt");
    number_total = stod(str);

    percentage = ( (number_total - number_lines)/number_total ) * 100;
    cout << "Percentage for match lines is: " << to_string(percentage) << "%\n";

    str = "rm -rf " + dir + "s_log.txt " + dir + "s_log_t.txt " + dir + "nh_s_log.txt " + dir + "nh_s_log_t.txt " + dir + "nn_s_log.txt " + dir + "nn_s_log_t.txt ";
    command = str.c_str();
    apply_command(command);

    return percentage;
}

#else
cout << "Some problems were found to execute the program" << endl;
#endif