// Exemplo mínimo — substitua pelo seu firmware
#include <Arduino.h>

void setup() {
  Serial.begin(115200);
  delay(1000);
  Serial.println("Firmware inicializado");
}

void loop() {
  // TODO: leitura de sensores, envio de dados, etc.
  delay(1000);
}
