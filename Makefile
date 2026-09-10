CC=gcc
CFLAGS=-Wall

all: process_manager

process_manager: main.c
	$(CC) $(CFLAGS) -o process_manager main.c

clean:
	rm -f process_manager