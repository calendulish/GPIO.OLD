// Lara Maia <lara@craft.net.br> (C) 2014
// -*- -std=c99 -Wall -pedantic -lwiringPi -*-

#include <wiringPi.h>
#include <stdlib.h>
#include <signal.h>

// for match with my extension board
#define ce1 11
#define ce0 10
#define sclk 14
#define miso 13
#define mosi 12
#define rxd 16
#define txd 15
#define scl 9
#define sda 8

int rows[8] = { 0, 5, scl, 3, ce1, txd, ce0, mosi };
int columns[8] = { 4, sclk, miso, 1, rxd, 2, 6, 7 };
int STOP;

void signal_handler(int sig)
{
    STOP = 1;
}

void clean()
{
    for(int i = 0; i < 8; i++)
    {
        pinMode(rows[i], INPUT);
        pinMode(columns[i], INPUT);
    }
}

void led(int column, int row, int status)
{
    if(STOP)
    {
        clean();
        exit(0);
    }

    for(int col = 0; col < 8; col++)
        if(col != column)
            digitalWrite(columns[col], status);

    digitalWrite(rows[row], status);
}

void draw(int column, int row)
{
    led(column, row, HIGH);
    delay(1);
    led(column, row, LOW);
}


int main(int argc, char **argv)
{
    wiringPiSetup();

    signal(SIGINT, signal_handler);

    for(int i = 0; i < 8; i++)
    {
        pinMode(rows[i], OUTPUT);
        pinMode(columns[i], OUTPUT);
    }

    for(;;)
    {
        draw(2, 0);
        draw(1, 1);
        draw(0, 2);
        draw(0, 3);
        draw(1, 4);
        draw(2, 5);
        draw(3, 6);
        draw(4, 5);
        draw(5, 4);
        draw(6, 3);
        draw(6, 2);
        draw(5, 1);
        draw(4, 0);
        draw(3, 1);
    }

    exit(0);
}
