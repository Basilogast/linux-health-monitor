#!/bin/bash

echo "--- Installing Health Monitor ---"

# 1. Create directory
sudo mkdir -p /opt/health-monitor

# 2. Copy application
sudo cp monitor.py /opt/health-monitor/
sudo chmod +x /opt/health-monitor/monitor.py

# 3. Copy systemd service
sudo cp health-monitor.service /etc/systemd/system/

# 4. Enable and Start
sudo systemctl daemon-reload
sudo systemctl enable health-monitor
sudo systemctl start health-monitor

echo "--- Installation Complete! Check status with: systemctl status health-monitor ---"