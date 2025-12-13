#include <Wire.h>
#include <Adafruit_TCS34725.h>
#include <WiFi.h>
#include <ThingSpeak.h>

// ---------- WiFi and ThingSpeak ----------
const char* ssid = "Galaxy A16 5G 2927";
const char* password = "ttpod123";
WiFiClient client;

unsigned long myChannelNumber = 3070629;
const char* myWriteAPIKey = "6B4U8UT18SXPTRL4";

// ---------- Sensor Pins ----------
const int pHpin = 34;        // ADC1 on ESP32
const int turbidityPin = 35; // ADC1 on ESP32
const int greenLED = 25;
const int yellowLED = 26;
const int redLED = 27;

// ---------- Calibration Constants ----------
// ✅ Calibrated pH constants (distilled water ≈ 7)
float phSlope = -1.76;
float phIntercept = 9.29;

// ✅ Turbidity calibration (distilled water ≈ 0 NTU)
float turbiditySlope = -648.88;
float turbidityIntercept = 610.95;  // recalibrated intercept for 0 NTU at ~0.94 V

// ---------- RGB Sensor ----------
Adafruit_TCS34725 tcs = Adafruit_TCS34725(
  TCS34725_INTEGRATIONTIME_154MS,
  TCS34725_GAIN_4X
);

// ---------- Function Prototypes ----------
float readPH();
float readTurbidity();
void readRGB(float &rNorm, float &gNorm, float &bNorm);
String classifyOil(float turbidityValue, float colorValue, int &oilStatusNo);
int classifyCode(String quality);

// ---------- Setup ----------
void setup() {
  Serial.begin(115200);
  delay(2000);
  Serial.println("\n🔧 Cooking Oil Purity Detection System");

  // LED setup
  pinMode(greenLED, OUTPUT);
  pinMode(yellowLED, OUTPUT);
  pinMode(redLED, OUTPUT);

  // Initialize TCS34725 color sensor
  if (tcs.begin()) {
    Serial.println("✅ RGB Sensor initialized.");
  } else {
    Serial.println("⚠️ RGB Sensor not found. Check wiring!");
  }

  // WiFi connection
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\n✅ WiFi connected!");
  Serial.print("📡 IP Address: ");
  Serial.println(WiFi.localIP());

  ThingSpeak.begin(client);
}

// ---------- Loop ----------
void loop() {
  float pH = readPH();
  float turbidity = readTurbidity();
  float rNorm = 0, gNorm = 0, bNorm = 0;
  readRGB(rNorm, gNorm, bNorm);
  float colorValue = (rNorm + gNorm + bNorm) / 3.0;

  int oilStatusNo = 0;
  String oilStatus = classifyOil(turbidity, colorValue, oilStatusNo);

  // Print readings
  Serial.println("==================================");
  Serial.printf("pH Value: %.2f\n", pH);
  Serial.printf("Turbidity: %.2f NTU (approx)\n", turbidity);
  Serial.printf("Color Avg: %.2f\n", colorValue);
  Serial.println("Oil Status: " + oilStatus);
  Serial.println("==================================");

  // Upload to ThingSpeak
  ThingSpeak.setField(1, (float)pH);
  ThingSpeak.setField(2, (float)turbidity);
  ThingSpeak.setField(3, (float)colorValue);
  ThingSpeak.setField(4, oilStatusNo);

  int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  if (x == 200) {
    Serial.println("✅ Data uploaded to ThingSpeak.");
  } else {
    Serial.println("⚠️ Upload failed, HTTP error: " + String(x));
  }

  delay(15000);  // ThingSpeak minimum update interval = 15s
}

// ---------- Functions ----------

// Read pH sensor and convert to pH scale
float readPH() {
  int sensorValue = analogRead(pHpin);
  float voltage = (sensorValue / 4095.0) * 3.3;
  float pH = phSlope * voltage + phIntercept;
  return pH;
}

// Read turbidity sensor
float readTurbidity() {
  int sensorValue = analogRead(turbidityPin);
  float voltage = (sensorValue / 4095.0) * 3.3;
  float turbidity = turbiditySlope * voltage + turbidityIntercept;
  if (turbidity < 0) turbidity = 0;
  return turbidity;
}

// Read and normalize RGB color sensor data (scaled 0–100)
void readRGB(float &rNorm, float &gNorm, float &bNorm) {
  uint16_t r, g, b, c;
  tcs.getRawData(&r, &g, &b, &c);
  if (c == 0) c = 1;
  rNorm = ((float)r / c) * 100.0;
  gNorm = ((float)g / c) * 100.0;
  bNorm = ((float)b / c) * 100.0;
}

// Classification logic + LED control
String classifyOil(float turbidityValue, float colorValue, int &oilStatusNo) {
  String oilStatus;

  if (turbidityValue < 200 && colorValue > 30) {
    oilStatus = "Good Oil";
    digitalWrite(greenLED, HIGH);
    digitalWrite(yellowLED, LOW);
    digitalWrite(redLED, LOW);
    oilStatusNo = 1;
  } 
  else if (turbidityValue > 500 && colorValue > 20) {
    oilStatus = "Used Oil";
    digitalWrite(greenLED, LOW);
    digitalWrite(yellowLED, HIGH);
    digitalWrite(redLED, LOW);
    oilStatusNo = 2;
  } 
  else {
    oilStatus = "Bad Oil";
    digitalWrite(greenLED, LOW);
    digitalWrite(yellowLED, LOW);
    digitalWrite(redLED, HIGH);
    oilStatusNo = 3;
  }

  return oilStatus;
}

// Convert text label to numeric code
int classifyCode(String quality) {
  if (quality == "Good Oil") return 1;
  if (quality == "Used Oil") return 2;
  if (quality == "Bad Oil") return 3;
  return 0;
}
