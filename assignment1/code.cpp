#include <iostream>
#include <string>
using std::cout;
using std::cin;
using std::string;

void replace(string o, string & m){

	string one = "";
	string two = "";
	cin >> one >> two;

	for(int i = 0; i < o.length(); ++i){

		if(o[i] == one[0]){
			m[i] = two[0];
		}

	}
	cout << m;
}

int main(){
	string original = "SFGESUAXXVUASVOOHKASUEGEOHDXNRCOCORMSHKGEOPARSHGOLGXFGEOFSCUGRUUSKHWOHGSHXNCFRAAUOWOUGOCBCDPGXKCRPEDBXNCUOGESURUUSKHWOHGQRUPXUGOMXHGNOUMRDXHGEOOSKEGEWXHGERHMXHGEOGESCGSOGEMRDSHGEODORCGQXGEXNURHMRHMUSLGOOHRUDXNERZOMSUBXZOCOMFCXWBCRBVSHKGESURUUSKHWOHGSGQRUOHBCDPGOMNUSHKRUSWPAOWXHXRAPERJOGSBUNJUGSGNGSXHBSPEOCFXCGESURUUSKHWOHGUNJWSGGEOFXAAXQSHKSGOWUJDOWRSAQSGESHRWXHGEXFGEOCOAORUOMRGOXFGESURUUSKHWOHGFSCUGPCXZSMOGEOUNJUGSGNGSXHGRJAONUOMFXCGEOAOGGOCUPCOUOHGSHGEOPARSHGOLGUOBXHMMOUBCSJORHMSWPAOWOHGDXNCXQHBSPEOCUDUGOWFXCOHBCDPGSHKRHMMOBCDPGSHKGOLGFSAOUDXNWRDNUOUXWOXFGEOXGEOCUNJUGSGNGSXHBSPEOCUVHXQHSHGEOASGOCRGNCODXNWRDQXCVSHKCXNPUXFGQXRHMWRDNUORHDPCXKCRWWSHKARHKNRKOXFDXNCBEXSBO\n";
	string mod = original;
	cout << original;

	string input = "";

	cin >> input;
	bool done = false;
	while(!done){
		if(input == "r"){
			replace(original,mod);
		}
		if(input == "d"){
			done = true;
		}
		input = "";
		cin >> input;
	}

}


