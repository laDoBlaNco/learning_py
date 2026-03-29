# errorsalert.py
alert_system = "email"  # other value can be "email"
error_severity = "critical"  # other values: "medium" or "low"
error_message = "Something terrible happened!"

def send_email(address, err_msg):
    print(address, err_msg)
    
    
if alert_system == "console":  # outer
    print(error_message)  # 1
elif alert_system == "email":
    if error_severity == "critical":  # inner
        send_email("admin@example.com", error_message)
    elif error_severity=='medium':
        send_email("support.1@example.com", error_message)  # 3
    else:
        send_email("support.2@example.com", error_message)  # 4

