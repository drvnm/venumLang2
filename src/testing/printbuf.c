#include <unistd.h>

void printSyscall(int number) {
    char buf[32];
    int index = 1;
    buf[sizeof(buf) - index] = '\n'; 
    do {
        buf[sizeof(buf) - index - 1] = '0' + number % 10;
        index++;
        number /= 10;
    } while (number > 0);
    write(1, &buf[sizeof(buf) - index ], index);
    

}

int main() {
    printSyscall(220);
    printSyscall(202);

}