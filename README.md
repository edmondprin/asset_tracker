# IT Asset Tracker

## About
- Program allowing a user, typically an IT admin, to manage their fleet of devices via CLI app.

## Requirements
- Python installed on your machine: https://www.python.org/downloads/

## How to run
- python3 asset_tracker.py

## Skills demonstrated
- OOP with all four pillars: classes/objects, encapsulation, inheritance, polymorphism.
- Data validation via @property and setter, invalid status rejected at class level.
- Inheritance hierarchy: Laptop and NetworkDevice extend a base Asset class.
- JSON persistence — assets save on exit and reload on startup.
- CLI menu with input handling and separation of concerns.

## Features
- Add, list, find, and update assets via CLI.
- Supports multiple device types: generic assets, laptops, network devices.
- Invalid data rejected automatically, no crashes on bad input.
- Data persists between sessions via data.json.
