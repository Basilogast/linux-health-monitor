# Linux System Health Monitor Service

A lightweight, open-source background daemon designed to monitor Linux server resources (Disk Usage) and log critical states directly to the System Journal. 

This project demonstrates **Systems Engineering** fundamentals, including creating Systemd units, managing background processes (daemons), and automating deployment via Bash scripting.

## 🚀 Features

* **Background Execution:** Runs as a fully managed `systemd` service (starts automatically on boot).
* **Resource Monitoring:** Continuously checks disk usage using Python's system libraries.
* **System Integration:** Utilizes the native Linux logging standard (`journalctl`) instead of simple text files.
* **Automated Deployment:** Includes a Bash script to handle permission setting, file copying, and service enablement.

## 🛠️ Technical Stack

* **Language:** Python 3.x (System interaction)
* **Process Manager:** Systemd (Service lifecycle management)
* **Automation:** Bash Scripting
* **OS:** Ubuntu / Debian / WSL2

## 📂 Project Structure

* `monitor.py`: The core logic. Checks system resources and writes to `stdout` (captured by the journal).
* `health-monitor.service`: The Systemd Unit file defining the service configuration, restart policies, and user permissions.
* `install.sh`: A script to automate the installation process (creates directories, moves files, enables services).

## 📥 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/linux-health-monitor.git](https://github.com/YOUR_USERNAME/linux-health-monitor.git)
    cd linux-health-monitor
    ```

2.  **Run the automated installer:**
    ```bash
    chmod +x install.sh
    sudo ./install.sh
    ```

    *The script will automatically move files to `/opt/`, configure systemd, and start the service.*

## 🔍 Verification & Usage

Once installed, you can manage the service using standard Linux systems administration commands:

### Check Service Status
Verify the daemon is active and running:
```bash
sudo systemctl status health-monitor