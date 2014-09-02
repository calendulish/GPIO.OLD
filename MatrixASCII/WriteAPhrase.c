// Lara Maia <lara@craft.net.br> (C) 2014
// -*- -std=c99 -Wall -pedantic -lwiringPi -*-

#include "core.h"
#include "letters.h"
#include <stdio.h>
#include <ctype.h>

int main(int argc, char **argv)
{
    initialize();

    char line[256];
    char *character = line;

    for(;;)
    {
        if(STOP)
        {
            clean();
            exit(0);
        }

        printf("Digite uma frase: ");
        if (fgets(line, sizeof(line), stdin) != NULL)
        {
            for(int count = 0; count < strlen(character)-1; count++)
            {
                switch(tolower(character[count])) {
                    case 'a':
                        scroll(a, 3, 0);
                        break;
                    case 'b':
                        scroll(b, 3, 0);
                        break;
                    case 'c':
                        scroll(c, 4, 0);
                        break;
                    case 'd':
                        scroll(d, 3, 0);
                        break;
                    case 'e':
                        scroll(e, 3, 0);
                        break;
                    case 'f':
                        scroll(f, 4, 0);
                        break;
                    case 'g':
                        scroll(g, 4, 0);
                        break;
                    case 'h':
                        scroll(h, 4, 0);
                        break;
                    case 'i':
                        scroll(i, 9, -3);
                        break;
                    case 'j':
                        scroll(j, 4, 0);
                        break;
                    case 'k':
                        scroll(k, 4, 0);
                        break;
                    case 'l':
                        scroll(l, 5, 0);
                        break;
                    case 'm':
                        scroll(m, 3, 0);
                        break;
                    case 'n':
                        scroll(n, 3, 0);
                        break;
                    case 'o':
                        scroll(o, 3, 0);
                        break;
                    case 'p':
                        scroll(p, 4, 0);
                        break;
                    case 'q':
                        scroll(q, 3, 0);
                        break;
                    case 'r':
                        scroll(r, 3, 0);
                        break;
                    case 's':
                        scroll(s, 4, 0);
                        break;
                    case 't':
                        scroll(t, 5, 0);
                        break;
                    case 'u':
                        scroll(u, 4, 0);
                        break;
                    case 'v':
                        scroll(v, 5, 0);
                        break;
                    case 'w':
                        scroll(w, 4, 0);
                        break;
                    case 'x':
                        scroll(x, 4, 0);
                        break;
                    case 'y':
                        scroll(y, 5, 0);
                        break;
                    case 'z':
                        scroll(z, 3, 0);
                        break;
                }
            }
            }
    }
    exit(0);
}
