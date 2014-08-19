CC := /usr/bin/gcc
CFLAGS := -Werror -O2
FLAGS_C99 := -Wall -pedantic -std=c99

all: nothing

nothing:
	@echo "Você não indicou um alvo."
	@echo "You did not specify a target."

clean:
	rm -f MatrixTest
	rm -f MatrixScroll

MatrixTest: MatrixTest.c
	$(CC) -o $@ $^ $(CFLAGS) $(FLAGS_C99) -lwiringPi

MatrixScroll: MatrixScroll.c
	$(CC) -o $@ $^ $(CFLAGS) $(FLAGS_C99) -lwiringPi

.PHONY: clean nothing
