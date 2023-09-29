#include <iostream>

// Having a single error can create multiple compiler errors so start with first error and see if that fixes everything

int main(){
    // error missing terminating character
    // second " missing
    std::cout<<"Hello world <<std::endl;
    return 0;
}

int main(){
    // error: expected ';' before '}' token
    std::cout<<"Hello world" <<std::endl
    return 0
}

int main(){
    // error: 'endll' is not a member of 'std';
    std::cout<<"Hello world" <<std::endll;
    return 0;
}

int main(){
    // error: return statement with no value in function returning int
    std::cout<<"Hello world" <<std::endl;
    return;
}

int main(){
    // error: invalid conversion from const char to int
    // tried returning string instead of an integer
    std::cout<<"Hello world" <<std::endl;
    return "Joe";
}

int main()
    // produced 3 errors when missing starting "{"
    std::cout<<"Hello world" <<std::endl;
    return 0;
}

int main(){
    // error: invalid operands - diviing string by an integer
    std::cout<<("Hello world" / 125) <<std::endll;
    return 0;
}
