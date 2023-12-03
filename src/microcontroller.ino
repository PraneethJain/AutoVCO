#include <EloquentTinyML.h>
#include <eloquent_tinyml/tensorflow.h>
#include <DHT.h>
#include "C:/Users/Faisal/Documents/neural.h"

#define N_INPUTS 3
#define N_OUTPUTS 1
#define TENSOR_ARENA_SIZE 4096

Eloquent::TinyML::TensorFlow::TensorFlow<N_INPUTS, N_OUTPUTS, TENSOR_ARENA_SIZE> tf;


int inputPin = 27;
#define DHTTYPE DHT11
#define dht_dpin 26
DHT dht(dht_dpin, DHTTYPE);
unsigned long startTime;
volatile unsigned long pulseCount = 0;

float adc_voltage = 0.0;
float in_voltage = 0.0;
int adc_value = 0;
float ref_voltage = 5.0;

void IRAM_ATTR onPulse() 
{
  pulseCount++;
}

float control_voltage = 1.97;
void setup() 
{
  pinMode(inputPin, INPUT);
  attachInterrupt(digitalPinToInterrupt(inputPin), onPulse, RISING);

  Serial.begin(9600);
  delay(4000);
  tf.begin(model_data);

  if (!tf.isOk()) {
    Serial.println(tf.getErrorMessage());
  }

  startTime = micros();
  dht.begin();
}

#define IN_PIN 32
float prev = 29.0;
void loop() 
{
  if (micros() - startTime >= 1000000) 
  {
    noInterrupts(); // Disable interrupts to read pulseCount safely
    float frequency = pulseCount / 1.0; // Calculate the frequency
    pulseCount = 0; // Reset the pulse count
    interrupts(); // Re-enable interrupts

    startTime = micros(); // Reset the timer
    float temperature = dht.readTemperature();
    if (std::isnan((temperature))) {
      temperature = prev;
    } else {
      prev = temperature;
    }
    // float temperature = 29;
    adc_value = analogRead(IN_PIN);
    adc_voltage = 1.1152 * (adc_value * ref_voltage) / 1024.0;
    Serial.print(temperature);
    Serial.print(" ");
    Serial.print(control_voltage);
    Serial.print(" ");
    Serial.println(adc_voltage);

    float input[3] = {temperature, control_voltage, adc_voltage};

    float y_pred = tf.predict(input);
    float y_true = frequency;
    Serial.print("Predicted: ");
    Serial.println(y_pred);
    Serial.print("Actual: ");
    Serial.println(y_true);
    float current_resistance = 10000;
    float percentage_error = ((y_pred - y_true)/y_true)*100;
    float new_resistance = current_resistance*(100 - percentage_error)/100;
    Serial.print("New Resistance: ");
    Serial.println(new_resistance);
    
    
    Serial.println();
  }
}
