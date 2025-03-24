# Recruitment Outreach Automation

A Python-based automation tool designed to streamline the recruitment outreach process. This project features an email automation script that sends personalized messages to recruiters and a browser script for extracting recruiter information from web pages. Built to enhance efficiency and reduce manual effort, making it easier for job seekers to connect with potential employers.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)

## Features

- Automates the process of sending personalized outreach emails to recruiters.
- Extracts recruiter information (name and email) from web pages using a browser script.
- Easily customizable email templates and configurations.

## Technologies Used

- Python
- smtplib
- MIME (email handling)
- Tampermonkey (browser script)

## Getting Started

### Prerequisites

- Python 3.x
- An email account (e.g., Gmail) for sending emails
- Tampermonkey browser extension

### Installing Tampermonkey

To use the Tampermonkey script for extracting recruiter information, follow these steps:

#### Download Tampermonkey:

1. Go to the [Tampermonkey website](https://www.tampermonkey.net/).
2. Choose your browser and click on the corresponding download link (available for Chrome, Firefox, Edge, Safari, etc.).

#### Add the Tampermonkey Extension:

1. Follow the prompts to install the extension in your browser.

#### Add the Script:

1. Click on the Tampermonkey icon in your browser toolbar.
2. Select **Create a New Script**.
3. Delete the default code in the editor and paste the Tampermonkey script from this repository.
4. Adjust the `@match` line to specify the website(s) you want to scrape.
5. Click **File** > **Save** to save your script.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Recruitment-Outreach-Automation.git
   cd Recruitment-Outreach-Automation

## Usage

1. Prepare a text file named `recruiter_emails.txt` with the format:
   email1@example.com, Name1 email2@example.com, Name2

2. Update the `RESUME_PATH` variable in the Python script to point to your resume file.

3. Customize the email subject and body in the script:
- Change the `SUBJECT` variable to your desired subject line.
- Update the `EMAIL_BODY` variable with your message template.

4. Run the Python script `python send_email_git.py`

5. Use the Tampermonkey script to extract recruiter information from the specified web pages:
   Adjust the @match line to match the URL pattern of the websites you want to scrape.
