/* @file HelloKeypad.pde
|| @version 1.0
|| @author Alexander Brevig
|| @contact alexanderbrevig@gmail.com
||
|| @description
|| | Demonstrates the simplest use of the matrix Keypad library.
|| #
*/
#include <SPI.h>
#include <SD.h>
#include <Keypad.h>
#include <Ethernet.h>

#define FTPWRITE

// set up variables using the SD utility library functions:
Sd2Card card;
SdVolume volume;
SdFile root;

const int chipSelect = 4;

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {8, 7, 6, 5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {4, 3, 2}; //connect to the column pinouts of the keypad

String password = "1234#";
String input = "";
File myFile;

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

IPAddress server(192, 168, 1, 110);

void setup(){
  Serial.begin(9600);
  pinMode(9, OUTPUT);
  digitalWrite(9, HIGH);
  keypad.addEventListener(keypadEvent); //add an event listener for this keypad

 if (!SD.begin(4)) {
    Serial.println("initialization failed!");
    while (1);
  }

  myFile = SD.open("test.txt", FILE_WRITE);

  // if the file opened okay, write to it:
  if (myFile) {
    myFile.println("testing 1, 2, 3.");
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }

  // re-open the file for reading:
  myFile = SD.open("test.txt");
  if (myFile) {
    Serial.println("test.txt:");

    // read from the file until there's nothing else in it:
    while (myFile.available()) {
      Serial.write(myFile.read());
    }
    // close the file:
    myFile.close();
  } else {
    // if the file didn't open, print an error:
    Serial.println("error opening test.txt");
  }
}
  
void loop(){
  
}

void keypadEvent(KeypadEvent key){
  if (keypad.getState() == PRESSED){
    input += key;

    if (key == '#')
    {
        if (input == password)
        {
          digitalWrite(9, LOW);
          delay(5000);
          digitalWrite(9, HIGH);
        }

        input = "";
    }
  }
}
