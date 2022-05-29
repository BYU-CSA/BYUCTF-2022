#include <iostream>
#include <string>

void constructFlag(int val) {
	std::string flag = "";
	if (val == 289) {
		flag = "ctf";
		flag = "byu" + flag;
		flag = flag + "{";
		flag += "t3";
		flag += char(val - 236);
		flag += char(val - 173);
		flag += char(95);
		flag += "fl";
		flag += std::to_string(4);
		flag += "g";
		flag = flag + "_p";
		flag = flag + "l3453";
		flag = flag + "_";
		flag = flag + "ig";
		flag += "n0";
		flag += char(100+14);
		flag += "3";
		flag += "}";
		std::cout << "Finished processing flag!" << "\n";
	}
	else {
		std:: cout << "Wrong number!";
	}
}

int main() {
	int val = 0;
	std::cout << "Enter an integer: ";
	std::cin >> val;
	constructFlag(val);
	return 0;
}