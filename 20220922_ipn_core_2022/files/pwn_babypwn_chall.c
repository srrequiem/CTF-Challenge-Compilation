#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define FLAG1 "--FAKE-FLAG-1--"
#define FLAG2 "--FAKE-FLAG-2--"

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void vuln(){
    char cmd[0x10];
    cmd[0] = 'e';
    cmd[1] = 'c';
    cmd[2] = 'h';
    cmd[3] = 'o';
    cmd[4] = ' ';
    cmd[5] = 'T';
    cmd[6] = 'O';
    cmd[7] = 'D';
    cmd[8] = 'O';
    cmd[9] = '\0';

    int canary = 0x23415673;

    char buf[0x100];

    printf("Ingresa tu nombre : ");
    int tam = scanf("%s", buf);

    if(tam > 0x100){
        printf("cadena demasiado grande. Vuelve a intentarlo\n");
        exit(0);
    }

    printf("Hola %s, lo lamento pero esta funcion no esta lista. :(\n", buf);

    if(canary != 0x23415673){
        printf("%s\n", FLAG1);
        printf("Buen intento hacker. Mas Suerte para la proxima\n");
        printf("Descubri que mi canary ahora es : 0x%08x\n", canary);
        exit(0);
    }

    if(strlen(buf) > 0x100){
        printf("Bien hecho!\n");
        printf("%s\n", FLAG2);
    }

    system(cmd);
    exit(0);
}

int main(){
    init();
    vuln();
    return 0;
}
