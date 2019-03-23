  1 #include <stdio.h>
  2 #include <stdlib.h>

  3 int main(int argc, char *argv[])
  4 {
  5     int i;
  6     for(i=1; i<argc; i++)
  7     {
  8         printf("%s%s", argv[i], (i<argc-1) ? " ":"");
  9         if(argv[i][0] == '-')
 10                 printf(" : squared value is %d",(atoi(argv[i]+1))*(atoi(argv[i]+1)));
 11     }
 12     printf("\n");
 13     return 0;
 14 }