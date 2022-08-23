
#include <ESP8266WiFi.h>

void setup() {
  WiFi.mode(WIFI_STA);
  
  Serial.begin(115200);
  Serial.println("Welcome to arduino");
  Serial.println(WiFi.macAddress());

}

void loop() {
  // put your main code here, to run repeatedly:

}
