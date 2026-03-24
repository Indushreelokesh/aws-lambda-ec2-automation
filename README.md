 AWS Lambda EC2 Automation

 Objective
Automate starting and stopping EC2 instances using AWS Lambda and Boto3.

 Steps Followed

1. Created 2 EC2 instances
   <img width="873" height="574" alt="image" src="https://github.com/user-attachments/assets/e4f5ea1d-7320-4f1b-bbfd-1786b281c0c9" />

3. Added tags:
   - Instance 1 → Action: Auto-Stop
   - <img width="880" height="215" alt="image" src="https://github.com/user-attachments/assets/2cd4cec2-6e9d-4bf1-9aa5-9689e5f81d3e" />
   - Instance 2 → Action: Auto-Start
  <img width="1522" height="620" alt="image" src="https://github.com/user-attachments/assets/fa902d73-b6b3-4c1a-93e1-94a3df68dc5d" />

    
4. Created IAM Role with EC2 permissions
   <img width="888" height="434" alt="image" src="https://github.com/user-attachments/assets/d3c47e0a-b08f-45ef-8326-f1e50b80ae02" />
   <img width="892" height="529" alt="image" src="https://github.com/user-attachments/assets/5f2acd71-9397-48ef-b1e1-50d7c287d7e4" />


6. Created Lambda function using Python

8. Wrote Boto3 script to:
   - Stop Auto-Stop instances
   - Start Auto-Start instances
9. Tested using Lambda Test Event

<img width="902" height="514" alt="image" src="https://github.com/user-attachments/assets/de0b10b6-d10c-4634-b630-7055a31eb257" />


 Output
- Auto-Stop instance → Stopped
- Auto-Start instance → Running


 Technologies Used
- AWS Lambda
- EC2
- Boto3
