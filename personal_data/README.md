# Personal Data

## Overview

This project aims to demonstrate secure practices for managing personal data, particularly Personally Identifiable Information (PII), within software applications. It covers techniques for logging, PII obfuscation, password encryption, and database authentication using Python.

## Learning Objectives

At the end of this project, you will be able to:

- Identify Personally Identifiable Information (PII) and examples of such data.
- Implement a logging system that filters and obfuscates PII fields from log messages.
- Encrypt passwords securely using bcrypt and validate user input passwords.
- Authenticate to a database securely using environment variables.

## Requirements

- Operating System: Ubuntu 18.04 LTS
- Python Version: 3.7
- Coding Style: PEP 8 (pycodestyle version 2.5)
- Encryption Library: bcrypt (install using `pip install bcrypt`)

## Implementation Details

- **Logging System**: Implements a custom logging filter to scan log messages for PII fields and obfuscate them. Log messages are written to files with configurable log levels and formatting.

- **Password Management**: Utilizes the bcrypt package to securely hash passwords for storage in a database. Provides functions for password encryption and validation to ensure user authentication.

- **Database Authentication**: Demonstrates how to authenticate to a database securely using environment variables for storing sensitive credentials. Establishes a connection to the database without exposing credentials in the source code.
