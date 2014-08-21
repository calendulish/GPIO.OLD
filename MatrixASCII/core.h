// Lara Maia <lara@craft.net.br> (C) 2014

#include <wiringPi.h>
#include <stdlib.h>
#include <stdio.h>
#include <signal.h>
#include <string.h>

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

void drawImage(char image[], int p)
{
    for(int x = 0; x < 8; x++)
        for(int y = 0; y < 8; y++)
            if(image[x+8*y] == '#')
                draw(x+p, y);
}

void scroll(char image[], int decrease, int distance)
{
    for(int iter = 0; iter < 16+distance; iter++)
    {
        int i=8-iter;
        for(int l = 0; l < decrease; l++)
        {
            drawImage(image, i);
            delay(1);
        }
    }
}

void initialize()
{
    wiringPiSetup();

    signal(SIGINT, signal_handler);

    for(int i = 0; i < 8; i++)
    {
        pinMode(rows[i], OUTPUT);
        pinMode(columns[i], OUTPUT);
    }
}
