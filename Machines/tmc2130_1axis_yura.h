#pragma once
// clang-format off

#define MACHINE_NAME    "ESP32_TMC2130_YU-RA-A"
#define X_LIMIT_PIN     GPIO_NUM_34

#define TRINAMIC_RUN_MODE           TrinamicMode :: StealthChop//CoolStep
#define TRINAMIC_HOMING_MODE        TrinamicMode :: StealthChop//CoolStep

#define X_STEP_PIN              GPIO_NUM_17
#define X_DIRECTION_PIN         GPIO_NUM_16
#define X_TRINAMIC_DRIVER       2130        // Which Driver Type?
#define X_CS_PIN                GPIO_NUM_21  //chip select
#define X_RSENSE                TMC2130_RSENSE_DEFAULT


// OK to comment out to use pin for other features
#define STEPPERS_DISABLE_PIN GPIO_NUM_22

#define USER_ANALOG_PIN_0      GPIO_NUM_2
#define USER_ANALOG_PIN_1      GPIO_NUM_4


// https://github.com/bdring/Grbl_Esp32/wiki/Setting-Defaults
#define DEFAULT_SOFT_LIMIT_ENABLE 1 // true
#define DEFAULT_HARD_LIMIT_ENABLE 1 // true
#define DEFAULT_HOMING_ENABLE 1     // true
#define DEFAULT_HOMING_PULLOFF 5    //5mm

#define DEFAULT_STEPPER_IDLE_LOCK_TIME 255

#define DEFAULT_X_STEPS_PER_MM 80


