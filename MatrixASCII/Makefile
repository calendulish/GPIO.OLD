CC = /usr/bin/gcc
CFLAGS = -Werror -Wno-error=unused-variable -O2
FLAGS_C99 = -Wall -pedantic -std=c99

all: WriteAPhrase

clean:
	rm -f WriteAPhrase

WriteAPhrase: WriteAPhrase.c
	$(CC) -o $@ $^ $(CFLAGS) $(FLAGS_C99) -lwiringPi

.PHONY: clean
