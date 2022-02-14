#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <fstream>
#include <ctime>
#include <cstdlib>

using namespace std;
//vector<string> read_logs();
vector<string> pick_functions();
vector<string> read_functions();
vector<string> select_functions(vector<string> functions);

class logFunctions { 
    private:
        string name;
        map<int, string> events;
    public:           
        logFunctions(string function) {     
        name = function;
        }
};

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

vector<string> select_functions(vector<string> functions){
    cout << "Type 'y' to select a function for analyze, or type 'n' to unselect the function" << endl;
    for
}