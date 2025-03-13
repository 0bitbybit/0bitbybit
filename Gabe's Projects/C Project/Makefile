cc := gcc
CFLAGS := -Wall -Wextra -Werror

all: my_mastermind

my_mastermind: main.o
	$(cc) $(CFLAGS) main.o -o my_mastermind

main.o: main.c
	$(cc) $(CFLAGS) -c main.c -o main.o

clean:
	rm -f *.o

fclean: clean
	rm -f my_mastermind

re: fclean all

.PHONY: all clean fclean re
